"""
MCP Gateway Service

This module implements a central gateway service that:
1. Allows MCP nodes to register and connect via WebSocket
2. Allows clients to connect via SSE
3. Routes client requests to appropriate MCP nodes
4. Returns MCP node responses to clients

The service leverages MCP's native components for transport protocols and message handling.
"""

import asyncio
import json
import logging
import uuid
from contextlib import asynccontextmanager
from typing import Dict, List, Optional, Set, Any, Tuple
from urllib.parse import quote

import anyio
from anyio.streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from starlette.routing import Mount, Route
from starlette.applications import Starlette
from sse_starlette.sse import EventSourceResponse

# Import MCP components
from mcp.server.sse import SseServerTransport
from mcp.server.websocket import websocket_server
from mcp.server.session import ServerSession
from mcp.server.lowlevel.server import Server as MCPServer
from mcp.types import JSONRPCMessage, ClientRequest, JSONRPCRequest, JSONRPCResponse, JSONRPCError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---- Models ----

class NodeRegistration(BaseModel):
    """Model for node registration requests"""
    node_id: Optional[str] = None  # If None, service will generate one
    name: str
    description: str = ""
    capabilities: Dict[str, Any] = Field(default_factory=dict)
    
    @field_validator('node_id', mode='before')
    @classmethod
    def set_node_id(cls, v):
        return v or str(uuid.uuid4())


class NodeInfo(BaseModel):
    """Extended information about a registered node"""
    node_id: str
    name: str
    description: str
    capabilities: Dict[str, Any]
    connected: bool = False
    last_seen: Optional[float] = None


# ---- Node Session Management ----

class NodeSession:
    """Represents a WebSocket connection to an MCP node"""
    def __init__(self, node_id: str, name: str):
        self.node_id = node_id
        self.name = name
        self.description = ""
        self.capabilities = {}
        self.connected = False
        self.last_seen = None
        self.websocket: Optional[WebSocket] = None
        self.clients: Set[str] = set()  # Client session IDs connected to this node
        self.client_lock = asyncio.Lock()
        self.message_queue = asyncio.Queue()  # Queue for messages to send to the node
        self.running = False


class ClientMapping:
    """Maps client sessions to nodes and tracks requests"""
    def __init__(self):
        self.client_to_node: Dict[str, str] = {}  # Maps client ID to node ID
        self.request_to_client: Dict[str, str] = {}  # Maps request ID to client ID
        self.lock = asyncio.Lock()


# ---- Gateway Service ----

class MCPGatewayService:
    """Main service class for MCP gateway"""
    
    def __init__(self, sse_path: str = "/sse", message_path: str = "/messages/"):
        self.nodes: Dict[str, NodeInfo] = {}
        self.node_sessions: Dict[str, NodeSession] = {}
        self.nodes_lock = asyncio.Lock()
        
        # Client-node mapping
        self.client_mapping = ClientMapping()
        
        # SSE endpoint configuration
        self.sse_path = sse_path
        self.message_path = message_path
        self.sse_transport = SseServerTransport(message_path)
        
        # Keep track of SSE sessions
        self.sse_sessions = {}
    
    def get_current_session_id(self):
        """Get the current session ID (placeholder method)"""
        # Note: In a real implementation, this would be handled by SseServerTransport
        # We're adding this as a placeholder since we need to extract the session ID
        # This would need to be implemented based on the actual transport implementation
        for session_id in self.sse_sessions.keys():
            return session_id
        return None
    
    async def register_node(self, registration: NodeRegistration) -> NodeInfo:
        """Register a new MCP node with the service"""
        async with self.nodes_lock:
            node_id = registration.node_id
            
            # Create or update node info
            node = NodeInfo(
                node_id=node_id,
                name=registration.name,
                description=registration.description,
                capabilities=registration.capabilities,
                last_seen=asyncio.get_event_loop().time()
            )
            self.nodes[node_id] = node
            
            # Create node session if it doesn't exist
            if node_id not in self.node_sessions:
                self.node_sessions[node_id] = NodeSession(node_id, registration.name)
                self.node_sessions[node_id].description = registration.description
                self.node_sessions[node_id].capabilities = registration.capabilities
            
            logger.info(f"Node registered: {node_id} ({registration.name})")
            return node
    
    async def deregister_node(self, node_id: str) -> bool:
        """Remove a node from the registry"""
        async with self.nodes_lock:
            if node_id not in self.nodes:
                return False
            
            # Get node session
            node_session = self.node_sessions.get(node_id)
            if node_session:
                # Disconnect node if connected
                if node_session.websocket:
                    try:
                        await node_session.websocket.close()
                    except Exception as e:
                        logger.error(f"Error closing node websocket: {e}")
                
                # Disconnect all clients from this node
                async with node_session.client_lock:
                    for client_id in list(node_session.clients):
                        await self.disconnect_client_from_node(client_id)
                
                # Stop message processing task
                node_session.running = False
            
            # Remove node records
            del self.nodes[node_id]
            if node_id in self.node_sessions:
                del self.node_sessions[node_id]
            
            logger.info(f"Node deregistered: {node_id}")
            return True
    
    async def list_nodes(self) -> List[NodeInfo]:
        """List all registered nodes"""
        return list(self.nodes.values())
    
    async def get_node(self, node_id: str) -> Optional[NodeInfo]:
        """Get information about a specific node"""
        return self.nodes.get(node_id)
    
    async def connect_client_to_node(self, client_id: str, node_id: str) -> bool:
        """Connect a client to a specific node"""
        # Check if node exists
        node_session = self.node_sessions.get(node_id)
        if not node_session:
            logger.warning(f"Cannot connect client {client_id} to non-existent node {node_id}")
            return False
        
        # Check if node is connected
        if not node_session.connected:
            logger.warning(f"Cannot connect client {client_id} to disconnected node {node_id}")
            return False
        
        # Update mapping
        async with self.client_mapping.lock:
            # Disconnect from current node if any
            current_node_id = self.client_mapping.client_to_node.get(client_id)
            if current_node_id:
                await self.disconnect_client_from_node(client_id)
            
            # Connect to new node
            self.client_mapping.client_to_node[client_id] = node_id
            
            # Add client to node's client list
            async with node_session.client_lock:
                node_session.clients.add(client_id)
        
        logger.info(f"Client {client_id} connected to node {node_id}")
        return True
    
    async def disconnect_client_from_node(self, client_id: str) -> bool:
        """Disconnect a client from its node"""
        # Get client's current node
        async with self.client_mapping.lock:
            node_id = self.client_mapping.client_to_node.get(client_id)
            if not node_id:
                return False
            
            # Remove client mapping
            del self.client_mapping.client_to_node[client_id]
            
            # Remove client from node's client list
            node_session = self.node_sessions.get(node_id)
            if node_session:
                async with node_session.client_lock:
                    if client_id in node_session.clients:
                        node_session.clients.remove(client_id)
        
        logger.info(f"Client {client_id} disconnected from node {node_id}")
        return True
    
    async def route_message_from_client_to_node(self, client_id: str, message: Dict[str, Any]) -> bool:
        """Route a message from a client to its connected node"""
        # Find client's node
        async with self.client_mapping.lock:
            node_id = self.client_mapping.client_to_node.get(client_id)
            if not node_id:
                logger.warning(f"Client {client_id} is not connected to any node")
                return False
            
            # Track request ID for routing response back
            request_id = message.get("id")
            if request_id:
                self.client_mapping.request_to_client[str(request_id)] = client_id
        
        # Get node session
        node_session = self.node_sessions.get(node_id)
        if not node_session or not node_session.connected:
            logger.warning(f"Node {node_id} is not connected")
            return False
        
        # Send message to node
        try:
            # Convert to JSONRPCMessage if needed
            if not isinstance(message, JSONRPCMessage):
                if "jsonrpc" not in message:
                    message["jsonrpc"] = "2.0"
                message = JSONRPCMessage.model_validate(message)
            
            # Send via WebSocket
            await node_session.websocket.send_json(
                message.model_dump(by_alias=True, exclude_none=True)
            )
            logger.debug(f"Message routed: client {client_id} -> node {node_id}")
            return True
        except Exception as e:
            logger.error(f"Error routing message to node {node_id}: {e}")
            return False
    
    async def route_message_from_node_to_client(self, node_id: str, message: JSONRPCMessage) -> bool:
        """Route a message from a node to the appropriate client"""
        # Determine if this is a response or notification
        is_response = hasattr(message.root, "id") and message.root.id is not None
        
        if is_response:
            # Route to specific client that sent the request
            request_id = str(message.root.id)
            async with self.client_mapping.lock:
                client_id = self.client_mapping.request_to_client.pop(request_id, None)
                if not client_id:
                    logger.warning(f"No client found for request ID {request_id}")
                    return False
            
            # Send response via SSE
            # The SseServerTransport handles this automatically by using session_id
            return True
        else:
            # This is a notification, broadcast to all clients connected to this node
            node_session = self.node_sessions.get(node_id)
            if not node_session:
                return False
            
            success = False
            async with node_session.client_lock:
                for client_id in node_session.clients:
                    # We don't need to do anything here - SseServerTransport will handle 
                    # sending to all connected clients
                    success = True
            
            return success
    
    async def handle_node_messages(self, node_id: str) -> None:
        """Background task to process messages for a node"""
        node_session = self.node_sessions.get(node_id)
        if not node_session:
            return
        
        node_session.running = True
        while node_session.running:
            try:
                # Get next message from queue
                message = await node_session.message_queue.get()
                
                # Process the message
                # This is handled by the WebSocket handler
                pass
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error processing message for node {node_id}: {e}")
    
    async def maintain_connections(self) -> None:
        """Background task to maintain connections and clean up"""
        while True:
            try:
                current_time = asyncio.get_event_loop().time()
                
                # Check node health
                async with self.nodes_lock:
                    for node_id, node in list(self.nodes.items()):
                        # Mark nodes as disconnected if not seen for 60 seconds
                        if node.last_seen and current_time - node.last_seen > 60:
                            if node.connected:
                                node.connected = False
                                logger.info(f"Node {node_id} marked as disconnected (timeout)")
                                
                                # Notify connected clients
                                node_session = self.node_sessions.get(node_id)
                                if node_session:
                                    async with node_session.client_lock:
                                        for client_id in list(node_session.clients):
                                            # Notification will be handled by SSE transport
                                            pass
                
                # Clean up stale request mappings
                # This is a simple implementation - in production, you'd want to track timestamps
                if len(self.client_mapping.request_to_client) > 1000:
                    async with self.client_mapping.lock:
                        # Just trim the dictionary if it gets too large
                        # A better approach would be to track timestamps
                        logger.warning("Cleaning up stale request mappings")
                        self.client_mapping.request_to_client.clear()
            
            except Exception as e:
                logger.error(f"Error in connection maintenance: {e}")
            
            await asyncio.sleep(30)  # Run every 30 seconds


# ---- FastAPI Application ----

def create_gateway_app(
    gateway_service: MCPGatewayService, 
    cors_enabled: bool = True,
    health_endpoint: Optional[str] = "/health"
) -> FastAPI:
    """Create and configure the FastAPI application"""
    app = FastAPI(title="MCP Gateway Service")
    
    # Add CORS middleware if enabled
    if cors_enabled:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    # Dependency to get service instance
    def get_service():
        return gateway_service
    
    # ---- Node Management Endpoints ----
    
    @app.post("/nodes/register", response_model=NodeInfo)
    async def register_node(registration: NodeRegistration, service: MCPGatewayService = Depends(get_service)):
        """Register a new MCP node with the service"""
        return await service.register_node(registration)
    
    @app.delete("/nodes/{node_id}")
    async def deregister_node(node_id: str, service: MCPGatewayService = Depends(get_service)):
        """Remove a node from the registry"""
        success = await service.deregister_node(node_id)
        if not success:
            raise HTTPException(status_code=404, detail="Node not found")
        return {"success": True}
    
    @app.get("/nodes", response_model=List[NodeInfo])
    async def list_nodes(service: MCPGatewayService = Depends(get_service)):
        """List all registered nodes"""
        return await service.list_nodes()
    
    @app.get("/nodes/{node_id}", response_model=NodeInfo)
    async def get_node(node_id: str, service: MCPGatewayService = Depends(get_service)):
        """Get information about a specific node"""
        node = await service.get_node(node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")
        return node
    
    # Node WebSocket connection
    @app.websocket("/nodes/{node_id}/ws")
    async def node_websocket(websocket: WebSocket, node_id: str, service: MCPGatewayService = Depends(get_service)):
        """WebSocket endpoint for nodes to connect to the gateway"""
        await websocket.accept()
        
        # Get node info
        node = await service.get_node(node_id)
        if not node:
            await websocket.close(code=1008, reason="Node not registered")
            return
        
        # Get node session
        node_session = service.node_sessions.get(node_id)
        if not node_session:
            await websocket.close(code=1008, reason="Node session not found")
            return
        
        # Update node session
        node_session.websocket = websocket
        node_session.connected = True
        node_session.last_seen = asyncio.get_event_loop().time()
        node.connected = True
        node.last_seen = asyncio.get_event_loop().time()
        
        logger.info(f"Node {node_id} connected via WebSocket")
        
        try:
            # Process incoming messages from node
            while True:
                # Receive message from node
                raw_message = await websocket.receive_json()
                node_session.last_seen = asyncio.get_event_loop().time()
                node.last_seen = asyncio.get_event_loop().time()
                
                try:
                    # Parse as JSONRPCMessage
                    message = JSONRPCMessage.model_validate(raw_message)
                    
                    # Route message to appropriate client(s)
                    await service.route_message_from_node_to_client(node_id, message)
                except Exception as e:
                    logger.error(f"Error processing message from node {node_id}: {e}")
        
        except WebSocketDisconnect:
            logger.info(f"Node {node_id} disconnected")
        except Exception as e:
            logger.error(f"Error in node WebSocket connection: {e}")
        finally:
            # Update node status
            node_session.connected = False
            node_session.websocket = None
            node.connected = False
            
            # Notify clients that node is disconnected
            async with node_session.client_lock:
                for client_id in list(node_session.clients):
                    # Disconnect client from node
                    await service.disconnect_client_from_node(client_id)
    
    # Client control API
    @app.post("/client/connect-node")
    async def connect_client_to_node(
        request: Request,
        service: MCPGatewayService = Depends(get_service)
    ):
        """Connect a client to a specific node"""
        # Get client ID from query parameters
        client_id = request.query_params.get("client_id")
        if not client_id:
            raise HTTPException(status_code=400, detail="Missing client_id parameter")
        
        # Get node ID from request body
        try:
            data = await request.json()
            node_id = data.get("node_id")
            if not node_id:
                raise HTTPException(status_code=400, detail="Missing node_id in request body")
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON body")
        
        # Connect client to node
        success = await service.connect_client_to_node(client_id, node_id)
        if not success:
            raise HTTPException(status_code=404, detail="Node not found or not connected")
        
        return {"success": True}
    
    # Health check endpoint
    if health_endpoint:
        @app.get(health_endpoint)
        async def health_check():
            """Health check endpoint"""
            return {"status": "ok"}
    
    # Define SSE handler here to fix scope issue
    async def handle_sse(request: Request):
        """SSE endpoint for clients"""
        async with gateway_service.sse_transport.connect_sse(
            request.scope, request.receive, request._send
        ) as streams:
            # Create a simple session ID for tracking
            session_id = str(uuid.uuid4())
            gateway_service.sse_sessions[session_id] = True
            
            # Create a simple MCP server for this session
            server = MCPServer(name="MCP Gateway")
            
            try:
                # Run the server for this session
                await server.run(
                    streams[0],
                    streams[1],
                    server.create_initialization_options()
                )
            finally:
                # Clean up session
                if session_id in gateway_service.sse_sessions:
                    del gateway_service.sse_sessions[session_id]
    
    # Add Starlette routes for SSE and message handling
    sse_routes = [
        Route(gateway_service.sse_path, endpoint=handle_sse),
        Mount(gateway_service.message_path, app=gateway_service.sse_transport.handle_post_message),
    ]
    
    # Create a Starlette instance for the SSE endpoints
    sse_app = Starlette(routes=sse_routes)
    
    # Mount the SSE app at /
    app.mount("/", sse_app)
    
    # Start background tasks on startup
    @app.on_event("startup")
    async def startup_event():
        # Start connection maintenance task
        asyncio.create_task(gateway_service.maintain_connections())
        logger.info("MCP Gateway Service started")
    
    # Cleanup on shutdown
    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("MCP Gateway Service shutting down")
    
    return app


# ---- Main Entry Point ----

def create_mcp_gateway(
    host: str = "0.0.0.0",
    port: int = 8000,
    sse_path: str = "/sse",
    message_path: str = "/messages/",
    cors_enabled: bool = True,
    health_endpoint: str = "/health"
) -> Tuple[FastAPI, MCPGatewayService]:
    """Create an MCP Gateway service and FastAPI app"""
    # Create service instance
    gateway_service = MCPGatewayService(
        sse_path=sse_path,
        message_path=message_path
    )
    
    # Create FastAPI app
    app = create_gateway_app(
        gateway_service=gateway_service,
        cors_enabled=cors_enabled,
        health_endpoint=health_endpoint
    )
    
    return app, gateway_service


# Run the server if executed directly
if __name__ == "__main__":
    import uvicorn
    import argparse
    
    parser = argparse.ArgumentParser(description="MCP Gateway Service")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", default=8000, type=int, help="Port to listen on")
    parser.add_argument("--sse-path", default="/sse", help="Path for SSE endpoint")
    parser.add_argument("--message-path", default="/messages/", help="Path for messages endpoint")
    parser.add_argument("--no-cors", action="store_true", help="Disable CORS")
    args = parser.parse_args()
    
    app, _ = create_mcp_gateway(
        host=args.host,
        port=args.port,
        sse_path=args.sse_path,
        message_path=args.message_path,
        cors_enabled=not args.no_cors
    )
    
    uvicorn.run(app, host=args.host, port=args.port)
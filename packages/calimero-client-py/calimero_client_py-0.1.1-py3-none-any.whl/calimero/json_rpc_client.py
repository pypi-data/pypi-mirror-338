import asyncio
import os
import time
import base58
import json
from typing import Optional, Dict, Any, TypedDict
import aiohttp
from .config import Config
from .keypair import Ed25519Keypair

class JsonRpcError(Exception):
    """Base exception for JSON-RPC errors."""
    pass

class JsonRpcResponse(TypedDict):
    """Type definition for JSON-RPC response."""
    jsonrpc: str
    id: int
    result: Optional[Dict[str, Any]]
    error: Optional[Dict[str, Any]]

class JsonRpcClient:
    """JSON-RPC client for Calimero.
    
    This client handles communication with the Calimero JSON-RPC server,
    including request formatting, signing, and response handling.
    """
    
    # Constants
    JSONRPC_VERSION = '2.0'
    DEFAULT_TIMEOUT = 1000
    JSONRPC_PATH = '/jsonrpc/dev'
    
    def __init__(self, config: Config):
        """Initialize the JSON-RPC client with a config.
        
        Args:
            config: Configuration object containing node URL and keypair.
            
        Raises:
            ValueError: If required environment variables are not set.
        """
        self.config = config
        self.node_url = config.node_url
        self.keypair = config.keypair
        self.context_id = os.getenv('CONTEXT_ID')
        self.executor_public_key = os.getenv('EXECUTOR_PUBLIC_KEY')
        
        self._validate_environment()
    
    def _validate_environment(self) -> None:
        """Validate that required environment variables are set.
        
        Raises:
            ValueError: If any required environment variable is missing.
        """
        if not self.context_id:
            raise ValueError("CONTEXT_ID environment variable is not set")
        if not self.executor_public_key:
            raise ValueError("EXECUTOR_PUBLIC_KEY environment variable is not set")
    
    def _prepare_headers(self) -> Dict[str, str]:
        """Prepare request headers with signature and timestamp.
        
        Returns:
            Dictionary containing request headers.
        """
        timestamp = str(int(time.time()))
        signature = self.keypair.sign(timestamp.encode())
        signature_b58 = base58.b58encode(signature).decode()
        
        return {
            'Content-Type': 'application/json',
            'X-Signature': signature_b58,
            'X-Timestamp': timestamp
        }
    
    def _prepare_request(self, method: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Prepare the JSON-RPC request payload.
        
        Args:
            method: The method to call.
            args: Optional arguments for the method.
            
        Returns:
            Dictionary containing the JSON-RPC request payload.
        """
        return {
            'jsonrpc': self.JSONRPC_VERSION,
            'id': 1,
            'method': 'execute',
            'params': {
                'contextId': self.context_id,
                'method': method,
                'argsJson': args or {},
                'executorPublicKey': self.executor_public_key,
                'timeout': self.DEFAULT_TIMEOUT
            }
        }
    
    async def _handle_response(self, response: aiohttp.ClientResponse) -> JsonRpcResponse:
        """Handle the JSON-RPC response.
        
        Args:
            response: The HTTP response from the server.
            
        Returns:
            Parsed JSON-RPC response.
            
        Raises:
            JsonRpcError: If the response indicates an error.
        """
        if response.status != 200:
            error_text = await response.text()
            raise JsonRpcError(f"HTTP error {response.status}: {error_text}")
        
        result = await response.json()
        if os.getenv('VERBOSE') == '1':
            print(f"Result: {json.dumps(result, indent=2)}")
            
        if 'error' in result:
            raise JsonRpcError(f"JSON-RPC error: {result['error']}")
            
        return result
    
    async def execute(self, method: str, args: Optional[Dict[str, Any]] = None) -> JsonRpcResponse:
        """Execute a JSON-RPC request.
        
        Args:
            method: The method to call.
            args: Optional arguments for the method.
            
        Returns:
            Parsed JSON-RPC response.
            
        Raises:
            JsonRpcError: If the request fails or returns an error.
        """
        headers = self._prepare_headers()
        payload = self._prepare_request(method, args)
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.node_url}{self.JSONRPC_PATH}",
                    headers=headers,
                    json=payload
                ) as response:
                    return await self._handle_response(response)
        except aiohttp.ClientError as e:
            raise JsonRpcError(f"Network error: {str(e)}")
        except json.JSONDecodeError as e:
            raise JsonRpcError(f"Invalid JSON response: {str(e)}") 
"""
Base client module with common client functionality.
"""
import logging
import aiohttp
from typing import Dict, Any, Optional, ClassVar, Type
import asyncio
from tenacity import (
    retry, 
    stop_after_attempt, 
    wait_exponential, 
    retry_if_exception_type, 
    before_sleep_log
)

logger = logging.getLogger(__name__)

class BaseClient:
    """
    Base client for making API calls.
    
    This is a singleton class - only one instance will be created.
    """
    # Singleton instance dictionary
    _instances: ClassVar[Dict[Type['BaseClient'], 'BaseClient']] = {}
    
    # Default base URL (should be overridden by subclasses or constructor)
    base_url: str = None
    
    # Default request timeout in seconds
    default_timeout: int = 30
    
    # Default number of retries for failed requests
    default_retries: int = 3
    
    def __new__(cls, *args, **kwargs):
        """Ensure only one client instance exists (singleton pattern)."""
        if cls not in cls._instances:
            cls._instances[cls] = super(BaseClient, cls).__new__(cls)
            # Initialize instance attributes
            instance = cls._instances[cls]
            instance._session = None
            instance._session_lock = asyncio.Lock()
        return cls._instances[cls]
    
    def __init__(self, host:str, port:int):
        """
        Initialize the base client.
        
        Args:
            host: Host name
            port: Port number
        """
        self.base_url = f"http://{host}:{port}"
    
    async def _ensure_session(self):
        """Initialize HTTP session if not already done."""
        if self._session is None or self._session.closed:
            async with self._session_lock:
                if self._session is None or self._session.closed:
                    try:
                        timeout = aiohttp.ClientTimeout(total=self.default_timeout)
                        connector = aiohttp.TCPConnector(ssl=False)
                        
                        self._session = aiohttp.ClientSession(
                            timeout=timeout,
                            headers={
                                "Accept-Encoding": "gzip, deflate",
                                "User-Agent": "python-aiohttp/at-backend-data-client"
                            },
                            connector=connector
                        )
                        logger.debug("Created new aiohttp session")
                    except Exception as e:
                        logger.error(f"Failed to create session: {repr(e)}")
                        self._session = None
                        raise
    
    async def close(self):
        """Close the HTTP session."""
        async with self._session_lock:
            if self._session and not self._session.closed:
                await self._session.close()
                self._session = None
    
    async def _request(
        self, 
        method: str, 
        endpoint: str, 
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Make a request to the API with retry logic.
        
        Args:
            method: HTTP method ('GET', 'POST', etc.)
            endpoint: API endpoint path
            json: JSON payload for the request
            params: Query parameters for the request
            
        Returns:
            Response from the API
        """
        @retry(
            stop=stop_after_attempt(self.default_retries),
            wait=wait_exponential(multiplier=1, min=2, max=30),
            retry=retry_if_exception_type((
                aiohttp.ClientError, 
                aiohttp.ClientResponseError, 
                asyncio.TimeoutError, 
                ConnectionError
            )),
            reraise=True,
            before_sleep=before_sleep_log(logger, logging.INFO)
        )
        async def _request_with_retry() -> Any:
            await self._ensure_session()
            
            try:
                url = f"{self.base_url}/{endpoint}"
                async with getattr(self._session, method.lower())(
                    url, json=json, params=params, raise_for_status=True
                ) as response:
                    return await response.json()
            except aiohttp.ClientResponseError as e:
                logger.error(f"HTTP error: {e.status} - {e.message}")
                if e.status == 429:  # Too Many Requests
                    retry_after = int(e.headers.get("Retry-After", 5))
                    logger.warning(f"Rate limit exceeded. Retrying after {retry_after}s")
                    await asyncio.sleep(retry_after)
                raise
            except Exception as e:
                logger.error(f"Request error: {repr(e)}")
                raise
                
        return await _request_with_retry()
    
    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a GET request to the API."""
        return await self._request("GET", endpoint, params=params)
    
    async def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Any:
        """Make a POST request to the API."""
        return await self._request("POST", endpoint, json=json)
    
    # Context manager support
    async def __aenter__(self):
        await self._ensure_session()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Don't close the session on exit - we want to keep it alive for reuse
        # The application should call close() explicitly when shutting down
        pass 
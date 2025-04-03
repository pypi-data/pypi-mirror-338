"""
External API client for the AT Backend Data service.
"""
import logging
from typing import List
import os

from .base import BaseClient

logger = logging.getLogger(__name__)

class ExternalClient(BaseClient):
    """Client for the AT Backend Data External API."""
    
    def __init__(self, host: str, port: int):
        """
        Initialize the External API client.
        
        Args:
            host: Host name
            port: Port number
        """
        super().__init__(host, port)
        self.base_url = f"{self.base_url}/external"
    
    #
    # Finnhub API
    #
    async def finnhub_list_stock(self) -> List[str]:
        """
        Get list of available stocks from Finnhub.
        
        Returns:
            List of stock symbols
        """
        return await self.post("finnhub/entry/stock/list")
    
    #
    # NasdaqTrader API
    #
    async def nasdaqtrader_list_stock(self) -> List[str]:
        """
        Get list of NASDAQ stocks from NasdaqTrader.
        
        Returns:
            List of NASDAQ stock symbols
        """
        return await self.post("nasdaqtrader/entry/stock/list") 
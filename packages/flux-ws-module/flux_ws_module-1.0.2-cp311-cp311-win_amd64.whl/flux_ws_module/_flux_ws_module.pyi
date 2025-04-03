
"""

        flux_ws_module
        -------------------
        A C++ library that provides WebSocket connections to different exchanges with same interface.

        This module allows connection to WebSocket servers, subscription to channels,
        placing and cancelling orders, and includes cryptographic functions for data encoding and hashing.
    
"""
from __future__ import annotations
from typing import Iterator, overload

__all__ = ['BaseExchangeConnector', 'OkxConnector', 'MexcConnector']
class BaseExchangeConnector:
    """
    
                BaseExchangeConnector
    
                A base class that provides common WebSocket connection functionality.
            
    """
    def connect(self, url: str) -> None:
        """
                        Connect to the WebSocket server.
        
                        Parameters:
                            url (str): The URL of the WebSocket server.
        
                        Returns:
                            A status or result of the connection attempt.
        """
    def disconnect(self) -> None:
        """
                        Disconnect from the WebSocket server.
        """

    def place_order(self, **kwargs) -> None:
        """
                        Place order on kwargs specified for exchange
        """

    def cancel_order(self, **kwargs) -> None:
        """
                        Place order on kwargs specified for exchange
        """
    
    def subscribe(self, **kwargs) -> None:
        """
                        Place order on kwargs specified for exchange
        """

    def unsubscribe(self, **kwargs) -> None:
        """
                        Place order on kwargs specified for exchange
        """
    
    def wsrun(self) -> Iterator[str]: ... 

class OkxConnector(BaseExchangeConnector):
    """
    
                WebSocket
    
                A specialized connector for OKX exchanges.
            
    """
    @overload
    def __init__(self) -> None:
        """
                        Constructor for public WebSocket.
        """
    @overload
    def __init__(self, API_key: str, API_secret: str, API_pass: str) -> None:
        """
                        Constructor for private WebSocket.
        
                        Parameters:
                            API_key (str)
                            API_secret (str)
                            API_pass (str)
        """
 
class MexcConnector(BaseExchangeConnector):
    """
    
                WebSocket
    
                A specialized connector for MEXC exchanges.
            
    """
    @overload
    def __init__(self) -> None:
        """
                        Constructor for public WebSocket.
        """
    @overload
    def __init__(self, API_key: str, API_secret: str, API_pass: str) -> None:
        """
                        Constructor for private WebSocket.
        
                        Parameters:
                            API_key (str)
                            API_secret (str)
                            API_pass (str)
        """
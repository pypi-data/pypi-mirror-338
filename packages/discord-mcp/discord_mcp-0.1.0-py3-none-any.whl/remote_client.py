#!/usr/bin/env python3
"""
Remote Client for Discord MCP Server

This module provides client functionality to communicate with a remote Discord data server.
It allows the MCP server running locally to access Discord data and BM25 search capabilities
hosted on a remote server.
"""

import json
import os
import logging
import requests
from typing import Dict, List, Optional, Any
from datetime import datetime

# Set up logging
logger = logging.getLogger(__name__)

class RemoteDiscordClient:
    """Client for interacting with a remote Discord data server."""
    
    def __init__(self, server_url: str, api_key: Optional[str] = None):
        """
        Initialize the remote client.
        
        Args:
            server_url: URL of the remote server API
            api_key: Optional API key for authentication
        """
        self.server_url = server_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        # Set up authentication if API key is provided
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})
        
        # Test connection
        try:
            self.check_connection()
            logger.info(f"Successfully connected to remote server at {server_url}")
        except Exception as e:
            logger.error(f"Failed to connect to remote server: {e}")
    
    def check_connection(self) -> bool:
        """
        Check if the connection to the remote server is working.
        
        Returns:
            bool: True if connection is successful
        """
        try:
            response = self.session.get(f"{self.server_url}/api/status")
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            logger.error(f"Connection test failed: {e}")
            raise ConnectionError(f"Could not connect to remote server: {e}")
    
    def get_channels(self) -> List[Dict[str, Any]]:
        """
        Get list of monitored Discord channels from the remote server.
        
        Returns:
            List of channel details
        """
        try:
            response = self.session.get(f"{self.server_url}/api/channels")
            response.raise_for_status()
            return response.json().get("channels", [])
        except requests.RequestException as e:
            logger.error(f"Failed to get channels: {e}")
            return []
    
    def keyword_search(self, 
                      query: str,
                      user: Optional[str] = None,
                      channel: Optional[str] = None,
                      days: Optional[int] = None,
                      after: Optional[str] = None,
                      before: Optional[str] = None,
                      limit: int = 30) -> str:
        """
        Perform keyword search on the remote server.
        
        Args:
            query: Text to search for
            user: Username filter
            channel: Channel name filter
            days: Number of days to look back
            after: Start date (YYYY-MM-DD)
            before: End date (YYYY-MM-DD)
            limit: Maximum results
            
        Returns:
            Formatted search results as string
        """
        try:
            params = {
                "query": query,
                "limit": limit
            }
            
            # Add optional parameters if provided
            if user:
                params["user"] = user
            if channel:
                params["channel"] = channel
            if days:
                params["days"] = days
            if after:
                params["after"] = after
            if before:
                params["before"] = before
            
            response = self.session.get(
                f"{self.server_url}/api/search/keyword",
                params=params
            )
            response.raise_for_status()
            
            return response.json().get("results", "No results found")
            
        except requests.RequestException as e:
            logger.error(f"Keyword search failed: {e}")
            return f"Search failed: {str(e)}"
    
    def search_discord(self, 
                       query: str,
                       user: Optional[str] = None,
                       channel: Optional[str] = None,
                       days: Optional[int] = None,
                       after: Optional[str] = None,
                       before: Optional[str] = None,
                       limit: int = 30,
                       min_relevance: float = 0.3) -> str:
        """
        Perform BM25 relevance search on the remote server.
        
        Args:
            query: Text to search for
            user: Username filter
            channel: Channel name filter
            days: Number of days to look back
            after: Start date (YYYY-MM-DD)
            before: End date (YYYY-MM-DD)
            limit: Maximum results
            min_relevance: Minimum relevance score (0-1) for including results
            
        Returns:
            Formatted search results as string
        """
        try:
            params = {
                "query": query,
                "limit": limit,
                "min_relevance": min_relevance
            }
            
            # Add optional parameters if provided
            if user:
                params["user"] = user
            if channel:
                params["channel"] = channel
            if days:
                params["days"] = days
            if after:
                params["after"] = after
            if before:
                params["before"] = before
            
            response = self.session.get(
                f"{self.server_url}/api/search",
                params=params
            )
            response.raise_for_status()
            
            return response.json().get("results", "No results found")
            
        except requests.RequestException as e:
            logger.error(f"Search failed: {e}")
            return f"Search failed: {str(e)}"
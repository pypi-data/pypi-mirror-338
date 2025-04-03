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
    
    def __init__(self, server_url: str):
        """
        Initialize the remote client.
        
        Args:
            server_url: URL of the Discord data API service
        """
        self.server_url = server_url.rstrip('/')
        self.session = requests.Session()
        
        # Test connection
        try:
            self.check_connection()
            logger.info(f"Successfully connected to Discord data API at {server_url}")
        except Exception as e:
            logger.error(f"Failed to connect to Discord data API: {e}")
    
    def check_connection(self) -> bool:
        """
        Check if the connection to the remote server is working.
        
        Returns:
            bool: True if connection is successful
        """
        # Try multiple possible API endpoints to be flexible with different server implementations
        endpoints = [
            "/api/status",
            "/status",
            "/api/health",
            "/"
        ]
        
        for endpoint in endpoints:
            try:
                logger.info(f"Trying to connect to {self.server_url}{endpoint}")
                response = self.session.get(f"{self.server_url}{endpoint}", timeout=5)
                if response.status_code < 400:
                    logger.info(f"Successfully connected to {self.server_url}{endpoint}")
                    return True
            except requests.RequestException as e:
                logger.debug(f"Endpoint {endpoint} failed: {e}")
                continue
        
        # If we get here, all endpoints failed
        logger.error(f"All connection attempts to {self.server_url} failed")
        raise ConnectionError(f"Could not connect to Discord data API at {self.server_url}")
    
    def get_channels(self) -> List[Dict[str, Any]]:
        """
        Get list of monitored Discord channels from the remote server.
        
        Returns:
            List of channel details
        """
        # Try multiple possible API endpoints
        endpoints = [
            "/api/channels", 
            "/channels",
            "/api/discord/channels"
        ]
        
        for endpoint in endpoints:
            try:
                logger.info(f"Trying to get channels from {self.server_url}{endpoint}")
                response = self.session.get(f"{self.server_url}{endpoint}", timeout=10)
                
                if response.status_code < 400:
                    data = response.json()
                    # Handle different response formats
                    if "channels" in data:
                        return data["channels"]
                    elif isinstance(data, list):
                        return data
                    else:
                        # If we got a valid response but unexpected format, log and try next endpoint
                        logger.warning(f"Unexpected response format from {endpoint}: {data}")
                        continue
            except requests.RequestException as e:
                logger.debug(f"Failed to get channels from {endpoint}: {e}")
                continue
            except json.JSONDecodeError as e:
                logger.warning(f"Invalid JSON response from {endpoint}: {e}")
                continue
        
        # If we get here, all endpoints failed
        logger.error("All attempts to get channels failed")
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
        # Try multiple possible API endpoints
        endpoints = [
            "/api/search",
            "/search",
            "/api/discord/search",
            "/api/messages/search"
        ]
        
        # Prepare search parameters
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
        
        # Try each endpoint
        for endpoint in endpoints:
            try:
                logger.info(f"Trying to search via {self.server_url}{endpoint}")
                response = self.session.get(
                    f"{self.server_url}{endpoint}",
                    params=params,
                    timeout=30  # Longer timeout for search
                )
                
                if response.status_code < 400:
                    data = response.json()
                    # Handle different response formats
                    if "results" in data:
                        return data["results"]
                    elif "messages" in data:
                        return data["messages"]
                    elif isinstance(data, list) or isinstance(data, str):
                        return data
                    else:
                        # If we got a valid response but unexpected format, just return it anyway
                        return str(data)
            except requests.RequestException as e:
                logger.debug(f"Search failed on endpoint {endpoint}: {e}")
                continue
            except json.JSONDecodeError as e:
                logger.warning(f"Invalid JSON response from search endpoint {endpoint}: {e}")
                continue
        
        # If we tried all endpoints and none worked
        logger.error("All search endpoints failed")
        return f"Search failed: Could not connect to any search API endpoint. Please check the server configuration."
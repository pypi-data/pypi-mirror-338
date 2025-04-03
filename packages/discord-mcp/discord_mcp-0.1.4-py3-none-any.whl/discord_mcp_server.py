#!/usr/bin/env python3
"""
Discord MCP Server

A Model Context Protocol server that allows Claude to access exported Discord channel messages.
"""

import json
import os
import re
import sys
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union

# Set up logging to file
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "discord_mcp.log")
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='a'
)
logger = logging.getLogger('discord_mcp')

# Also log to stderr
console = logging.StreamHandler(sys.stderr)
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

from mcp.server.fastmcp import FastMCP, Context

# Import our modules
logger.info("Importing discord_exporter modules and dependencies...")
logger.info(f"Current working directory: {os.getcwd()}")
logger.info(f"Script location: {os.path.dirname(os.path.abspath(__file__))}")
logger.info(f"Python executable: {sys.executable}")
logger.info(f"Python version: {sys.version}")

import sys
import traceback
logger.info(f"Python path: {sys.path}")

# Add the current directory to sys.path to help with imports
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    logger.info(f"Adding script directory to Python path: {script_dir}")
    sys.path.insert(0, script_dir)

# Import required modules
from discord_exporter import DiscordExporter
logger.info("Successfully imported DiscordExporter")

import requests
logger.info("Successfully imported requests")

import bm25s
logger.info("Successfully imported bm25s")

logger.info("BM25 search and Discord exporter modules successfully loaded.")

# Create an MCP server
mcp = FastMCP("Discord Messages")

# Configuration for Discord data access
# Get the Discord data URL from environment
DISCORD_DATA_URL = os.environ.get("DISCORD_DATA_URL")

# Log configuration
if DISCORD_DATA_URL:
    logger.info(f"Using Discord data API: {DISCORD_DATA_URL}")
else:
    logger.error("DISCORD_DATA_URL environment variable is not set. Please configure it in claude_desktop_config.json.")
    logger.error("Example: \"DISCORD_DATA_URL\": \"http://your-server:8081\"")

class DiscordMessageDB:
    """A simple database to manage and query Discord messages."""
    
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.messages = {}
        self.channels = {}
        self.users = {}
        self.load_data()
    
    def load_data(self):
        """Load all exported Discord data from the data directory."""
        if not self.data_dir.exists():
            logger.info(f"Data directory {self.data_dir} does not exist. Creating it.")
            self.data_dir.mkdir(parents=True, exist_ok=True)
            return
        
        # Load exported messages from the exports directory
        exports_dir = self.data_dir / "exports"
        
        if not exports_dir.exists():
            logger.info(f"Exports directory {exports_dir} does not exist.")
            return
            
        logger.info(f"Loading exported messages from {exports_dir}")
        
        # Process all JSON files in the exports directory
        for export_file in exports_dir.glob("*.json"):
            try:
                with open(export_file, 'r', encoding='utf-8') as f:
                    export_data = json.load(f)
                    
                    # Extract channel information
                    if 'guild' in export_data and 'channel' in export_data:
                        channel_data = export_data['channel']
                        channel_id = channel_data.get('id')
                        
                        if channel_id:
                            # Store channel info
                            self.channels[channel_id] = channel_data
                            
                            # Process messages
                            if 'messages' in export_data:
                                for message in export_data['messages']:
                                    message_id = message.get('id')
                                    if message_id:
                                        # Create channel dict if it doesn't exist
                                        if channel_id not in self.messages:
                                            self.messages[channel_id] = {}
                                        
                                        # Add timestamp for sorting and filtering
                                        if 'timestamp' in message:
                                            message['timestamp_obj'] = datetime.fromisoformat(
                                                message['timestamp'].replace('Z', '+00:00')
                                            )
                                        
                                        # Add channel info for reference
                                        message['channel_id'] = channel_id
                                        message['channel_name'] = channel_data.get('name', channel_id)
                                        
                                        # Store the message
                                        self.messages[channel_id][message_id] = message
                                        
                                        # Store user information
                                        author = message.get('author', {})
                                        author_id = author.get('id')
                                        if author_id:
                                            self.users[author_id] = author
                                            
                                logger.info(f"Loaded {len(export_data['messages'])} messages from {export_file.name}")
            except Exception as e:
                logger.error(f"Error processing export file {export_file}: {e}")
                continue
                
        # Log results
        total_messages = sum(len(msgs) for msgs in self.messages.values())
        logger.info(f"Loaded {total_messages} messages from {len(self.channels)} channels")
    
    def search_messages(self, 
                        query: Optional[str] = None, 
                        user: Optional[str] = None,
                        channel: Optional[str] = None,
                        days: Optional[int] = None,
                        start_date: Optional[datetime] = None,
                        end_date: Optional[datetime] = None,
                        limit: int = 50) -> List[Dict]:
        """
        Search for messages matching the given criteria.
        
        Args:
            query: Text to search for in message content
            user: Username or ID to filter by
            channel: Channel name or ID to filter by
            days: Number of days to look back from today
            start_date: Start date for date range search
            end_date: End date for date range search
            limit: Maximum number of results to return
            
        Returns:
            List of matching messages
        """
        results = []
        
        # Calculate date range if days is provided
        if days:
            from datetime import timezone
            end_date = datetime.now(timezone.utc)
            start_date = end_date - timedelta(days=days)
        
        # Determine channel ID if channel name is provided
        channel_id = None
        if channel:
            for ch_id, ch_data in self.channels.items():
                if channel.lower() in ch_data.get('name', '').lower() or channel == ch_id:
                    channel_id = ch_id
                    break
        
        # Determine user ID if username is provided
        user_id = None
        if user:
            for u_id, u_data in self.users.items():
                if (user.lower() in u_data.get('username', '').lower() or 
                    user.lower() in u_data.get('global_name', '').lower() or 
                    user == u_id):
                    user_id = u_id
                    break
                    
        # Get messages that match the criteria
        channels_to_search = [channel_id] if channel_id else self.messages.keys()
        
        for ch_id in channels_to_search:
            if ch_id not in self.messages:
                continue
                
            for msg_id, message in self.messages[ch_id].items():
                # Skip if doesn't match user filter
                if user_id and message.get('author', {}).get('id') != user_id:
                    continue
                
                # Skip if doesn't match date filter
                msg_timestamp = message.get('timestamp_obj')
                if msg_timestamp:
                    if start_date and msg_timestamp < start_date:
                        continue
                    if end_date and msg_timestamp > end_date:
                        continue
                
                # Skip if doesn't match content filter
                if query and not self._content_matches(message, query):
                    continue
                
                # Add channel information to the message
                message_copy = message.copy()
                message_copy['channel'] = self.channels.get(ch_id, {}).get('name', ch_id)
                message_copy['channel_id'] = ch_id
                
                results.append(message_copy)
                
                # Stop if we've reached the limit
                if len(results) >= limit:
                    break
        
        # Sort results by timestamp (newest first)
        results.sort(key=lambda x: x.get('timestamp_obj', datetime.min), reverse=True)
        
        return results[:limit]
    
    def _content_matches(self, message: Dict, query: str) -> bool:
        """
        Check if the message content contains the query string.
        
        Note: This is primarily used for simple keyword matching.
        BM25 search uses a different approach for relevance scoring.
        """
        if not query:  # Empty query matches everything
            return True
            
        content = message.get('content', '')
        return query.lower() in content.lower()
    
    def format_message(self, message: Dict) -> str:
        """Format a message for display."""
        author = message.get('author', {})
        username = author.get('nickname') or author.get('name') or author.get('global_name') or author.get('username', 'unknown')
        timestamp = message.get('timestamp', '')
        content = message.get('content', '')
        channel = message.get('channel', 'Unknown')
        
        # Format timestamp
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')
            except (ValueError, TypeError):
                formatted_time = timestamp
        else:
            formatted_time = 'Unknown time'
        
        return f"[{formatted_time}] #{channel} @{username}: {content}"
    
    def format_messages(self, messages: List[Dict]) -> str:
        """Format a list of messages for display."""
        if not messages:
            return "No messages found matching the criteria."
            
        return "\n\n".join(self.format_message(msg) for msg in messages)

# Initialize the Discord client that connects to the data URL
discord_client = None
if DISCORD_DATA_URL:
    try:
        from remote_client import RemoteDiscordClient
        logger.info(f"Initializing Discord client connection to {DISCORD_DATA_URL}")
        discord_client = RemoteDiscordClient(DISCORD_DATA_URL)
        logger.info("✅ Successfully connected to Discord data API")
    except Exception as e:
        logger.error(f"Error initializing Discord client: {e}", exc_info=True)
        logger.error("Make sure the Discord data service is running and the URL is correct")
else:
    logger.error("DISCORD_DATA_URL environment variable is required to run this service")
    logger.error("Please configure it in claude_desktop_config.json")

def format_search_results(results: List[Dict]) -> str:
    """
    Format search results for display.
    
    Args:
        results: List of search results
        
    Returns:
        Formatted string of search results
    """
    if not results:
        return "No matching messages found."
    
    formatted_results = []
    
    for result in results:
        # Format timestamp
        timestamp = result.get('timestamp', '')
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')
            except (ValueError, TypeError):
                formatted_time = timestamp
        else:
            formatted_time = 'Unknown time'
        
        # Format message
        channel_name = result.get('channel', 'Unknown')
        author = result.get('author', {})
        author_name = author.get('nickname') or author.get('name') or author.get('global_name') or author.get('username', 'unknown')
        content = result.get('content', '')
        relevance = result.get('relevance', 0.0)
        
        formatted_result = (
            f"[{formatted_time}] #{channel_name} @{author_name} "
            f"(Relevance: {relevance:.2f})\n"
            f"{content}"
        )
        
        formatted_results.append(formatted_result)
    
    return "\n\n".join(formatted_results)

@mcp.tool()
def search_discord(
    query: str,
    user: Optional[str] = None,
    channel: Optional[str] = None,
    days: Optional[int] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    limit: int = 30,
    min_relevance: float = 0.3
) -> str:
    """
    Search Discord messages using keyword matching with BM25 relevance scoring.
    
    Args:
        query: The text to search for in message content
        user: Optional username to filter messages by
        channel: Optional channel name to filter messages by
        days: Number of days to look back (from today)
        after: Get messages after this date (YYYY-MM-DD format)
        before: Get messages before this date (YYYY-MM-DD format)
        limit: Maximum number of results to return
        min_relevance: Minimum relevance score (0-1) for including results
        
    Returns:
        Formatted string of matching messages
    """
    if not discord_client:
        return "Discord client not initialized. Please ensure DISCORD_DATA_URL is set correctly."
    
    try:
        logger.info(f"Searching Discord messages via API: {query}")
        return discord_client.search_discord(
            query=query,
            user=user,
            channel=channel,
            days=days,
            after=after,
            before=before,
            limit=limit,
            min_relevance=min_relevance
        )
    except Exception as e:
        logger.error(f"Discord search failed: {e}", exc_info=True)
        return f"Error searching Discord messages: {str(e)}"

# Add a list_monitored_channels tool to retrieve the channels being monitored with their server names
@mcp.tool()
def list_monitored_channels() -> str:
    """
    Lists all Discord channels currently being monitored with their server names.
    
    Returns:
        A formatted list of monitored channels, including channel IDs, channel names, and server names
    """
    if not discord_client:
        return "Discord client not initialized. Please ensure DISCORD_DATA_URL is set correctly."
    
    logger.info("Fetching list of monitored channels with server information")
    try:
        channels = discord_client.get_channels()
        return format_channels(channels)
    except Exception as e:
        logger.error(f"Error getting monitored channels: {e}", exc_info=True)
        return f"Error retrieving monitored channels: {str(e)}"

def format_channels(channels):
    """Format channels received from the API"""
    if not channels:
        return "No channels are currently being monitored."
        
    result = "# Monitored Discord Channels\n\n"
    
    # Group channels by server
    servers = {}
    for channel in channels:
        server_name = channel.get('server_name', 'Unknown Server')
        if server_name not in servers:
            servers[server_name] = []
        servers[server_name].append(channel)
    
    # Sort servers by name
    sorted_servers = sorted(servers.items(), key=lambda x: x[0].lower())
    
    # Format channels by server
    for server_name, server_channels in sorted_servers:
        result += f"## {server_name}\n\n"
        
        # Sort channels by name
        sorted_channels = sorted(server_channels, key=lambda x: x.get('name', '').lower())
        
        for channel in sorted_channels:
            channel_name = channel.get('name', 'Unknown')
            channel_id = channel.get('id', 'Unknown')
            result += f"- #{channel_name} (`{channel_id}`)\n"
        
        result += "\n"
    
    # Add summary
    total_channels = sum(len(channels) for channels in servers.values())
    result += f"**Total Monitored Channels:** {total_channels}\n"
    result += f"**Total Servers:** {len(servers)}\n"
    
    return result

# Removed vector database functionality
# BM25 search is now used for relevance-based searching

# Export functionality removed - all data is accessed via the API

# Removed keyword_search_discord in favor of the new search_discord with BM25 relevance scoring

@mcp.resource("discord://help")
def get_help() -> str:
    """Return help information about the Discord MCP server."""
    help_text = """
Discord MCP Server Help

This server allows Claude to access and search through Discord messages using BM25 relevance-based search.

Available tools:
- search_discord: Search for messages with BM25 relevance scoring
- list_monitored_channels: List all Discord channels being monitored with their server names
"""

    examples = """
Example queries:
1. "Search for messages about feature requests"
2. "Find messages related to 'release date' with min_relevance=0.5"
3. "Search for 'bug report' in the #feedback channel"
4. "Find discussions about Claude and AI assistants" 
5. "Locate messages talking about upcoming events from the last 7 days"
6. "Search for conversations about technical issues"
7. "List all monitored Discord channels"
8. "Which Discord channels are currently being monitored?"

Data is automatically exported and loaded in the background.
"""

    return help_text + examples

@mcp.resource("discord://status")
def get_status() -> str:
    """Return the status of the Discord message database."""
    if not discord_client:
        return "Discord client not initialized. Please ensure DISCORD_DATA_URL is set correctly."
    
    try:
        # Check if channels exist - if any are available, we are initialized
        channels = discord_client.get_channels()
        channel_count = len(channels) if channels else 0
        
        # Create detailed status based on available data
        if channel_count > 0:
            status = f"""
Discord MCP Server Status:
- Connected to: {DISCORD_DATA_URL}
- Status: Ready
- Monitored channels: {channel_count}
- Search algorithm: BM25 relevance scoring
"""
        else:
            status = f"""
Discord MCP Server Status:
- Connected to: {DISCORD_DATA_URL}
- Status: Connected but no channels available
- Search algorithm: BM25 relevance scoring
"""
        return status
    except Exception as e:
        logger.error(f"Error getting status: {e}", exc_info=True)
        return f"Error getting Discord server status: {str(e)}"

@mcp.prompt()
def search_prompt(topic: str) -> str:
    """Create a prompt to search messages by topic using BM25 relevance scoring."""
    return f"Please search Discord messages about '{topic}' using BM25 relevance scoring and summarize the key discussion points."

@mcp.prompt()
def monitored_channels_prompt() -> str:
    """Create a prompt to list all monitored Discord channels."""
    return "Please list all the Discord channels that are currently being monitored, including their server names and channel names."

def main_cli():
    """Main entry point for the CLI."""
    # Check for host configuration for remote deployment
    mcp_host = os.environ.get("MCP_HOST", "127.0.0.1")
    
    # Log connectivity information
    logger.info(f"Starting MCP server on {mcp_host}:21001...")
    if mcp_host == "0.0.0.0":
        logger.info("Server configured for remote access (listening on all interfaces)")
        # Get the machine's IP addresses for easier connection
        import socket
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            logger.info(f"Local hostname: {hostname}")
            logger.info(f"Local IP address: {ip_address}")
            logger.info(f"Configure Claude Desktop to connect to: http://{ip_address}:21001")
        except Exception as e:
            logger.error(f"Could not determine IP address: {e}")
    
    # Run the MCP server with error handling
    try:
        # Run the server using the FastMCP instance we already created
        logger.info("Running MCP server with FastMCP")
        # FastMCP.run() doesn't accept host parameter
        # Set binding with an environment variable instead
        os.environ["MCP_BIND_ADDRESS"] = mcp_host
        logger.info(f"Set MCP_BIND_ADDRESS to {mcp_host}")
        mcp.run()
    except Exception as e:
        logger.error(f"Error running MCP server: {e}", exc_info=True)
        # Re-raise to ensure the error is visible
        raise

if __name__ == "__main__":
    main_cli()
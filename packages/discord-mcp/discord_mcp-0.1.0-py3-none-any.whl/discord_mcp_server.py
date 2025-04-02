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

# Path to the exported Discord data and configuration
DISCORD_DATA_DIR = os.environ.get("DISCORD_DATA_DIR", "./discord_data")
DISCORD_USER_TOKEN = os.environ.get("DISCORD_USER_TOKEN", None)

# Service URLs configuration - can be local or remote
DISCORD_API_URL = os.environ.get("DISCORD_API_URL")
API_KEY = os.environ.get("API_KEY")

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

# Note: Remote client functionality has been removed
# Only local database mode is now supported

# Initialize local database (always needed as fallback)
logger.info("Initializing local database as fallback")
db = DiscordMessageDB(DISCORD_DATA_DIR)

# Initialize exporter
exporter = None

try:
    # Make sure path exists
    exports_dir = Path(DISCORD_DATA_DIR) / "exports"
    exports_dir.mkdir(parents=True, exist_ok=True)
    
    # Create exporter with detailed setup
    logger.info(f"Setting up Discord exporter with output directory: {exports_dir}")
    exporter = DiscordExporter(output_dir=str(exports_dir), token=DISCORD_USER_TOKEN)
    
    # Check .NET availability immediately
    if exporter:
        dotnet_available = exporter.check_dotnet()
        if dotnet_available:
            logger.info("✅ .NET Runtime is available, Discord exporter should work properly.")
        else:
            logger.warning("⚠️ .NET Runtime is NOT available. Discord exporter may not work correctly without it.")
            logger.warning("Please install .NET Runtime from https://dotnet.microsoft.com/download")
except Exception as e:
    logger.error(f"Error initializing exporter: {e}", exc_info=True)
    logger.warning("Continuing with limited functionality...")

# Log configuration mode
logger.info("Using local database mode only with BM25 search")

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
    try:
        # Convert date strings to datetime objects if provided
        start_date = None
        end_date = None
        
        if after:
            try:
                start_date = datetime.fromisoformat(after)
                # Add timezone info if it's not present
                if start_date.tzinfo is None:
                    from datetime import timezone
                    start_date = start_date.replace(tzinfo=timezone.utc)
            except ValueError:
                return f"Invalid 'after' date format: {after}. Please use YYYY-MM-DD format."
                
        if before:
            try:
                end_date = datetime.fromisoformat(before)
                # Add timezone info if it's not present
                if end_date.tzinfo is None:
                    from datetime import timezone
                    end_date = end_date.replace(tzinfo=timezone.utc)
            except ValueError:
                return f"Invalid 'before' date format: {before}. Please use YYYY-MM-DD format."
        
        # Calculate date range if days is provided
        if days:
            from datetime import timezone
            end_date = datetime.now(timezone.utc)
            start_date = end_date - timedelta(days=days)
        
        # Get initial filtered results using existing search function
        # (This handles user/channel/date filtering)
        raw_results = db.search_messages(
            query="",  # Empty query to get all messages that match other filters
            user=user,
            channel=channel,
            days=days,
            start_date=start_date,
            end_date=end_date,
            limit=limit * 3  # Get more results for relevance scoring
        )
        
        # Skip BM25 scoring if no results or empty query
        if not raw_results:
            return "No messages found matching the criteria."
            
        if not query.strip():
            # If query is empty, just return the filtered results
            limited_results = raw_results[:limit]
            for result in limited_results:
                result['relevance'] = 1.0
            return format_search_results(limited_results)
            
        # Extract message contents
        contents = [msg.get('content', '') for msg in raw_results]
        
        # Using bm25s for efficient BM25 scoring
        # Tokenize the corpus
        logger.info(f"Tokenizing {len(contents)} messages for BM25 scoring")
        corpus_tokens = bm25s.tokenize(contents)
        
        # Create and index BM25 model
        logger.info("Creating and indexing BM25 model")
        retriever = bm25s.BM25()
        retriever.index(corpus_tokens)
        
        # Tokenize query
        query_tokens = bm25s.tokenize(query)
        
        # Get results and scores
        logger.info("Retrieving and scoring results with BM25")
        result_indices, scores = retriever.retrieve(
            query_tokens, 
            k=len(contents)  # Get all scores for our pre-filtered results
        )
        
        # Flatten result arrays (bm25s returns shape [n_queries, k])
        result_indices = result_indices[0]
        scores = scores[0]
        
        # Normalize scores to 0-1 range
        import numpy as np
        max_score = np.max(scores) if scores.size > 0 else 1.0
        if max_score > 0:
            normalized_scores = scores / max_score
        else:
            normalized_scores = scores
        
        # Filter and sort results
        scored_results = []
        for idx, score in zip(result_indices, normalized_scores):
            if score >= min_relevance:
                result_copy = raw_results[idx].copy()
                result_copy['relevance'] = float(score)  # Convert numpy float to Python float
                scored_results.append(result_copy)
        
        # Sort by relevance score
        scored_results.sort(key=lambda x: x['relevance'], reverse=True)
        
        # Limit results
        limited_results = scored_results[:limit]
        
        # Format results including the relevance score
        logger.info(f"Returning {len(limited_results)} messages above relevance threshold {min_relevance}")
        return format_search_results(limited_results)
        
    except Exception as e:
        logger.error(f"Error in search_discord: {e}", exc_info=True)
        return f"Error performing search: {str(e)}"

# Add a list_monitored_channels tool to retrieve the channels being monitored with their server names
@mcp.tool()
def list_monitored_channels() -> str:
    """
    Lists all Discord channels currently being monitored with their server names.
    
    Returns:
        A formatted list of monitored channels, including channel IDs, channel names, and server names
    """
    logger.info("Fetching list of monitored channels with server information")
    
    # Only local channel list is supported now
    
    # Local implementation - used if remote is not available or failed
    channels_file = os.environ.get("DISCORD_CHANNELS_FILE", "channels.txt")
    
    # Read the monitored channel IDs from channels.txt
    try:
        channel_ids = []
        channels_path = Path(os.path.dirname(os.path.abspath(__file__))) / channels_file
        
        if not channels_path.exists():
            return "No channels are currently being monitored. The channels file does not exist."
            
        with open(channels_path, 'r') as f:
            for line in f:
                channel_id = line.strip()
                if channel_id:  # Skip empty lines
                    channel_ids.append(channel_id)
                    
        if not channel_ids:
            return "No channels are currently being monitored."
            
        # Load Discord servers cache
        servers_cache_path = Path(os.path.dirname(os.path.abspath(__file__))) / "discord_servers_cache.json"
        servers = {}
        if servers_cache_path.exists():
            try:
                with open(servers_cache_path, 'r') as f:
                    servers = json.load(f)
            except json.JSONDecodeError:
                logger.error("Failed to parse discord_servers_cache.json")
        
        # Create a mapping of channel_id -> {server_name, channel_name}
        channel_info = {}
        
        # Look through all servers and find the channel details
        for server_name, server_data in servers.items():
            for channel in server_data.get('channels', []):
                if channel['id'] in channel_ids:
                    channel_info[channel['id']] = {
                        'server_name': server_name,
                        'channel_name': channel['name']
                    }
        
        # Format the results
        result = "# Monitored Discord Channels\n\n"
        
        # First list channels with known server and channel names
        known_channels = []
        for channel_id in channel_ids:
            if channel_id in channel_info:
                known_channels.append({
                    'id': channel_id,
                    'server_name': channel_info[channel_id]['server_name'],
                    'channel_name': channel_info[channel_id]['channel_name']
                })
        
        # Sort known channels by server name, then channel name
        known_channels.sort(key=lambda x: (x['server_name'].lower(), x['channel_name'].lower()))
        
        # Add known channels to the result
        if known_channels:
            result += "## Channels with Server Information\n\n"
            for channel in known_channels:
                result += f"- **{channel['server_name']}** / #{channel['channel_name']} (`{channel['id']}`)\n"
        
        # List channels without known server/channel names
        unknown_channels = [ch_id for ch_id in channel_ids if ch_id not in channel_info]
        if unknown_channels:
            if known_channels:
                result += "\n"
            result += "## Channels without Server Information\n\n"
            for channel_id in unknown_channels:
                result += f"- Channel ID: `{channel_id}`\n"
                
        # Add a summary
        result += f"\n**Total Monitored Channels:** {len(channel_ids)}\n"
        result += f"**Channels with Server Information:** {len(known_channels)}\n"
        result += f"**Channels without Server Information:** {len(unknown_channels)}\n"
            
        return result
            
    except Exception as e:
        logger.error(f"Error listing monitored channels: {e}", exc_info=True)
        return f"Error listing monitored channels: {str(e)}"

# Removed vector database functionality
# BM25 search is now used for relevance-based searching

# Internal function for background exports (not exposed as a tool)
def _export_discord_channel(
    channel_id: Union[str, int],
    token: Optional[str] = None,
    format: str = "Json",
    hours: Optional[int] = None,
    after: Optional[str] = None,
    before: Optional[str] = None
) -> str:
    """
    Internal function to export a Discord channel using DiscordChatExporter.
    
    Args:
        channel_id: The Discord channel ID to export
        token: Discord authentication token (optional if set in environment)
        format: Export format (Json, HtmlDark, HtmlLight, etc.)
        hours: Number of hours to look back (will set after parameter to current time minus hours)
        after: Get messages after this date (ISO 8601 format, e.g., 2025-03-01)
        before: Get messages before this date (ISO 8601 format, e.g., 2025-03-19)
        
    Returns:
        Path to exported file or None
    """
    logger.debug(f"Exporting channel {channel_id} with format={format}")
    
    # Use the provided token, or fall back to the one from environment  
    use_token = token or DISCORD_USER_TOKEN
    
    if not use_token:
        logger.error("Discord token is required but not provided")
        return None
        
    try:
        # Validate channel ID format (Discord IDs are typically 17-19 digits)
        channel_id_str = str(channel_id).strip()
        if not channel_id_str.isdigit() or len(channel_id_str) < 17 or len(channel_id_str) > 20:
            logger.warning(f"Channel ID appears invalid: {channel_id_str}. Discord IDs are typically 17-19 digits.")
            
        # Handle the hours parameter by converting to an ISO 8601 date string
        calc_after = after
        if hours and not after:
            from datetime import datetime, timedelta
            calc_after = (datetime.now() - timedelta(hours=hours)).isoformat()
            logger.debug(f"Converting {hours} hours to after={calc_after}")
        
        # Check if exporter is properly initialized
        if not hasattr(exporter, 'dce_cli_path') or not exporter.dce_cli_path.exists():
            logger.error(f"DiscordChatExporter CLI not found at expected path: {getattr(exporter, 'dce_cli_path', 'unknown')}")
            return None
        
        exported_file = exporter.export_channel(
            channel_id=channel_id_str,
            token=use_token,
            format=format,
            after=calc_after,
            before=before
        )
        
        if exported_file:
            logger.info(f"Successfully exported channel {channel_id} to {exported_file}")
            return exported_file
        else:
            logger.error(f"Failed to export channel {channel_id}")
            return None
    except Exception as e:
        logger.error(f"Exception in export_discord_channel: {type(e).__name__}: {e}")
        logger.error(f"Exception traceback: {traceback.format_exc()}")
        return None

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
    # Local mode status
    num_channels = len(db.channels)
    num_users = len(db.users)
    
    # Count total messages
    total_messages = sum(len(messages) for messages in db.messages.values())
    
    # Get date range
    all_timestamps = []
    for channel_messages in db.messages.values():
        for msg in channel_messages.values():
            if 'timestamp_obj' in msg:
                all_timestamps.append(msg['timestamp_obj'])
    
    date_range = ""
    if all_timestamps:
        min_date = min(all_timestamps).strftime('%Y-%m-%d')
        max_date = max(all_timestamps).strftime('%Y-%m-%d')
        date_range = f"Date range: {min_date} to {max_date}"
    
    # Count monitored channels
    channels_file = os.environ.get("DISCORD_CHANNELS_FILE", "channels.txt")
    monitored_channels = []
    channels_path = Path(os.path.dirname(os.path.abspath(__file__))) / channels_file
    if channels_path.exists():
        try:
            with open(channels_path, 'r') as f:
                for line in f:
                    channel_id = line.strip()
                    if channel_id:  # Skip empty lines
                        monitored_channels.append(channel_id)
        except Exception as e:
            logger.error(f"Error reading channels file: {e}")
    
    status = f"""
Discord MCP Server Status:
- Channels: {num_channels}
- Users: {num_users}
- Total messages: {total_messages}
- Monitored channels: {len(monitored_channels)}
- Data directory: {db.data_dir}
- Search algorithm: BM25 relevance scoring
- {date_range}
"""
    
    return status

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
    # Create data directories if they don't exist
    Path(DISCORD_DATA_DIR).mkdir(parents=True, exist_ok=True)
    Path(DISCORD_DATA_DIR, "exports").mkdir(parents=True, exist_ok=True)
    logger.info(f"Ensuring Discord data directory exists: {DISCORD_DATA_DIR}")
    
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
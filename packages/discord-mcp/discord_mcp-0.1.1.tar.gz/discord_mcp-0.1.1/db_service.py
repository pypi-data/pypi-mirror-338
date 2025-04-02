#!/usr/bin/env python3
"""
Discord Database Service

Runs a server that provides Discord data access through a REST API.
"""

import os
import json
import logging
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Query, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("db_service.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("db_service")

# Create FastAPI app
app = FastAPI(title="Discord Database Service")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration from environment variables
DISCORD_DATA_DIR = os.environ.get("DISCORD_DATA_DIR", "./discord_data")
API_KEY = os.environ.get("API_KEY", None)
API_PORT = int(os.environ.get("API_PORT", "8081"))

# Global variables
discord_messages = {}
discord_channels = {}
discord_users = {}

# API key dependency
def verify_api_key(x_api_key: Optional[str] = Header(None)):
    """Verify the API key if configured"""
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

# Pydantic models for API
class StatusResponse(BaseModel):
    status: str
    channels: int
    users: int
    messages: int
    discord_data_dir: str

class SearchRequest(BaseModel):
    query: str
    user: Optional[str] = None
    channel: Optional[str] = None
    days: Optional[int] = None
    after: Optional[str] = None
    before: Optional[str] = None
    limit: int = 30
    min_relevance: Optional[float] = 0.3

class SearchResponse(BaseModel):
    results: str

class ChannelsResponse(BaseModel):
    channels: List[Dict[str, str]]

# Helper functions
def load_discord_data():
    """Load Discord message data from the data directory"""
    global discord_messages, discord_channels, discord_users
    
    data_dir = Path(DISCORD_DATA_DIR)
    logger.info(f"Loading Discord data from {data_dir}")
    
    # Reset data
    discord_messages = {}
    discord_channels = {}
    discord_users = {}
    
    if not data_dir.exists():
        logger.warning(f"Data directory {data_dir} does not exist")
        return
    
    # Load channels data
    for channel_file in data_dir.glob("*/channel.json"):
        try:
            with open(channel_file, 'r', encoding='utf-8') as f:
                channel_data = json.load(f)
                channel_id = channel_data.get('id')
                if channel_id:
                    discord_channels[channel_id] = channel_data
        except Exception as e:
            logger.error(f"Error loading channel data from {channel_file}: {e}")
    
    # Load messages data
    for message_file in data_dir.glob("*/messages.json"):
        try:
            with open(message_file, 'r', encoding='utf-8') as f:
                messages_data = json.load(f)
                channel_id = message_file.parent.name
                
                # Process and store messages
                for message in messages_data:
                    message_id = message.get('id')
                    if message_id:
                        # Store message with channel as key for efficient lookup
                        if channel_id not in discord_messages:
                            discord_messages[channel_id] = {}
                        
                        # Add timestamp for sorting and filtering
                        if 'timestamp' in message:
                            message['timestamp_obj'] = datetime.fromisoformat(
                                message['timestamp'].replace('Z', '+00:00')
                            )
                        
                        discord_messages[channel_id][message_id] = message
                        
                        # Store user information
                        author = message.get('author', {})
                        author_id = author.get('id')
                        if author_id:
                            discord_users[author_id] = author
        except Exception as e:
            logger.error(f"Error loading messages from {message_file}: {e}")
    
    logger.info(f"Loaded {len(discord_channels)} channels, {len(discord_users)} users, and {sum(len(msgs) for msgs in discord_messages.values())} messages")

def search_messages(
    query: str, 
    user: Optional[str] = None,
    channel: Optional[str] = None,
    days: Optional[int] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    limit: int = 10
) -> List[Dict]:
    """
    Search for messages matching the query and filters
    
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
        start_date = end_date - datetime.timedelta(days=days)
    
    # Determine channel ID if channel name is provided
    channel_id = None
    if channel:
        for ch_id, ch_data in discord_channels.items():
            if channel.lower() in ch_data.get('name', '').lower() or channel == ch_id:
                channel_id = ch_id
                break
    
    # Determine user ID if username is provided
    user_id = None
    if user:
        for u_id, u_data in discord_users.items():
            if (user.lower() in u_data.get('username', '').lower() or 
                user.lower() in u_data.get('global_name', '').lower() or 
                user == u_id):
                user_id = u_id
                break
                
    # Get messages that match the criteria
    channels_to_search = [channel_id] if channel_id else discord_messages.keys()
    
    for ch_id in channels_to_search:
        if ch_id not in discord_messages:
            continue
            
        for msg_id, message in discord_messages[ch_id].items():
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
            if query and not query.lower() in message.get('content', '').lower():
                continue
            
            # Add channel information to the message
            message_copy = message.copy()
            message_copy['channel'] = discord_channels.get(ch_id, {}).get('name', ch_id)
            message_copy['channel_id'] = ch_id
            
            results.append(message_copy)
            
            # Stop if we've reached the limit
            if len(results) >= limit:
                break
    
    # Sort results by timestamp (newest first)
    results.sort(key=lambda x: x.get('timestamp_obj', datetime.min), reverse=True)
    
    return results[:limit]

def format_message(message: Dict) -> str:
    """Format a message for display"""
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

def format_messages(messages: List[Dict]) -> str:
    """Format a list of messages for display"""
    if not messages:
        return "No messages found matching the criteria."
        
    return "\n\n".join(format_message(msg) for msg in messages)

def get_monitored_channels() -> List[Dict[str, str]]:
    """Get list of monitored channels"""
    channels_file = Path(os.environ.get("DISCORD_CHANNELS_FILE", "channels.txt"))
    
    monitored_channels = []
    if channels_file.exists():
        try:
            with open(channels_file, 'r') as f:
                for line in f:
                    channel_id = line.strip()
                    if channel_id:
                        # Get channel details if available
                        channel_data = discord_channels.get(channel_id, {})
                        channel_name = channel_data.get('name', 'Unknown Channel')
                        server_name = channel_data.get('guild', {}).get('name', 'Unknown Server')
                        
                        monitored_channels.append({
                            'id': channel_id,
                            'channel_name': channel_name,
                            'server_name': server_name
                        })
        except Exception as e:
            logger.error(f"Error reading channels file: {e}")
    
    return monitored_channels

# API routes
@app.get("/api/status", response_model=StatusResponse, dependencies=[Depends(verify_api_key)])
async def get_status():
    """Get the status of the database service"""
    try:
        # Count messages, users, and channels
        total_messages = sum(len(messages) for messages in discord_messages.values())
        
        return {
            "status": "running",
            "channels": len(discord_channels),
            "users": len(discord_users),
            "messages": total_messages,
            "discord_data_dir": DISCORD_DATA_DIR
        }
    except Exception as e:
        logger.error(f"Error getting status: {e}")
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.post("/api/search", response_model=SearchResponse, dependencies=[Depends(verify_api_key)])
async def search(request: SearchRequest):
    """Search for messages using BM25 relevance scoring"""
    try:
        # This endpoint implements BM25 search similar to the main MCP server
        # For now, simply delegate to keyword search as a basic implementation
        return await keyword_search(request)
    except Exception as e:
        logger.error(f"Error in BM25 search: {e}")
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.post("/api/search/keyword", response_model=SearchResponse, dependencies=[Depends(verify_api_key)])
async def keyword_search(request: SearchRequest):
    """Search for messages using keyword matching"""
    try:
        # Parse date strings if provided
        start_date = None
        end_date = None
        
        if request.after:
            try:
                start_date = datetime.fromisoformat(request.after)
            except ValueError:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Invalid 'after' date format: {request.after}. Please use YYYY-MM-DD format."
                )
                
        if request.before:
            try:
                end_date = datetime.fromisoformat(request.before)
            except ValueError:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Invalid 'before' date format: {request.before}. Please use YYYY-MM-DD format."
                )
        
        # Search for messages
        results = search_messages(
            query=request.query,
            user=request.user,
            channel=request.channel,
            days=request.days,
            start_date=start_date,
            end_date=end_date,
            limit=request.limit
        )
        
        # Format results
        formatted_results = format_messages(results)
        
        return {"results": formatted_results}
    
    except Exception as e:
        logger.error(f"Error in keyword search: {e}")
        raise HTTPException(status_code=500, detail=f"Search error: {str(e)}")

@app.get("/api/channels", response_model=ChannelsResponse, dependencies=[Depends(verify_api_key)])
async def get_channels():
    """Get list of monitored Discord channels"""
    try:
        channels = get_monitored_channels()
        return {"channels": channels}
    except Exception as e:
        logger.error(f"Error getting channels: {e}")
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

# Initialization and startup
@app.on_event("startup")
async def startup():
    """Initialize the database service on startup"""
    # Load Discord data
    load_discord_data()
    logger.info("Database service startup complete")

@app.on_event("shutdown")
async def shutdown():
    """Clean up resources on shutdown"""
    logger.info("Database service shutting down")

def main():
    """Start the database service"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Discord Database Service")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host")
    parser.add_argument("--port", type=int, default=API_PORT, help="API port")
    parser.add_argument("--reload", action="store_true", help="Enable auto reload")
    args = parser.parse_args()
    
    # Start the API server
    logger.info(f"Starting Discord Database Service on {args.host}:{args.port}")
    
    uvicorn.run(
        "db_service:app",
        host=args.host,
        port=args.port,
        reload=args.reload
    )

if __name__ == "__main__":
    main()
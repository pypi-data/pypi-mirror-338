#!/usr/bin/env python3
"""
Discord Exporter Web UI

A web interface for managing the Discord auto exporter.
"""

import os
import json
import logging
import datetime
import re
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_file, Response

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("discord_webui.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('discord_webui')

# Add current directory to path to help with imports
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# Import our modules
from discord_auto_exporter import DiscordAutoExporter
from discord_exporter import DiscordExporter
from discord_api import DiscordAPI

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev_secret_key")

# Default paths
DEFAULT_DATA_DIR = "./discord_data"
CHANNELS_FILE = "channels.txt"

# Global state
exporter_status = {
    "is_running": False,
    "last_export_time": None,
    "export_count": 0,
    "errors": []
}

# Log settings
log_settings = {
    "max_lines": 1000,
    "refresh_interval": 5  # seconds
}

# Log files to monitor
default_log_files = [
    "discord_auto_exporter.log",
    "discord_mcp.log",
    "discord_mcp_runtime.log",
    "discord_webui.log"
]

# Auto exporter instance placeholder
auto_exporter = None

# Servers and channels cache
discord_servers = {}
discord_channels_file = "discord_servers_cache.json"

def get_config() -> Dict:
    """
    Load the configuration from environment or defaults.
    
    Returns:
        Dict: Configuration dictionary
    """
    # Default values with error handling
    try:
        export_interval_hours_str = os.environ.get("DISCORD_INTERVAL_HOURS", "6").strip()
        export_interval_hours = int(export_interval_hours_str)
        if export_interval_hours < 1:
            export_interval_hours = 6  # Default to 6 hours if invalid
    except (ValueError, TypeError):
        export_interval_hours = 6  # Default to 6 hours on parsing error
    
    try:
        export_window_hours_str = os.environ.get("DISCORD_MAX_HOURS", "24").strip()
        export_window_hours = int(export_window_hours_str)
        if export_window_hours < 1:
            export_window_hours = 24  # Default to 24 hours if invalid
    except (ValueError, TypeError):
        export_window_hours = 24  # Default to 24 hours on parsing error
    
    # Set interval unit to hours regardless of value
    export_interval_value = export_interval_hours
    export_interval_unit = "hours"
    
    # Set window unit to days, converting from hours if needed
    export_window_value = max(1, export_window_hours // 24)  # Ensure at least 1 day
    export_window_unit = "days"
    
    # For backward compatibility, still include the old fields
    config = {
        "discord_data_dir": os.environ.get("DISCORD_DATA_DIR", DEFAULT_DATA_DIR),
        "token": os.environ.get("DISCORD_USER_TOKEN", ""),
        "export_format": os.environ.get("DISCORD_EXPORT_FORMAT", "Json"),
        "max_hours_per_export": export_window_hours,
        "export_interval_hours": export_interval_hours,
        "channels_file": os.environ.get("DISCORD_CHANNELS_FILE", CHANNELS_FILE),
        "webui_port": os.environ.get("DISCORD_WEBUI_PORT", "8080"),
        "webui_host": os.environ.get("DISCORD_WEBUI_HOST", "0.0.0.0"),
        # New fields for interval and window settings
        "export_interval_value": export_interval_value,
        "export_interval_unit": os.environ.get("DISCORD_INTERVAL_UNIT", export_interval_unit),
        "export_window_value": export_window_value,
        "export_window_unit": os.environ.get("DISCORD_WINDOW_UNIT", export_window_unit),
    }
    return config

def save_config(config: Dict) -> None:
    """
    Save configuration values to environment file.
    
    Args:
        config: Configuration dictionary to save
    """
    env_file = Path(script_dir) / ".env"
    
    # Keep existing variables
    env_vars = {}
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value
    
    # Convert interval and window values to hours for backward compatibility
    if "export_interval_value" in config and "export_interval_unit" in config:
        interval_value = int(config["export_interval_value"])
        interval_unit = config["export_interval_unit"]
        interval_hours = interval_value * 24 if interval_unit == "days" else interval_value
        
        # Save both the new format and the old format for backward compatibility
        env_vars["DISCORD_INTERVAL_HOURS"] = str(interval_hours)
        env_vars["DISCORD_INTERVAL_UNIT"] = interval_unit
        env_vars["DISCORD_INTERVAL_VALUE"] = str(interval_value)
    elif "export_interval_hours" in config:
        # Fallback to the old format if new format not available
        env_vars["DISCORD_INTERVAL_HOURS"] = str(config["export_interval_hours"])
    
    if "export_window_value" in config and "export_window_unit" in config:
        window_value = int(config["export_window_value"])
        window_unit = config["export_window_unit"]
        window_hours = window_value * 24 if window_unit == "days" else window_value
        
        # Save both the new format and the old format for backward compatibility
        env_vars["DISCORD_MAX_HOURS"] = str(window_hours)
        env_vars["DISCORD_WINDOW_UNIT"] = window_unit
        env_vars["DISCORD_WINDOW_VALUE"] = str(window_value)
    elif "max_hours_per_export" in config:
        # Fallback to the old format if new format not available
        env_vars["DISCORD_MAX_HOURS"] = str(config["max_hours_per_export"])
    
    # Update with other values
    env_vars["DISCORD_DATA_DIR"] = config["discord_data_dir"]
    env_vars["DISCORD_USER_TOKEN"] = config["token"]
    env_vars["DISCORD_EXPORT_FORMAT"] = config["export_format"]
    env_vars["DISCORD_CHANNELS_FILE"] = config["channels_file"]
    
    # Save Web UI configuration if provided
    if "webui_port" in config:
        env_vars["DISCORD_WEBUI_PORT"] = str(config["webui_port"])
    if "webui_host" in config:
        env_vars["DISCORD_WEBUI_HOST"] = config["webui_host"]
    
    # Write back to file
    with open(env_file, 'w') as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")
    
    logger.info("Configuration saved to .env file")

def get_channel_list() -> List[str]:
    """
    Get the list of channel IDs from the channels file.
    
    Returns:
        List[str]: List of channel IDs
    """
    config = get_config()
    channels_file = Path(config["channels_file"])
    
    if not channels_file.exists():
        return []
        
    with open(channels_file, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def save_channel_list(channels: List[str]) -> None:
    """
    Save the list of channel IDs to the channels file.
    
    Args:
        channels: List of channel IDs to save
    """
    config = get_config()
    channels_file = Path(config["channels_file"])
    
    with open(channels_file, 'w') as f:
        for channel in channels:
            f.write(f"{channel}\n")
    
    logger.info(f"Saved {len(channels)} channel IDs to {channels_file}")

def load_discord_servers() -> Dict[str, Any]:
    """
    Load the cached Discord servers and channels from the JSON file.
    
    Returns:
        Dict: Mapping of server names to their data, alphabetically sorted
    """
    global discord_servers
    
    cache_path = Path(script_dir) / discord_channels_file
    
    if cache_path.exists():
        try:
            with open(cache_path, 'r') as f:
                unsorted_servers = json.load(f)
            
            # Create a new sorted dictionary based on server names (case-insensitive)
            discord_servers = {}
            for server_name in sorted(unsorted_servers.keys(), key=str.lower):
                discord_servers[server_name] = unsorted_servers[server_name]
                
            logger.info(f"Loaded and sorted {len(discord_servers)} servers from cache")
        except Exception as e:
            logger.error(f"Error loading Discord servers cache: {e}")
            discord_servers = {}
            
    return discord_servers

def save_discord_servers(servers: Dict[str, Any]) -> None:
    """
    Save the Discord servers and channels to the JSON cache file.
    Ensures servers are stored in alphabetical order.
    
    Args:
        servers: Dictionary of server data to save
    """
    global discord_servers
    
    # Create a sorted OrderedDict to maintain alphabetical order
    from collections import OrderedDict
    sorted_servers = OrderedDict()
    for server_name in sorted(servers.keys(), key=str.lower):
        sorted_servers[server_name] = servers[server_name]
    
    # Update the global variable with the sorted dictionary
    discord_servers = sorted_servers
    
    cache_path = Path(script_dir) / discord_channels_file
    
    try:
        with open(cache_path, 'w') as f:
            json.dump(sorted_servers, f, indent=2)
        logger.info(f"Saved {len(sorted_servers)} servers to cache in alphabetical order")
    except Exception as e:
        logger.error(f"Error saving Discord servers cache: {e}")

def fetch_discord_servers(token: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetch the Discord servers and channels using the Discord API.
    
    Args:
        token: Discord authentication token (optional if set in environment)
        
    Returns:
        Dict: Mapping of server names to their data
    """
    config = get_config()
    
    # Use the provided token, or fall back to the one from environment
    use_token = token or config["token"]
    
    if not use_token:
        logger.error("Discord token is required but not provided")
        return {}
    
    try:
        # Create Discord API instance
        discord_api = DiscordAPI(use_token)
        
        # Get hierarchical structure of guilds and channels
        servers = discord_api.get_channels_hierarchical()
        
        # Sort servers alphabetically
        sorted_servers = {}
        for server_name in sorted(servers.keys(), key=str.lower):
            sorted_servers[server_name] = servers[server_name]
        
        # Save to cache
        save_discord_servers(sorted_servers)
        
        return sorted_servers
    
    except Exception as e:
        logger.error(f"Error fetching Discord servers: {e}")
        return {}

def delete_channel_data(channel_id: str) -> Dict:
    """
    Delete all data related to a specific channel, including:
    - Export files
    - Export timestamps
    
    Args:
        channel_id: The ID of the channel to delete data for
        
    Returns:
        Dict: Result of the operation
    """
    config = get_config()
    data_dir = Path(config["discord_data_dir"])
    exports_dir = data_dir / "exports"
    
    deleted_files = []
    
    try:
        # Delete exported JSON files for this channel
        if exports_dir.exists():
            # Look for files matching the channel ID pattern
            channel_files = list(exports_dir.glob(f"*{channel_id}*.json"))
            for file_path in channel_files:
                try:
                    file_path.unlink()
                    deleted_files.append(file_path.name)
                    logger.info(f"Deleted export file: {file_path}")
                except Exception as file_err:
                    logger.error(f"Error deleting file {file_path}: {file_err}")
        
        # BM25 search doesn't require database cleanup
        logger.info(f"No cleanup needed for channel {channel_id} as BM25 search is used")
        
        # Remove from timestamps
        timestamps_file = data_dir / "last_export_times.txt"
        timestamp_updated = False
        
        if timestamps_file.exists():
            last_exports = {}
            
            # Read current timestamps
            with open(timestamps_file, 'r') as f:
                for line in f:
                    if ":" in line:
                        ch_id, timestamp_str = line.strip().split(":", 1)
                        if ch_id != channel_id:  # Skip the channel we're deleting
                            last_exports[ch_id] = timestamp_str
            
            # Save updated timestamps without the deleted channel
            with open(timestamps_file, 'w') as f:
                for ch_id, timestamp in last_exports.items():
                    f.write(f"{ch_id}:{timestamp}\n")
            
            timestamp_updated = True
            logger.info(f"Removed channel {channel_id} from export timestamps")
        
        return {
            "success": True,
            "message": f"Channel data deleted successfully",
            "details": {
                "deleted_files": deleted_files,
                "timestamp_updated": timestamp_updated
            }
        }
        
    except Exception as e:
        logger.error(f"Error deleting channel data: {e}")
        logger.error(traceback.format_exc())
        return {
            "success": False,
            "message": f"Error deleting channel data: {str(e)}"
        }

def save_export_status(last_exports: Dict[str, str]) -> None:
    """
    Save the export status timestamps to file.
    
    Args:
        last_exports: Dictionary of channel_id to timestamps
    """
    config = get_config()
    data_dir = Path(config["discord_data_dir"])
    timestamps_file = data_dir / "last_export_times.txt"
    
    try:
        # Convert pretty-formatted timestamps back to ISO format if needed
        iso_timestamps = {}
        for channel_id, timestamp in last_exports.items():
            try:
                # Check if timestamp is already in ISO format
                datetime.datetime.fromisoformat(timestamp)
                iso_timestamps[channel_id] = timestamp
            except ValueError:
                try:
                    # Try to parse from the pretty format
                    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                    iso_timestamps[channel_id] = dt.isoformat()
                except ValueError:
                    # If it fails, just keep the original
                    iso_timestamps[channel_id] = timestamp
        
        # Write the timestamps to file
        with open(timestamps_file, 'w') as f:
            for channel_id, timestamp in iso_timestamps.items():
                f.write(f"{channel_id}:{timestamp}\n")
        
        logger.info(f"Saved export timestamps for {len(last_exports)} channels")
    except Exception as e:
        logger.error(f"Error saving export timestamps: {e}")

def get_export_status() -> Dict:
    """
    Get the status of the exporter and exports.
    
    Returns:
        Dict: Status information
    """
    config = get_config()
    data_dir = Path(config["discord_data_dir"])
    exports_dir = data_dir / "exports"
    timestamps_file = data_dir / "last_export_times.txt"
    
    # Get exported files
    exported_files = []
    if exports_dir.exists():
        files = list(exports_dir.glob("*.json"))
        exported_files = [
            {
                "name": f.name,
                "size": f.stat().st_size // 1024,  # Size in KB
                "modified": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            }
            for f in files
        ]
        # Sort by modification time, newest first
        exported_files.sort(key=lambda x: x["modified"], reverse=True)
    
    # Get last export times
    last_exports = {}
    if timestamps_file.exists():
        with open(timestamps_file, 'r') as f:
            for line in f:
                if ":" in line:
                    channel_id, timestamp_str = line.strip().split(":", 1)
                    try:
                        last_exports[channel_id] = datetime.datetime.fromisoformat(timestamp_str).strftime("%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        last_exports[channel_id] = "Invalid timestamp"
    
    # BM25 search system
    search_status = "BM25 search active"
    
    return {
        "is_running": exporter_status["is_running"],
        "last_export_time": exporter_status["last_export_time"],
        "export_count": exporter_status["export_count"],
        "errors": exporter_status["errors"],
        "exported_files": exported_files,
        "last_exports": last_exports,
        "search_status": search_status
    }

def get_log_files() -> List[Dict]:
    """
    Get a list of available log files.
    
    Returns:
        List[Dict]: List of log files with name and path
    """
    script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    log_files = []
    
    # Look for log files in the current directory
    for log_file in default_log_files:
        file_path = script_dir / log_file
        if file_path.exists():
            log_files.append({
                "name": log_file,
                "path": str(file_path)
            })
    
    # Look for other log files
    for file in script_dir.glob("*.log"):
        if file.name not in default_log_files:
            log_files.append({
                "name": file.name,
                "path": str(file)
            })
    
    return log_files

def parse_log_line(line: str) -> Tuple[str, str, str]:
    """
    Parse a log line to extract timestamp, level, and message.
    
    Args:
        line: A single line from a log file
        
    Returns:
        Tuple of (timestamp, level, message)
    """
    # Match standard log format: YYYY-MM-DD HH:MM:SS,mmm - name - LEVEL - message
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (\w+) - (\w+) - (.+)'
    match = re.match(log_pattern, line)
    
    if match:
        timestamp = match.group(1)
        # name = match.group(2)  # We don't use this but could if needed
        level = match.group(3)
        message = match.group(4)
        return timestamp, level, message
    
    # Simple fallback for non-standard lines
    return "", "INFO", line.strip()

def read_log_file(file_path: str, max_lines: int = 1000) -> List[Dict]:
    """
    Read a log file and parse its contents.
    
    Args:
        file_path: Path to the log file
        max_lines: Maximum number of lines to read from the end of the file
        
    Returns:
        List[Dict]: List of log entries with timestamp, level, and message
    """
    log_entries = []
    
    try:
        with open(file_path, 'r') as f:
            # Read the file and get the last max_lines lines
            lines = f.readlines()
            lines = lines[-max_lines:] if len(lines) > max_lines else lines
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                timestamp, level, message = parse_log_line(line)
                log_entries.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message
                })
        
        return log_entries
    except Exception as e:
        logger.error(f"Error reading log file {file_path}: {e}")
        return [{"timestamp": "", "level": "ERROR", "message": f"Error reading log file: {str(e)}"}]

def run_channel_export(channel_id: str) -> Dict:
    """
    Run an export for a single channel.
    
    Args:
        channel_id: The ID of the channel to export
        
    Returns:
        Dict: Result of the export operation
    """
    global exporter_status
    
    config = get_config()
    
    # Check if already running
    if exporter_status["is_running"]:
        return {"success": False, "message": "An export is already running"}
    
    # Verify channel ID is in the monitored channels
    channels = get_channel_list()
    if channel_id not in channels:
        return {"success": False, "message": "Channel ID is not in the list of monitored channels"}
    
    # Create exporter instances
    try:
        # Set status to running
        exporter_status["is_running"] = True
        
        # Calculate window hours from the new settings
        if "export_window_value" in config and "export_window_unit" in config:
            window_value = int(config["export_window_value"])
            window_unit = config["export_window_unit"]
            window_hours = window_value * 24 if window_unit == "days" else window_value
        else:
            window_hours = config["max_hours_per_export"]
        
        # Get last export time
        timestamps_file = Path(config["discord_data_dir"]) / "last_export_times.txt"
        last_exports = {}
        
        if timestamps_file.exists():
            with open(timestamps_file, 'r') as f:
                for line in f:
                    if ":" in line:
                        ch_id, timestamp_str = line.strip().split(":", 1)
                        try:
                            last_exports[ch_id] = datetime.datetime.fromisoformat(timestamp_str)
                        except ValueError:
                            pass
        
        # Calculate export time range
        current_time = datetime.datetime.now()
        if channel_id in last_exports:
            after_time = last_exports[channel_id]
        else:
            # First export gets last N hours
            after_time = current_time - datetime.timedelta(hours=config["max_hours_per_export"])
        
        # Format as ISO 8601
        after_str = after_time.isoformat()
        
        logger.info(f"Exporting single channel {channel_id} from {after_str} to now")
        
        # Create a direct exporter instance for the main export
        direct_exporter = DiscordExporter(
            output_dir=os.path.join(config["discord_data_dir"], "exports"),
            token=config["token"]
        )
        
        # Perform the export
        exported_file = direct_exporter.export_channel(
            channel_id=channel_id,
            token=config["token"],
            format=config["export_format"],
            after=after_str
        )
        
        # Update last export time
        last_exports[channel_id] = current_time
        
        # Save updated timestamps
        with open(timestamps_file, 'w') as f:
            for ch_id, timestamp in last_exports.items():
                f.write(f"{ch_id}:{timestamp.isoformat()}\n")
        
        # Create auto exporter to handle message cleanup
        auto_exporter = DiscordAutoExporter(
            discord_data_dir=config["discord_data_dir"],
            token=config["token"],
            export_format=config["export_format"],
            export_window_hours=window_hours
        )
        
        # Delete old messages that fall outside the export window
        try:
            auto_exporter._delete_old_messages(channel_id, current_time)
            logger.info(f"Cleaned up old messages for channel {channel_id}")
        except Exception as clean_err:
            logger.error(f"Error cleaning up old messages: {clean_err}")
        
        # BM25 search doesn't require any additional update step
        logger.info("BM25 search activated with new data automatically")
        
        # Update status
        exporter_status["is_running"] = False
        exporter_status["last_export_time"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
        exporter_status["export_count"] += 1
        
        # Get updated export status with fresh timestamps
        updated_status = get_export_status()
        
        if exported_file:
            return {
                "success": True,
                "message": f"Successfully exported channel {channel_id}",
                "last_exports": updated_status["last_exports"]
            }
        else:
            return {
                "success": False,
                "message": f"No new messages found for channel {channel_id} or export failed",
                "last_exports": updated_status["last_exports"]
            }
            
    except Exception as e:
        logger.error(f"Error exporting channel {channel_id}: {e}")
        logger.error(traceback.format_exc())
        exporter_status["is_running"] = False
        exporter_status["errors"].append(str(e))
        return {"success": False, "message": f"Error: {str(e)}"}

def run_manual_export() -> Dict:
    """
    Run a manual export of all configured channels.
    
    Returns:
        Dict: Result of the export operation
    """
    global exporter_status
    
    config = get_config()
    
    # Check if already running
    if exporter_status["is_running"]:
        return {"success": False, "message": "An export is already running"}
    
    # Create exporter instance
    try:
        # Calculate window hours from the new settings
        if "export_window_value" in config and "export_window_unit" in config:
            window_value = int(config["export_window_value"])
            window_unit = config["export_window_unit"]
            window_hours = window_value * 24 if window_unit == "days" else window_value
        else:
            window_hours = config["max_hours_per_export"]
        
        exporter = DiscordAutoExporter(
            discord_data_dir=config["discord_data_dir"],
            token=config["token"],
            export_format=config["export_format"],
            channels_file=config["channels_file"],
            max_hours_per_export=config["max_hours_per_export"],
            export_interval_hours=config["export_interval_hours"],
            export_window_hours=window_hours,
        )
        
        # Set status to running
        exporter_status["is_running"] = True
        exporter_status["last_export_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Run export
        success = exporter.run_scheduled_export()
        
        # Update status
        exporter_status["is_running"] = False
        if success:
            exporter_status["export_count"] += 1
            
            # Get updated export status with fresh timestamps
            updated_status = get_export_status()
            
            return {
                "success": True, 
                "message": "Export completed successfully",
                "last_exports": updated_status["last_exports"]
            }
        else:
            exporter_status["errors"].append("Export failed")
            return {"success": False, "message": "Export failed. Check logs for details."}
            
    except Exception as e:
        logger.error(f"Error running manual export: {e}")
        exporter_status["is_running"] = False
        exporter_status["errors"].append(str(e))
        return {"success": False, "message": f"Error: {str(e)}"}

@app.route('/')
def index():
    """Main dashboard page"""
    config = get_config()
    channels = get_channel_list()
    status = get_export_status()
    log_files = get_log_files()
    
    # Get channel details from Discord API if token is available
    channel_details = []
    if channels and config["token"]:
        # Load servers and channels from cache first
        servers = load_discord_servers()
        
        # If servers cache is empty, try to fetch only the basic server list without channels
        if not servers:
            try:
                discord_api = DiscordAPI(config["token"])
                servers = discord_api.get_user_guilds_basic()
                save_discord_servers(servers)
            except Exception as e:
                logger.error(f"Failed to fetch Discord servers: {e}")
        
        # Create a map of channel_id -> (server_name, channel_name)
        channel_info = {}
        
        # First collect what server/channel info we already have in the cache
        for server_name, server_data in servers.items():
            if server_data.get('channels_loaded', False):
                for channel in server_data.get('channels', []):
                    channel_info[channel['id']] = {
                        'server_name': server_name,
                        'channel_name': channel['name']
                    }
        
        # Keep track of which servers we've checked
        checked_servers = set()
        
        # For any channels not found in cache, try to find their servers and fetch specific channel details
        missing_channels = [ch_id for ch_id in channels if ch_id not in channel_info]
        if missing_channels and servers:
            try:
                discord_api = DiscordAPI(config["token"])
                
                # For each missing channel, search for it in the servers
                for channel_id in missing_channels:
                    # Get partial channel info directly if possible
                    try:
                        # This is a hypothetical method - we'd need to implement this in discord_api.py
                        # to get channel info directly by ID rather than listing all channels in a guild
                        channel_data = discord_api.get_channel_info(channel_id)
                        if channel_data and 'guild_id' in channel_data:
                            # Find the server name
                            guild_id = channel_data['guild_id']
                            server_name = "Unknown Server"
                            for name, data in servers.items():
                                if data.get('id') == guild_id:
                                    server_name = name
                                    break
                                    
                            channel_info[channel_id] = {
                                'server_name': server_name,
                                'channel_name': channel_data.get('name', 'Unknown Channel')
                            }
                            continue
                    except Exception:
                        # If direct channel lookup fails, fall back to searching servers
                        pass
                        
                    # Try each server that we haven't checked yet
                    for server_name, server_data in servers.items():
                        server_id = server_data.get('id')
                        if not server_id or server_id in checked_servers:
                            continue
                            
                        # Only check each server once
                        checked_servers.add(server_id)
                        
                        # Skip servers that already have channels loaded
                        if server_data.get('channels_loaded', False):
                            continue
                        
                        # Load channels for this server
                        try:
                            server_channels = discord_api.get_guild_channels_detail(server_id)
                            server_data['channels'] = server_channels
                            server_data['channels_loaded'] = True
                            
                            # Save the updated server data
                            save_discord_servers(servers)
                            
                            # Check if any of our missing channels are in this server
                            for channel in server_channels:
                                if channel['id'] in missing_channels:
                                    channel_info[channel['id']] = {
                                        'server_name': server_name,
                                        'channel_name': channel['name']
                                    }
                        except Exception as e:
                            logger.error(f"Failed to fetch channels for server {server_name}: {e}")
                            
                            # If we hit a rate limit, stop trying more servers for now
                            if "429" in str(e):
                                break
            except Exception as e:
                logger.error(f"Error processing channels: {e}")
        
        # Create detailed channel list
        for channel_id in channels:
            detail = {
                'id': channel_id,
                'server_name': channel_info.get(channel_id, {}).get('server_name', 'Unknown Server'),
                'channel_name': channel_info.get(channel_id, {}).get('channel_name', 'Unknown Channel'),
                'last_export': status.get('last_exports', {}).get(channel_id, 'Never attempted')
            }
            channel_details.append(detail)
    
    return render_template(
        'index.html',
        config=config,
        channels=channels,
        channel_details=channel_details,
        status=status,
        log_files=log_files
    )

@app.route('/config', methods=['GET', 'POST'])
def config_page():
    """Configuration page"""
    if request.method == 'POST':
        # Get the export interval and window settings from the form
        export_interval_value = int(request.form.get('export_interval_value', '6'))
        export_interval_unit = request.form.get('export_interval_unit', 'hours')
        export_window_value = int(request.form.get('export_window_value', '24'))
        export_window_unit = request.form.get('export_window_unit', 'hours')
        
        # Update configuration
        config = {
            "discord_data_dir": request.form.get('discord_data_dir', DEFAULT_DATA_DIR),
            "token": request.form.get('token', ''),
            "export_format": request.form.get('export_format', 'Json'),
            "channels_file": request.form.get('channels_file', CHANNELS_FILE),
            "webui_port": request.form.get('webui_port', '8080'),
            "webui_host": request.form.get('webui_host', '0.0.0.0'),
            # New settings
            "export_interval_value": export_interval_value,
            "export_interval_unit": export_interval_unit,
            "export_window_value": export_window_value,
            "export_window_unit": export_window_unit,
        }
        
        # Save to .env file
        save_config(config)
        
        flash('Configuration has been updated successfully', 'success')
        return redirect(url_for('index'))
    
    # GET request - show form
    config = get_config()
    return render_template('config.html', config=config)

@app.route('/channels', methods=['GET', 'POST'])
def channels_page():
    """Channel management page"""
    if request.method == 'POST':
        # Get selected channels from checkboxes
        selected_channels = request.form.getlist('selected_channels')
        
        # Add any manually entered channels
        manual_channels = [ch.strip() for ch in request.form.getlist('manual_channels') if ch.strip()]
        
        # Combine both sets of channels
        all_channels = selected_channels + manual_channels
        
        # Save to file
        save_channel_list(all_channels)
        
        flash('Channel list has been updated successfully', 'success')
        return redirect(url_for('channels_page'))
    
    # GET request - show form
    config = get_config()
    selected_channels = get_channel_list()
    
    # Load servers and channels from cache or fetch if needed
    servers = load_discord_servers()
    if not servers and config["token"]:
        servers = fetch_discord_servers(config["token"])
    
    # Prepare manual channels (those not found in the server list)
    manual_channels = []
    if selected_channels:
        # Find all channel IDs in the server list
        server_channel_ids = []
        for server_data in servers.values():
            for channel in server_data.get('channels', []):
                server_channel_ids.append(channel['id'])
        
        # Any selected channels not in server list are manual entries
        manual_channels = [ch for ch in selected_channels if ch not in server_channel_ids]
    
    return render_template(
        'channels.html', 
        servers=servers, 
        selected_channels=selected_channels,
        manual_channels=manual_channels
    )

@app.route('/exports')
def exports_page():
    """Export history page"""
    status = get_export_status()
    return render_template('exports.html', status=status)

@app.route('/logs')
def logs_page():
    """Logs monitoring page"""
    log_files = get_log_files()
    current_log = request.args.get('file', default_log_files[0] if default_log_files else '')
    
    # Find the selected log file
    selected_log = None
    for log_file in log_files:
        if log_file['name'] == current_log:
            selected_log = log_file
            break
    
    # If no log file is selected, use the first one
    if not selected_log and log_files:
        selected_log = log_files[0]
        current_log = selected_log['name']
    
    # Read logs from the selected file
    logs = []
    if selected_log:
        logs = read_log_file(selected_log['path'], log_settings['max_lines'])
    
    return render_template(
        'logs.html',
        logs=logs,
        log_files=log_files,
        current_log=current_log,
        max_lines=log_settings['max_lines'],
        refresh_interval=log_settings['refresh_interval'],
        last_updated=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

@app.route('/api/export', methods=['POST'])
def api_export():
    """API endpoint to trigger a manual export of all channels"""
    result = run_manual_export()
    return jsonify(result)
    
@app.route('/api/export-channel', methods=['POST'])
def api_export_channel():
    """API endpoint to export a single channel"""
    data = request.json
    channel_id = data.get('channel_id')
    
    if not channel_id:
        return jsonify({"success": False, "message": "Channel ID is required"})
    
    result = run_channel_export(channel_id)
    return jsonify(result)
    
@app.route('/api/clear-database', methods=['POST'])
def api_clear_database():
    """API endpoint to clear export timestamps and exported files"""
    config = get_config()
    
    try:
        # BM25 search doesn't need any database clearing
        logger.info("Using BM25 search which doesn't require database clearing")
        
        # Clear the export timestamps file
        timestamps_file = Path(config["discord_data_dir"]) / "last_export_times.txt"
        if timestamps_file.exists():
            try:
                # Empty file (preferred as it maintains the file's existence)
                with open(timestamps_file, 'w') as f:
                    pass  # Write nothing, effectively emptying the file
                
                logger.info(f"Cleared export timestamps file at {timestamps_file}")
            except Exception as ts_err:
                logger.error(f"Error clearing timestamps file: {ts_err}")
        
        # Delete all exported files
        exports_dir = Path(config["discord_data_dir"]) / "exports"
        if exports_dir.exists():
            try:
                # Count files before deletion
                export_files = list(exports_dir.glob("*.json"))
                file_count = len(export_files)
                
                # Delete each export file
                for file_path in export_files:
                    try:
                        file_path.unlink()
                    except Exception as file_err:
                        logger.error(f"Error deleting file {file_path}: {file_err}")
                
                logger.info(f"Deleted {file_count} exported files from {exports_dir}")
            except Exception as ex_err:
                logger.error(f"Error clearing exports directory: {ex_err}")
        
        # Clear any other cached data if present (e.g., processed messages)
        processed_dir = Path(config["discord_data_dir"]) / "processed"
        if processed_dir.exists():
            try:
                processed_files = list(processed_dir.glob("*.json"))
                for file_path in processed_files:
                    try:
                        file_path.unlink()
                    except Exception as proc_err:
                        logger.error(f"Error deleting processed file {file_path}: {proc_err}")
                
                logger.info(f"Cleared processed message files in {processed_dir}")
            except Exception as proc_dir_err:
                logger.error(f"Error clearing processed directory: {proc_dir_err}")
        
        logger.info("Message cache, export timestamps, and exported files cleared successfully")
        return jsonify({
            "success": True,
            "message": "Message cache, export history, and all exported files cleared successfully"
        })
        
    except Exception as e:
        logger.error(f"Error clearing message cache and exports: {e}")
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        })

@app.route('/api/status')
def api_status():
    """API endpoint to get the current status"""
    status = get_export_status()
    return jsonify(status)

@app.route('/api/channels', methods=['GET', 'POST'])
def api_channels():
    """API endpoint to get or update channel list"""
    if request.method == 'POST':
        data = request.json
        if 'channels' in data:
            save_channel_list(data['channels'])
            return jsonify({"success": True})
        return jsonify({"success": False, "message": "No channels provided"})
    
    # GET request
    channels = get_channel_list()
    return jsonify({"channels": channels})

@app.route('/api/delete-channel-data', methods=['POST'])
def api_delete_channel_data():
    """API endpoint to delete the data for a single channel"""
    try:
        data = request.json
        channel_id = data.get('channel_id')
        
        if not channel_id:
            return jsonify({"success": False, "message": "Channel ID is required"})
        
        # Convert to string to ensure consistency
        str_channel_id = str(channel_id)
        
        # Delete the channel data
        result = delete_channel_data(str_channel_id)
        
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error deleting channel data: {e}")
        logger.error(traceback.format_exc())
        return jsonify({"success": False, "message": str(e)})

@app.route('/api/remove-channel', methods=['POST'])
def api_remove_channel():
    """API endpoint to remove a single channel from monitoring and delete its data"""
    try:
        data = request.json
        channel_id = data.get('channel_id')
        delete_data = data.get('delete_data', True)  # Default to true - delete data when removing channel
        
        if not channel_id:
            return jsonify({"success": False, "message": "Channel ID is required"})
        
        # Get current channel list
        current_channels = get_channel_list()
        
        # Try both string and integer versions of channel_id
        str_channel_id = str(channel_id)
        
        # Check if channel exists in the list
        if str_channel_id not in current_channels:
            return jsonify({"success": False, "message": "Channel not found in monitoring list"})
        
        # Remove the channel
        current_channels.remove(str_channel_id)
        
        # Save the updated list
        save_channel_list(current_channels)
        
        # Update export status to ensure UI is consistent
        status = get_export_status() 
        
        # If the channel has an export timestamp, remove it
        if 'last_exports' in status:
            last_exports = status['last_exports']
            if str_channel_id in last_exports:
                del last_exports[str_channel_id]
                save_export_status(last_exports)
        
        # Delete channel data if requested
        if delete_data:
            delete_channel_data(str_channel_id)
        
        return jsonify({"success": True, "message": "Channel removed successfully"})
    except Exception as e:
        logger.error(f"Error removing channel: {e}")
        logger.error(traceback.format_exc())
        return jsonify({"success": False, "message": str(e)})

@app.route('/api/refresh-channels', methods=['GET'])
def api_refresh_channels():
    """API endpoint to refresh the server and channel list"""
    config = get_config()
    
    if not config["token"]:
        return jsonify({
            "success": False, 
            "message": "Discord token is required. Please set it in the configuration."
        })
    
    try:
        # Fetch Discord servers and channels
        servers = fetch_discord_servers(config["token"])
        
        if not servers:
            return jsonify({
                "success": False, 
                "message": "No servers found. Please check your Discord token."
            })
        
        return jsonify({
            "success": True,
            "server_count": len(servers)
        })
        
    except Exception as e:
        logger.error(f"Error refreshing Discord servers: {e}")
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        })

@app.route('/api/guild-channels', methods=['GET'])
def api_guild_channels():
    """API endpoint to get channels for a specific guild/server"""
    guild_id = request.args.get('guild_id')
    
    if not guild_id:
        return jsonify({
            "success": False,
            "message": "Guild ID is required"
        })
        
    config = get_config()
    
    if not config["token"]:
        return jsonify({
            "success": False,
            "message": "Discord token is required. Please set it in the configuration."
        })
    
    try:
        # Create Discord API instance
        discord_api = DiscordAPI(config["token"])
        
        # Get channels for this guild
        channels = discord_api.get_guild_channels_detail(guild_id)
        
        # Update the channel data in the server cache
        servers = load_discord_servers()
        
        # Find the server by guild_id
        for server_name, server_data in servers.items():
            if server_data['id'] == guild_id:
                server_data['channels'] = channels
                server_data['channels_loaded'] = True
                break
        
        # Save updated servers to cache
        save_discord_servers(servers)
        
        # Get currently selected channels for the checkbox state
        selected_channels = get_channel_list()
        
        return jsonify({
            "success": True,
            "channels": channels,
            "selected_channels": selected_channels
        })
        
    except Exception as e:
        logger.error(f"Error fetching guild channels: {e}")
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        })

@app.route('/api/config', methods=['GET', 'POST'])
def api_config():
    """API endpoint to get or update configuration"""
    if request.method == 'POST':
        data = request.json
        if data:
            # Update configuration with provided values
            config = get_config()
            for key, value in data.items():
                if key in config:
                    config[key] = value
            
            # Save to .env file
            save_config(config)
            return jsonify({"success": True})
        return jsonify({"success": False, "message": "No configuration provided"})
    
    # GET request
    config = get_config()
    # Don't expose token in API response
    safe_config = config.copy()
    safe_config["token"] = "****" if safe_config["token"] else ""
    return jsonify(safe_config)

@app.route('/api/logs')
def api_logs():
    """API endpoint to get logs"""
    log_file_name = request.args.get('file', default_log_files[0] if default_log_files else '')
    max_lines = int(request.args.get('lines', log_settings['max_lines']))
    
    # Find the log file
    log_file_path = None
    log_files = get_log_files()
    for log_file in log_files:
        if log_file['name'] == log_file_name:
            log_file_path = log_file['path']
            break
    
    if not log_file_path:
        return jsonify({
            "logs": [{"timestamp": "", "level": "ERROR", "message": f"Log file '{log_file_name}' not found"}]
        })
    
    # Read logs from the file
    logs = read_log_file(log_file_path, max_lines)
    
    return jsonify({
        "logs": logs,
        "file": log_file_name,
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/api/logs/download')
def api_logs_download():
    """API endpoint to download a log file"""
    log_file_name = request.args.get('file', default_log_files[0] if default_log_files else '')
    
    # Find the log file
    log_file_path = None
    log_files = get_log_files()
    for log_file in log_files:
        if log_file['name'] == log_file_name:
            log_file_path = log_file['path']
            break
    
    if not log_file_path:
        return jsonify({"error": f"Log file '{log_file_name}' not found"}), 404
    
    # Return the file for download
    return send_file(
        log_file_path,
        as_attachment=True,
        download_name=log_file_name,
        mimetype='text/plain'
    )

@app.route('/api/logs/settings', methods=['POST'])
def api_logs_settings():
    """API endpoint to update log settings"""
    global log_settings
    
    data = request.json
    if data:
        # Update log settings
        if 'max_lines' in data:
            try:
                max_lines = int(data['max_lines'])
                if 10 <= max_lines <= 5000:
                    log_settings['max_lines'] = max_lines
            except ValueError:
                pass
        
        if 'refresh_interval' in data:
            try:
                refresh_interval = int(data['refresh_interval'])
                if 1 <= refresh_interval <= 60:
                    log_settings['refresh_interval'] = refresh_interval
            except ValueError:
                pass
                
        return jsonify({"success": True, "settings": log_settings})
    
    return jsonify({"success": False, "message": "No settings provided"})

# Note: Remote API endpoints have been removed
# The webUI now only runs on the same machine as the database

if __name__ == "__main__":
    # Create data directories if they don't exist
    config = get_config()
    Path(config["discord_data_dir"]).mkdir(parents=True, exist_ok=True)
    Path(config["discord_data_dir"], "exports").mkdir(parents=True, exist_ok=True)
    # Vector DB directory no longer needed with BM25 search
    
    # Create static and templates directories if they don't exist
    templates_dir = Path(script_dir) / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    
    static_dir = Path(script_dir) / "static"
    static_dir.mkdir(parents=True, exist_ok=True)
    
    # Load Discord servers from cache
    load_discord_servers()
    
    # If token is available and servers cache is empty, try to fetch them
    if config["token"] and not discord_servers:
        logger.info("Attempting to fetch Discord servers on startup...")
        try:
            fetch_discord_servers(config["token"])
        except Exception as e:
            logger.error(f"Failed to fetch Discord servers on startup: {e}")
    
    # Read port from environment variable or use default 8080
    # (to avoid conflict with macOS AirPlay on port 5000)
    try:
        port_str = os.environ.get("DISCORD_WEBUI_PORT", "8080").strip()
        port = int(port_str)
        if port < 1024 or port > 65535:
            logger.warning(f"Port {port} is out of valid range, using default 8080")
            port = 8080
    except (ValueError, TypeError):
        logger.warning(f"Invalid port setting, using default: 8080")
        port = 8080
    
    # Get host binding (0.0.0.0 for all interfaces, 127.0.0.1 for localhost only)
    # Make sure to strip any whitespace or unwanted characters
    try:
        host = os.environ.get("DISCORD_WEBUI_HOST", "0.0.0.0").strip()
        
        # Validate the host (make sure it's just an IP or hostname)
        if not re.match(r'^[\w\.\-]+$', host):
            logger.warning(f"Invalid host binding '{host}', using 0.0.0.0 instead")
            host = "0.0.0.0"
    except Exception as e:
        logger.warning(f"Error parsing host: {e}, using default: 0.0.0.0")
        host = "0.0.0.0"
    
    logger.info(f"Starting Discord Exporter Web UI on {host}:{port}")
    app.run(host=host, port=port, debug=False)

def main_cli():
    """Main entry point for the CLI."""
    # Load Discord servers info on startup
    load_discord_servers()
    
    # If token is available and servers cache is empty, try to fetch them
    if config["token"] and not discord_servers:
        logger.info("Attempting to fetch Discord servers on startup...")
        try:
            fetch_discord_servers(config["token"])
        except Exception as e:
            logger.error(f"Failed to fetch Discord servers on startup: {e}")
    
    # Read port from environment variable or use default 8080
    # (to avoid conflict with macOS AirPlay on port 5000)
    try:
        port_str = os.environ.get("DISCORD_WEBUI_PORT", "8080").strip()
        port = int(port_str)
        if port < 1024 or port > 65535:
            logger.warning(f"Port {port} is out of valid range, using default 8080")
            port = 8080
    except (ValueError, TypeError):
        logger.warning(f"Invalid port setting, using default: 8080")
        port = 8080
    
    # Get host binding (0.0.0.0 for all interfaces, 127.0.0.1 for localhost only)
    # Make sure to strip any whitespace or unwanted characters
    try:
        host = os.environ.get("DISCORD_WEBUI_HOST", "0.0.0.0").strip()
        
        # Validate the host (make sure it's just an IP or hostname)
        if not re.match(r'^[\w\.\-]+$', host):
            logger.warning(f"Invalid host binding '{host}', using 0.0.0.0 instead")
            host = "0.0.0.0"
    except Exception as e:
        logger.warning(f"Error parsing host: {e}, using default: 0.0.0.0")
        host = "0.0.0.0"
    
    logger.info(f"Starting Discord Exporter Web UI on {host}:{port}")
    app.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    main_cli()
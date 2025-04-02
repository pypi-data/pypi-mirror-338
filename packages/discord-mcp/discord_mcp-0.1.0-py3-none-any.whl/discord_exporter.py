#!/usr/bin/env python3
"""
Discord Chat Exporter Wrapper

This module provides a Python wrapper for DiscordChatExporter, a tool for
exporting Discord chat history to various formats.
"""

import os
import sys
import platform
import zipfile
import subprocess
import tempfile
import shutil
import logging
import traceback
import requests
import re
from pathlib import Path
from typing import List, Optional, Dict, Any

# Configure logger to write to stderr
logger = logging.getLogger("discord_exporter")
handler = logging.StreamHandler(sys.stderr)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing special characters and emojis.
    
    Args:
        filename: The filename to sanitize
        
    Returns:
        Sanitized filename that is safe for all filesystems
    """
    # Handle None or empty input
    if not filename:
        return "discord_export"
    
    # Replace backslashes and forward slashes with dashes
    filename = filename.replace('\\', '-').replace('/', '-')
    
    # Remove emojis and other non-ASCII characters
    # This pattern matches any character that is not alphanumeric, space, or common punctuation
    sanitized = re.sub(r'[^\w\s\.\-_]', '', filename)
    
    # Replace multiple spaces with a single space
    sanitized = re.sub(r'\s+', ' ', sanitized)
    
    # Replace problematic characters in the filename with underscores
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', sanitized)
    
    # Trim the result
    sanitized = sanitized.strip()
    
    # If the result is empty, use a placeholder
    if not sanitized:
        return "discord_export"
    
    # Limit the length of the filename
    if len(sanitized) > 200:
        # Keep the extension if it exists
        ext_match = re.search(r'(\.[^\.]+)$', sanitized)
        extension = ext_match.group(1) if ext_match else ""
        
        # Truncate the name part to fit within 200 chars including extension
        max_name_length = 200 - len(extension)
        sanitized = sanitized[:max_name_length] + extension
        
    return sanitized

class DiscordExporter:
    """A wrapper for DiscordChatExporter to export Discord chat history."""
    
    DCE_VERSION = "2.40.3"  # Latest stable version as of now
    
    def __init__(self, 
                 output_dir: str = "./discord_exports",
                 dce_path: Optional[str] = None,
                 token: Optional[str] = None):
        """
        Initialize the Discord Exporter.
        
        Args:
            output_dir: Directory to store exports
            dce_path: Path to DiscordChatExporter files (will download if not provided)
            token: Discord authentication token
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.token = token
        
        # Determine the correct download for the platform
        self.system = platform.system().lower()
        if self.system not in ['windows', 'linux', 'darwin']:
            raise ValueError(f"Unsupported platform: {self.system}")
            
        # Set path for DCE or use provided path
        if dce_path:
            self.dce_path = Path(dce_path)
        else:
            self.dce_path = Path("./dce")
            self.dce_path.mkdir(parents=True, exist_ok=True)
        
        # Check if DCE exists, download if not
        self.dce_cli_path = self._get_dce_path()
    
    def _get_dce_path(self) -> Path:
        """
        Get the path to DiscordChatExporter CLI. Download if not found.
        
        Returns:
            Path to the DCE CLI executable
        """
        if self.system == 'windows':
            cli_path = self.dce_path / "DiscordChatExporter.Cli.exe"
        elif self.system in ['linux', 'darwin']:
            cli_path = self.dce_path / "DiscordChatExporter.Cli"
        
        logger.info(f"System detected: {self.system}")
        logger.info(f"Looking for DiscordChatExporter CLI at {cli_path}")
        
        # Check if the main executable exists
        if cli_path.exists():
            logger.info(f"Found DiscordChatExporter executable at {cli_path}")
            
            # Check if we have the required DLL files
            dll_files = list(self.dce_path.glob("*.dll"))
            if len(dll_files) == 0:
                logger.warning("No .dll files found in the dce directory")
                
                # Check if there are subdirectories that might contain the DLLs
                subdirs_with_dlls = []
                for subdir in self.dce_path.iterdir():
                    if subdir.is_dir():
                        subdir_dlls = list(subdir.glob("*.dll"))
                        if len(subdir_dlls) > 0:
                            subdirs_with_dlls.append(subdir)
                
                if subdirs_with_dlls:
                    logger.info(f"Found .dll files in subdirectory: {subdirs_with_dlls[0]}")
                    
                    # Copy all DLLs to the main directory
                    for dll in list(subdirs_with_dlls[0].glob("*.dll")):
                        shutil.copy(dll, self.dce_path)
                    
                    logger.info(f"Copied all DLL files to {self.dce_path}")
                else:
                    logger.warning("Missing required DLL files. DiscordChatExporter may not work properly")
            
            # Check file permissions
            try:
                if self.system in ['linux', 'darwin'] and not os.access(cli_path, os.X_OK):
                    logger.warning(f"File exists but is not executable. Trying to fix permissions...")
                    os.chmod(cli_path, 0o755)
                    logger.info(f"Set executable permissions on {cli_path}")
            except Exception as e:
                logger.error(f"Error setting executable permissions: {e}")
            
            return cli_path
        
        # Try to find the executable with a case-insensitive search
        potential_executables = []
        for file in self.dce_path.glob("*"):
            filename = file.name.lower()
            if filename.startswith("discordchatexporter.cli") and file.is_file():
                potential_executables.append(file)
        
        if potential_executables:
            executable = potential_executables[0]
            logger.info(f"Found executable with different casing: {executable}")
            
            # Create a symlink or copy with the expected name
            if self.system in ['linux', 'darwin']:
                try:
                    # Try to create a symlink first
                    if not cli_path.exists():
                        os.symlink(executable, cli_path)
                        logger.info(f"Created symlink from {executable} to {cli_path}")
                except Exception:
                    # If symlink fails, copy the file
                    shutil.copy(executable, cli_path)
                    logger.info(f"Copied {executable} to {cli_path}")
                
                # Make executable
                os.chmod(cli_path, 0o755)
            else:
                # On Windows, just copy the file
                shutil.copy(executable, cli_path)
                logger.info(f"Copied {executable} to {cli_path}")
            
            return cli_path
        
        # Download DCE if not found
        logger.info("DiscordChatExporter not found. Downloading...")
        download_success = self._download_dce()
        
        # Check if download/extraction was successful
        if not cli_path.exists():
            # Try to look for the executable in subdirectories
            for subdir in self.dce_path.iterdir():
                if subdir.is_dir():
                    for file in subdir.glob("DiscordChatExporter.Cli*"):
                        if file.is_file():
                            logger.info(f"Found executable in subdirectory: {file}")
                            
                            # Copy or link it to the expected location
                            if self.system in ['linux', 'darwin']:
                                if not cli_path.exists():
                                    try:
                                        os.symlink(file, cli_path)
                                        logger.info(f"Created symlink from {file} to {cli_path}")
                                    except Exception:
                                        shutil.copy(file, cli_path)
                                        logger.info(f"Copied {file} to {cli_path}")
                                
                                # Make executable
                                os.chmod(cli_path, 0o755)
                            else:
                                # On Windows, just copy the file
                                shutil.copy(file, cli_path)
                                logger.info(f"Copied {file} to {cli_path}")
                            
                            # Also copy all DLL files to the main directory
                            for dll in subdir.glob("*.dll"):
                                shutil.copy(dll, self.dce_path)
                            
                            logger.info(f"Copied all supporting files to {self.dce_path}")
                            return cli_path
            
            # If still not found, raise error
            error_msg = f"DiscordChatExporter not found at {cli_path} after download attempt"
            logger.error(error_msg)
            raise FileNotFoundError(
                f"{error_msg}. Please download it manually from "
                "https://github.com/Tyrrrz/DiscordChatExporter/releases"
            )
        
        logger.info(f"Successfully initialized DiscordChatExporter at {cli_path}")
        return cli_path
    
    def _download_dce(self):
        """Download and extract DiscordChatExporter."""
        # Determine download URL
        base_url = f"https://github.com/Tyrrrz/DiscordChatExporter/releases/download/{self.DCE_VERSION}/"
        
        if self.system == 'windows':
            filename = f"DiscordChatExporter.Cli.{self.DCE_VERSION}.zip"
        elif self.system in ['linux', 'darwin']:
            filename = f"DiscordChatExporter.Cli.{self.DCE_VERSION}.zip"
        
        download_url = base_url + filename
        
        # Download file
        try:
            logger.info(f"Downloading from {download_url}")
            response = requests.get(download_url, stream=True)
            response.raise_for_status()
            
            zip_path = self.dce_path / filename
            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Extract all contents of the zip file
            logger.info(f"Extracting all files from {zip_path} to {self.dce_path}")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # List all files in the zip for debugging
                file_list = zip_ref.namelist()
                logger.info(f"Files in zip: {file_list}")
                
                # Extract everything
                zip_ref.extractall(self.dce_path)
            
            # Set executable permissions for Linux/macOS
            if self.system in ['linux', 'darwin']:
                # Make main executable file executable
                cli_path = self.dce_path / "DiscordChatExporter.Cli"
                if cli_path.exists():
                    os.chmod(cli_path, 0o755)
                    logger.info(f"Set executable permissions on {cli_path}")
                else:
                    # Look for the executable in any subdirectories
                    for root, dirs, files in os.walk(self.dce_path):
                        for file in files:
                            if file == "DiscordChatExporter.Cli" or file.startswith("DiscordChatExporter") and not file.endswith(".dll"):
                                full_path = os.path.join(root, file)
                                os.chmod(full_path, 0o755)
                                logger.info(f"Set executable permissions on {full_path}")
            
            # Clean up zip file
            os.remove(zip_path)
            
            # Check if the necessary files were extracted
            dll_files = list(self.dce_path.glob("*.dll"))
            logger.info(f"Found {len(dll_files)} .dll files in {self.dce_path}")
            
            if len(dll_files) > 0:
                logger.info(f"Downloaded DiscordChatExporter to {self.dce_path}")
                return True
            else:
                logger.warning(f"No .dll files found in {self.dce_path}. The extraction might have created a subdirectory.")
                
                # Look for .dll files in subdirectories
                for subdir in self.dce_path.iterdir():
                    if subdir.is_dir():
                        subdir_dlls = list(subdir.glob("*.dll"))
                        if len(subdir_dlls) > 0:
                            logger.info(f"Found {len(subdir_dlls)} .dll files in {subdir}")
                            return True
                
                logger.error("Could not find necessary DiscordChatExporter files after extraction")
                return False
            
        except requests.RequestException as e:
            logger.error(f"Error downloading DiscordChatExporter: {e}")
            logger.error("Please download it manually from "
                 "https://github.com/Tyrrrz/DiscordChatExporter/releases")
            return False
    
    def check_dotnet(self) -> bool:
        """
        Check if .NET Runtime is installed.
        
        Returns:
            True if .NET is installed, False otherwise
        """
        try:
            logger.info("Checking for .NET Runtime...")
            
            # First check if dotnet command exists
            if shutil.which("dotnet") is None:
                logger.error("dotnet command not found in PATH. Please install .NET Runtime from https://dotnet.microsoft.com/download")
                logger.error("For macOS users: 'brew install dotnet' | For Ubuntu/Debian: 'sudo apt-get install dotnet-runtime'")
                print("\n==== .NET RUNTIME MISSING ====")
                print("DiscordChatExporter requires .NET Runtime to be installed.")
                print("Please install .NET Runtime from: https://dotnet.microsoft.com/download")
                print("  - macOS: brew install dotnet")
                print("  - Ubuntu/Debian: sudo apt-get install dotnet-runtime")
                print("  - Windows: Download from Microsoft's website")
                print("==== ===================== ====\n")
                return False
            
            # Try to check dotnet version
            result = subprocess.run(
                ["dotnet", "--list-runtimes"], 
                capture_output=True, 
                text=True
            )
            
            if result.returncode == 0:
                if "Microsoft.NETCore.App" in result.stdout:
                    # Successfully found .NET runtime
                    runtime_version = re.search(r'Microsoft\.NETCore\.App (\d+\.\d+\.\d+)', result.stdout)
                    if runtime_version:
                        logger.info(f"Found .NET Runtime version: {runtime_version.group(1)}")
                    else:
                        logger.info("Found .NET Runtime (version unknown)")
                    return True
                else:
                    logger.warning("dotnet command available but .NET Runtime not found. You may have only SDK installed.")
                    return self._fallback_dotnet_check()
            else:
                # Try alternative check
                return self._fallback_dotnet_check()
                
        except FileNotFoundError:
            logger.error("dotnet command not found in PATH. Please install .NET Runtime from https://dotnet.microsoft.com/download")
            return False
        except Exception as e:
            logger.error(f"Unexpected error checking for .NET: {str(e)}")
            logger.error(traceback.format_exc())
            return self._fallback_dotnet_check()
    
    def _fallback_dotnet_check(self) -> bool:
        """Fallback method to check for .NET Runtime existence"""
        try:
            # Try a simple dotnet --info command
            result = subprocess.run(
                ["dotnet", "--info"], 
                capture_output=True, 
                text=True
            )
            
            if result.returncode == 0:
                logger.info("dotnet command works with --info parameter. Assuming runtime is available.")
                return True
            
            # On some systems --version might work
            result = subprocess.run(
                ["dotnet", "--version"], 
                capture_output=True, 
                text=True
            )
            
            if result.returncode == 0:
                logger.info(f"Found .NET version: {result.stdout.strip()}")
                return True
                
            # Check if we can run a minimal app
            # This is a harsher check but will confirm if the runtime is actually functional
            logger.warning("Standard dotnet checks failed. Trying to execute a minimal .NET command...")
            
            # Check if the DCE files exist - if so, we can try to run a help command as a test
            if (self.dce_path / "DiscordChatExporter.Cli").exists() or (self.dce_path / "DiscordChatExporter.Cli.exe").exists():
                logger.info("Found DiscordChatExporter, trying to run a simple help command...")
                
                try:
                    test_cmd = [str(self.dce_cli_path), "--help"]
                    test_result = subprocess.run(
                        test_cmd,
                        capture_output=True,
                        text=True,
                        timeout=5  # Add timeout to prevent hanging
                    )
                    
                    if test_result.returncode == 0:
                        logger.info("DiscordChatExporter help command worked, .NET runtime is functional")
                        return True
                    else:
                        logger.error(f"DiscordChatExporter help command failed: {test_result.stderr}")
                except Exception as e:
                    logger.error(f"Error running DiscordChatExporter test: {e}")
            
            # Display detailed error message
            logger.error(f".NET Runtime check failed with return code {result.returncode}")
            logger.error(f"STDERR: {result.stderr}")
            
            print("\n==== .NET RUNTIME ERROR ====")
            print("DiscordChatExporter requires .NET Runtime to be installed and functional.")
            print("Your system appears to have the dotnet command, but the runtime is not working correctly.")
            print("Please install or repair your .NET Runtime installation from: https://dotnet.microsoft.com/download")
            print("  - macOS: brew install dotnet")
            print("  - Ubuntu/Debian: sudo apt-get install dotnet-runtime")
            print("  - Windows: Download from Microsoft's website")
            print("==== =================== ====\n")
            
            return False
            
        except Exception as e:
            logger.error(f"Fallback .NET check failed: {e}")
            return False
    
    def export_channel(self, 
                      channel_id: str, 
                      token: Optional[str] = None,
                      format: str = "Json",
                      after: Optional[str] = None,
                      before: Optional[str] = None,
                      partition: Optional[str] = None) -> Optional[Path]:
        """
        Export a Discord channel.
        
        Args:
            channel_id: Discord channel ID
            token: Discord authentication token (overrides the one set in constructor)
            format: Export format (Json, HtmlDark, HtmlLight, etc.)
            after: Get messages after this date (ISO 8601)
            before: Get messages before this date (ISO 8601)
            partition: Split output into partitions (e.g., "monthly")
            
        Returns:
            Path to the exported file or None if export failed
        """
        # Check requirements
        if not self.check_dotnet():
            logger.error("Cannot proceed with export due to missing .NET Runtime")
            print("\n======================= EXPORT FAILED =======================")
            print("DiscordChatExporter requires .NET Runtime to be installed.")
            print("Please install the .NET Runtime from Microsoft's website:")
            print("  https://dotnet.microsoft.com/download")
            print("")
            print("Installation commands:")
            print("  - macOS: brew install dotnet")
            print("  - Ubuntu/Debian: sudo apt-get install -y dotnet-runtime")
            print("  - Windows: Download installer from Microsoft's website")
            print("")
            print("After installing, restart this application to continue.")
            print("================================================================\n")
            return None
        
        # Use token from constructor if not provided
        token = token or self.token
        if not token:
            print("Discord token is required. Please provide a token.")
            return None
        
        # Build command
        cmd = [str(self.dce_cli_path), "export", 
               "-t", token,
               "-c", channel_id,
               "-f", format,
               "-o", str(self.output_dir)]
        
        # Add optional parameters
        if after:
            cmd.extend(["--after", after])
        if before:
            cmd.extend(["--before", before])
        if partition:
            cmd.extend(["-p", partition])
        
        # Run command
        try:
            # Log the full command being executed
            logger.info(f"Exporting channel {channel_id} with command: {' '.join(cmd)}")
            logger.info(f"Working directory: {os.getcwd()}")
            
            # Check if executable exists and is accessible
            if not os.path.exists(cmd[0]):
                logger.error(f"Executable not found at path: {cmd[0]}")
                return None
                
            if os.path.isfile(cmd[0]) and not os.access(cmd[0], os.X_OK):
                logger.error(f"Executable found but not executable: {cmd[0]}")
                # Try to make it executable
                try:
                    os.chmod(cmd[0], 0o755)
                    logger.info(f"Set executable permissions on {cmd[0]}")
                except Exception as perm_e:
                    logger.error(f"Failed to set executable permissions: {perm_e}")
            
            # Run the command with comprehensive logging
            logger.info("Executing subprocess...")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                # Find the exported file
                # DCE names files with channel ID and possibly channel name
                # Get the most recently modified file matching the pattern
                exported_files = sorted(
                    list(self.output_dir.glob(f"*{channel_id}*.json")), 
                    key=lambda f: f.stat().st_mtime, 
                    reverse=True
                )
                
                if exported_files:
                    original_file = exported_files[0]
                    logger.info(f"Found exported file at {original_file}")
                    
                    # Sanitize the filename
                    original_name = original_file.name
                    sanitized_name = sanitize_filename(original_name)
                    
                    # Ensure the sanitized name is valid
                    if not sanitized_name or sanitized_name == "":
                        sanitized_name = f"discord_channel_{channel_id}"
                    
                    # Always add .json extension if missing
                    if not sanitized_name.endswith('.json'):
                        sanitized_name = f"{sanitized_name}.json"
                        
                    # Make sure the sanitized name still includes the channel ID
                    if channel_id not in sanitized_name:
                        sanitized_name = sanitized_name.replace('.json', f'_{channel_id}.json')
                    
                    # Create the new path
                    sanitized_path = original_file.parent / sanitized_name
                    
                    # Only rename if the sanitized name is different
                    if sanitized_name != original_name:
                        # Rename the file
                        try:
                            original_file.rename(sanitized_path)
                            logger.info(f"Renamed exported file to {sanitized_path}")
                            return sanitized_path
                        except Exception as e:
                            logger.error(f"Error renaming file: {e}")
                            return original_file
                    
                    return original_file
                else:
                    logger.error("Export command succeeded but couldn't find the output file.")
                    return None
            else:
                # Log the detailed error output
                logger.error(f"Export failed with returncode {result.returncode}")
                logger.error(f"STDERR: {result.stderr}")
                logger.error(f"STDOUT: {result.stdout}")
                return None
                
        except Exception as e:
            import traceback
            logger.error(f"Error running DiscordChatExporter: {e}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            return None
    
    def export_guild(self, 
                    guild_id: str, 
                    token: Optional[str] = None,
                    format: str = "Json",
                    channel_ids: Optional[List[str]] = None) -> List[Path]:
        """
        Export all channels in a Discord guild/server.
        
        Args:
            guild_id: Discord guild/server ID
            token: Discord authentication token (overrides the one set in constructor)
            format: Export format (Json, HtmlDark, HtmlLight, etc.)
            channel_ids: Optional list of specific channel IDs to export
            
        Returns:
            List of paths to exported files
        """
        # Check requirements
        if not self.check_dotnet():
            logger.error("Cannot proceed with guild export due to missing .NET Runtime")
            print("\n======================= EXPORT FAILED =======================")
            print("DiscordChatExporter requires .NET Runtime to be installed.")
            print("Please install the .NET Runtime from Microsoft's website:")
            print("  https://dotnet.microsoft.com/download")
            print("")
            print("Installation commands:")
            print("  - macOS: brew install dotnet")
            print("  - Ubuntu/Debian: sudo apt-get install -y dotnet-runtime")
            print("  - Windows: Download installer from Microsoft's website")
            print("")
            print("After installing, restart this application to continue.")
            print("================================================================\n")
            return []
        
        # Use token from constructor if not provided
        token = token or self.token
        if not token:
            print("Discord token is required. Please provide a token.")
            return []
        
        # First, get channel list if not provided
        if not channel_ids:
            channel_ids = self.get_guild_channels(guild_id, token)
            if not channel_ids:
                print(f"No channels found in guild {guild_id}")
                return []
        
        # Export each channel
        exported_files = []
        for channel_id in channel_ids:
            exported_file = self.export_channel(
                channel_id=channel_id,
                token=token,
                format=format
            )
            if exported_file:
                exported_files.append(exported_file)
        
        return exported_files
    
    def get_guild_channels(self, guild_id: str, token: Optional[str] = None) -> List[str]:
        """
        Get a list of channel IDs in a guild.
        
        Args:
            guild_id: Discord guild/server ID
            token: Discord authentication token
            
        Returns:
            List of channel IDs
        """
        # Check requirements
        if not self.check_dotnet():
            logger.error("Cannot list guild channels due to missing .NET Runtime")
            print("\n======================= OPERATION FAILED =======================")
            print("DiscordChatExporter requires .NET Runtime to be installed.")
            print("Please install the .NET Runtime from Microsoft's website:")
            print("  https://dotnet.microsoft.com/download")
            print("")
            print("Installation commands:")
            print("  - macOS: brew install dotnet")
            print("  - Ubuntu/Debian: sudo apt-get install -y dotnet-runtime")
            print("  - Windows: Download installer from Microsoft's website")
            print("")
            print("After installing, restart this application to continue.")
            print("================================================================\n")
            return []
        
        # Use token from constructor if not provided
        token = token or self.token
        if not token:
            print("Discord token is required. Please provide a token.")
            return []
        
        # Build command
        cmd = [str(self.dce_cli_path), "channels", 
               "-t", token,
               "-g", guild_id]
        
        # Run command
        try:
            # Set up logging
            import logging
            logger = logging.getLogger("discord_exporter")
            
            # Log the full command being executed
            logger.info(f"Getting channels for guild {guild_id} with command: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                # Parse channel IDs from output
                lines = result.stdout.strip().split('\n')
                channel_ids = []
                
                for line in lines:
                    if 'Text' in line or 'Announcement' in line:
                        parts = line.split()
                        if parts and parts[0].isdigit():
                            channel_ids.append(parts[0])
                
                logger.info(f"Found {len(channel_ids)} text channels in guild {guild_id}")
                return channel_ids
            else:
                # Log the detailed error output
                logger.error(f"Failed to get channels with returncode {result.returncode}")
                logger.error(f"STDERR: {result.stderr}")
                logger.error(f"STDOUT: {result.stdout}")
                return []
                
        except Exception as e:
            import traceback
            logger.error(f"Error running DiscordChatExporter: {e}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            return []
    
    def get_token_instructions(self) -> str:
        """
        Get instructions for obtaining a Discord token.
        
        Returns:
            Instructions as a string
        """
        return """
How to Get Your Discord Token:

1. Open Discord in your browser (not the app).
2. Press F12 to open Developer Tools.
3. Go to the Network tab.
4. Refresh the page.
5. Find a request to "api/v9/users/@me" or similar.
6. Look in the request headers for "Authorization".
7. Your token is the value after "Authorization".

WARNING: 
- Keep your token secret! Don't share it with anyone.
- Using a token for DiscordChatExporter is technically against Discord's ToS. 
- Use at your own risk and be responsible with the exports.
"""

# Test code
if __name__ == "__main__":
    exporter = DiscordExporter()
    
    print(exporter.get_token_instructions())
    
    token = input("Enter your Discord token: ")
    
    channel_id = input("Enter a Discord channel ID to export: ")
    
    exported_file = exporter.export_channel(
        channel_id=channel_id,
        token=token,
        format="Json"
    )
    
    if exported_file:
        print(f"Successfully exported to {exported_file}")
    else:
        print("Export failed.")
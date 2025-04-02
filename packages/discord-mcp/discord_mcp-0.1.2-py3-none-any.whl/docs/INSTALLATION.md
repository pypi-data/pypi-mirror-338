# Installation Guide

This guide provides detailed instructions for installing and setting up Discord MCP, both locally and in a remote configuration.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Docker Installation (Recommended)](#docker-installation-recommended)
- [Manual Installation](#manual-installation)
- [Getting Your Discord Token](#getting-your-discord-token)
- [Configuring Channels](#configuring-channels)
- [Remote Deployment](#remote-deployment)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, you'll need:

- A Discord account and user token (see [Getting Your Discord Token](#getting-your-discord-token))
- For Docker installation:
  - [Docker](https://docs.docker.com/get-docker/)
  - [Docker Compose](https://docs.docker.com/compose/install/)
- For manual installation:
  - Python 3.10+
  - [.NET Runtime 7.0+](https://dotnet.microsoft.com/download)
  - Claude Desktop (with MCP support)

## Docker Installation (Recommended)

Using Docker is the easiest way to get started, as it handles all dependencies automatically.

1. **Clone the repository**:

```bash
git clone git@github.com:LouD82/discord-mcp.git
cd discord-mcp
```

2. **Run the setup script**:

```bash
chmod +x setup.sh
./setup.sh
```

The setup script will guide you through the installation process, including:
- Checking for Docker
- Creating necessary directories
- Setting up your Discord token
- Building and starting the containers

3. **Or manually set up with Docker**:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env to add your Discord token
nano .env  # or use any text editor

# Build and start the containers
docker-compose up -d
```

4. **Access the web UI**:

Once the containers are running, you can access the web UI at:
http://localhost:8080

## Manual Installation

If you prefer not to use Docker, you can install Discord MCP manually:

1. **Clone the repository**:

```bash
git clone git@github.com:LouD82/discord-mcp.git
cd discord-mcp
```

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Install .NET Runtime**:

The DiscordChatExporter tool requires .NET Runtime 7.0 or higher. Download and install it from:
https://dotnet.microsoft.com/download

5. **Set up environment variables**:

```bash
cp .env.example .env
# Edit .env with your Discord token and other settings
```

6. **Create data directories**:

```bash
mkdir -p discord_data/exports
```

7. **Run the components**:

In one terminal:
```bash
python discord_mcp_server.py
```

In another terminal:
```bash
python discord_webui.py
```

8. **Configure Claude Desktop**:

Add this server to Claude Desktop by adding the following to your configuration:

```json
"Discord Messages": {
  "command": "/path/to/discord-mcp/run_discord_mcp.sh",
  "args": [],
  "env": {
    "DISCORD_DATA_DIR": "/absolute/path/to/discord/data",
    "DISCORD_USER_TOKEN": "your_discord_token"
  }
}
```

> **Important:** `DISCORD_DATA_DIR` must be an absolute path, especially when running in read-only environments like Claude Desktop with pipx.

## Getting Your Discord Token

To get your Discord authentication token:

1. Open Discord in your browser (not the app)
2. Press F12 to open Developer Tools
3. Go to the Network tab
4. Refresh the page
5. Find a request to "api/v9/users/@me" or similar
6. Look in the request headers for "Authorization"
7. Your token is the value after "Authorization"

**IMPORTANT**: Keep your token secret and never share it. Using your token with third-party tools like DiscordChatExporter is technically against Discord's Terms of Service, although it's commonly used for personal archiving. Use at your own risk and be responsible with the exports.

## Configuring Channels

To configure which Discord channels are monitored:

1. Find the channel IDs of the channels you want to monitor:
   - Right-click on a channel in Discord
   - Select "Copy Channel ID" (you may need to enable Developer Mode in Discord settings)

2. Add channel IDs to the `channels.txt` file:
   - Create a text file named `channels.txt` in the project root
   - Add one channel ID per line

Example `channels.txt`:
```
1234567890123456789
9876543210987654321
```

3. Alternatively, use the web UI to manage channels:
   - Open http://localhost:8080
   - Go to the Channels tab
   - Add or remove channels as needed

## Remote Deployment

Discord MCP supports a service-oriented architecture where database and API services run on a remote server while the MCP client runs locally.

### Architecture Overview

The system can be deployed in two main configurations:

1. **Local-only**: Everything runs on a single machine (described in previous sections)
2. **Service-oriented**: Database and API services run on a remote server while the MCP client runs locally

The service-oriented architecture allows you to:
- Keep your data in one centralized location
- Access your Discord message database from multiple client machines
- Offload computationally intensive tasks to a more powerful server
- Maintain the local Claude Desktop integration with the MCP protocol

### Components

The system consists of these key components:

1. **MCP Client** (`discord_mcp_server.py`): Runs locally with Claude Desktop, provides data to Claude
2. **Database Service** (`db_service.py`): Provides Discord data API for message access
3. **Web UI** (`discord_webui.py`): Web interface for managing the system (runs on the same machine as the database service)

### Deployment Option

With the current architecture, the Web UI must always run on the same machine as the database service.

1. **Remote Server** (Linux/Ubuntu):
   - Database Service
   - Web UI
   - Discord data

2. **Local Machine** (macOS/Windows):
   - MCP Client (with Claude Desktop)
   - Configuration points to remote database service

### Remote Server Setup

1. **Clone the repository to your remote server**:
   ```bash
   git clone https://github.com/LouD82/discord-mcp.git
   cd discord-mcp
   ```

2. **Create a `.env` file**:
   ```bash
   cp .env.example .env
   ```

3. **Edit the `.env` file** with your configuration:
   ```
   DISCORD_DATA_DIR=/absolute/path/to/discord_data
   API_KEY=your_secure_api_key_here  # Choose a strong API key
   ```

4. **Start the services using Docker** (recommended):
   ```bash
   docker-compose up -d db-service
   # If you want the web UI as well:
   docker-compose up -d discord-webui
   ```

   Alternatively, run without Docker:
   ```bash
   pip install -r requirements.txt
   python db_service.py
   ```

5. **Copy your Discord data** to the remote server if needed:
   ```bash
   # From your local machine:
   scp -r ./discord_data user@remote-server:/path/to/discord-mcp/
   ```

### Local Machine Setup with Remote Database

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/LouD82/discord-mcp.git
   cd discord-mcp
   ```

2. **Create a `.env` file**:
   ```bash
   cp .env.example .env
   ```

3. **Edit the `.env` file** with your remote server information:
   ```
   # Point to remote services
   DISCORD_API_URL=http://your-remote-server:8081
   API_KEY=your_secure_api_key_here  # Same as on the server
   
   # Local settings
   MCP_HOST=127.0.0.1  # Use localhost for security
   ```

4. **Start the MCP server**:
   ```bash
   python discord_mcp_server.py
   ```

5. **Configure Claude Desktop** to connect to your local MCP server at `http://localhost:21001`

Note: The Web UI will only run on the remote server and cannot be run on your local machine.

### Security Considerations

1. **API Key**: Always use a strong API key to secure the connection between your local client and remote server.

2. **Firewall**: Configure your server firewall to only allow connections on port 8081 from trusted IP addresses.

3. **HTTPS**: For production use, consider setting up HTTPS with a reverse proxy like Nginx.

### Custom Ports

You can modify the port used by the API service in your `.env` file:

```
API_PORT=8081
```

Remember to update your Docker configuration and firewall rules if you change these ports.

## Troubleshooting

### Common Issues

1. **"Discord token is required but not provided"**
   - Make sure your Discord token is correctly set in the .env file
   - For Docker, make sure the .env file is in the same directory as docker-compose.yml

2. **".NET Runtime not found"**
   - Install .NET Runtime 7.0 or higher from https://dotnet.microsoft.com/download
   - For Docker, this should be handled automatically

3. **"Failed to connect to Discord API"**
   - Check that your Discord token is valid and not expired
   - Try refreshing your token by following the steps in [Getting Your Discord Token](#getting-your-discord-token)

4. **"No messages found matching the criteria"**
   - Check that your channels.txt file contains valid channel IDs
   - Make sure the auto-exporter has successfully exported messages
   - Check the logs for any errors during export

5. **Docker container won't start**
   - Check Docker logs: `docker-compose logs`
   - Make sure ports 21001 and 8080 are not already in use
   - Verify that Docker has enough resources allocated

6. **Connection Issues with Remote Server**
   - Check firewall settings on your remote server: `sudo ufw status`
   - Verify services are running: `curl http://your-remote-server:8081/api/status`
   - Check logs: `docker-compose logs db-service` or `cat db_service.log`

### Logs

Check the following logs for more information:

- **MCP Server Logs**: `discord_mcp.log`
- **Web UI Logs**: Check the console where the web UI is running
- **Docker Logs**: `docker-compose logs`
- **Database Service Logs**: `db_service.log`

### Getting Help

If you encounter issues not covered here:

1. Check the GitHub repository issues
2. Create a new issue with:
   - A clear description of the problem
   - Steps to reproduce
   - Relevant logs (with sensitive information redacted)
   - Your environment details (OS, Python version, etc.)
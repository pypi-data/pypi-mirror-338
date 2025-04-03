# Discord MCP

Discord Message Context Provider for Claude - Enables Claude to search and access Discord messages through the Model Context Protocol (MCP).

## Features

- Connect Claude to your Discord messages using MCP
- Search messages with BM25 relevance scoring
- Export Discord channels using DiscordChatExporter
- Web UI for configuration and monitoring
- Docker support for containerized deployment

## Installation

### Using pipx (Recommended)

```bash
pipx install discord-mcp
```

### Using pip

```bash
pip install discord-mcp
```

## Usage

### Setting up Claude Desktop

Configure Claude Desktop to connect to the Discord MCP server by adding the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "discord-mcp": {
      "command": "pipx",
      "args": [
        "run", 
        "discord-mcp"
      ],
      "env": {
        "DISCORD_DATA_URL": "http://your-server-ip:8081"
      }
    }
  }
}
```

### Running the MCP Server

```bash
discord-mcp
```

### Running the Web UI

```bash
discord-webui
```

## Configuration

Create a `.env` file with the following variables:

```
DISCORD_DATA_DIR=/absolute/path/to/discord_data
DISCORD_USER_TOKEN=your_discord_token
DISCORD_WEBUI_PORT=8080
DISCORD_WEBUI_HOST=0.0.0.0
```

> **Important:** `DISCORD_DATA_DIR` must be an absolute path, especially when running in read-only environments like Claude Desktop with pipx.

## Docker Deployment

```bash
docker-compose up -d
```

## License

MIT
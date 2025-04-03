# Architecture Overview

## System Components

The Discord MCP system consists of the following components:

1. **MCP Server** (`discord_mcp_server.py`) - Implements Model Context Protocol for Claude
   - Exposes port 21001 for Claude connections
   - Provides BM25 relevance-based search capabilities
   - Connects to either local or remote services

2. **Database Service** (`db_service.py`) - Provides data storage services
   - Discord Data API - Message data service (port 8081)
   - Handles message storage and retrieval

3. **Web UI** (`discord_webui.py`) - Configuration and monitoring interface
   - Exposes port 8080 for web access
   - Manages channel configuration
   - Monitors export status
   - Provides logs and diagnostics

4. **BM25 Search** - Relevance-based search implementation
   - Built into the MCP server using bm25s library
   - Fast, efficient keyword search with relevance scoring
   - Provides search functions with configurable relevance threshold

5. **Discord Exporter** - Downloads and processes Discord messages
   - Auto-exports messages from configured channels
   - Handles authentication with Discord
   - Stores messages for search and analysis

## Architecture

### Local Deployment

In a standard local deployment, all components run on the same machine:

1. The MCP server connects to local files and processes search requests
2. The Web UI manages local configuration and exports
3. Claude Desktop connects to the local MCP server

```
┌──────────────────────────────────────────────────────────┐
│                      Local Machine                        │
│                                                          │
│  ┌─────────────┐      ┌────────────┐     ┌────────────┐  │
│  │ Claude      │      │            │     │            │  │
│  │ Desktop     │◄────►│ MCP Server │◄───►│  Discord   │  │
│  │             │      │ (BM25)     │     │  Data      │  │
│  └─────────────┘      └────────────┘     └────────────┘  │
│                              ▲                 ▲         │
│                              │                 │         │
│                              ▼                 │         │
│                       ┌────────────┐          │         │
│                       │            │          │         │
│                       │   Web UI   │◄─────────┘         │
│                       │            │                    │
│                       └────────────┘                    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Service-Oriented Deployment

In a service-oriented deployment:

1. Claude Desktop and the MCP server run on the local machine
2. The MCP server connects to service endpoints via HTTP
3. The database service, Web UI, and exporters run together on a remote server

```
┌─────────────────────────────────────┐   ┌──────────────────────────────────────┐
│          Local Machine              │   │            Remote Server             │
│                                     │   │                                      │
│  ┌─────────────┐    ┌────────────┐  │   │  ┌────────────────────────────────┐  │
│  │ Claude      │    │            │  │   │  │                                │  │
│  │ Desktop     │◄───►│ MCP Server │◄─┼───┼─►│ Discord Data API (port 8081)  │  │
│  │             │    │ (BM25)     │  │   │  │                                │  │
│  └─────────────┘    └────────────┘  │   │  │                                │  │
│                                     │   │  └────────────────────────────────┘  │
└─────────────────────────────────────┘   │              ▲                       │
                                          │              │                       │
                                          │              ▼                       │
                                          │       ┌────────────┐                 │
                                          │       │            │                 │
                                          │       │   Web UI   │                 │
                                          │       │            │                 │
                                          │       └────────────┘                 │
                                          │                                      │
                                          └──────────────────────────────────────┘
```

## Data Flow

1. The Discord exporter downloads messages from configured channels
2. Message data is stored in JSON format in the Discord data directory
3. The MCP server loads messages in memory and indexes them with BM25
4. The MCP server receives queries from Claude and performs BM25 relevance search
5. Relevant search results are returned to Claude via the MCP protocol

## Deployment Options

The system supports three deployment options:

1. **Local Deployment** - All components on a single machine
2. **Docker Deployment** - Components in Docker containers on a single machine
3. **Service-Oriented Deployment** - MCP client on local machine, with database services and WebUI on remote server

## Service Endpoints

The system uses the following service endpoints:

1. **Discord Data API**: REST API for message data
   - Default URL: `http://localhost:8081`
   - Environment variable: `DISCORD_API_URL`

2. **Authentication**:
   - API Key for securing service access
   - Environment variable: `API_KEY`

## Environment Configuration

The system is configured through environment variables:

1. **Data Paths**:
   - `DISCORD_DATA_DIR`: Path to Discord message data

2. **Service URLs**:
   - `DISCORD_API_URL`: URL of Discord data API service

3. **Authentication**:
   - `API_KEY`: API key for service authentication

4. **Server Configuration**:
   - `MCP_HOST`: Host address for MCP server (default: 127.0.0.1)
   - `API_PORT`: Port for Discord data API (default: 8081)

See the Remote Deployment Guide for detailed setup instructions.
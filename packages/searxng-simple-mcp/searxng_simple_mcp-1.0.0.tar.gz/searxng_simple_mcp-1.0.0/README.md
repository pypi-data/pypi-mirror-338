# SearxNG MCP Server

A Model Context Protocol (MCP) server that provides web search capabilities using SearxNG, allowing AI assistants like Claude to search the web.

## Overview

This project implements an MCP server that connects to SearxNG, a privacy-respecting metasearch engine. The server provides a simple and efficient way for Large Language Models to search the web without tracking users.

### Features

- Privacy-focused web search through SearxNG
- Simple API for LLM integration
- Compatible with Claude Desktop and other MCP-compliant clients
- Configurable search parameters
- Clean, formatted search results optimized for LLMs

## Quick Start

### Prerequisites

- Python 3.10 or higher
- A SearxNG instance (public or self-hosted)

### Installation

```bash
# Clone the repository
git clone https://github.com/Sacode/searxng-simple-mcp.git
cd searxng-simple-mcp

# Install dependencies
pip install uv
uv pip install -e .
```

### Using with Claude Desktop

Install the server in Claude Desktop:

```bash
# Navigate to the project directory
cd searxng-simple-mcp

# Install the server
npm run install:claude
# Or directly:
# fastmcp install src/searxng_simple_mcp/server.py
```

You can now use web search in Claude! Try prompts like:

- "Search for recent news about quantum computing."
- "Find information about climate change solutions and summarize the findings."
- "Search for Python programming tutorials and list the best ones."

### Configuration

You can configure the server using environment variables:

```bash
# Set a custom SearxNG instance
fastmcp install src/searxng_simple_mcp/server.py -e SEARXNG_MCP_SEARXNG_URL=https://your-instance.example.com

# Set default result count
fastmcp install src/searxng_simple_mcp/server.py -e SEARXNG_MCP_DEFAULT_RESULT_COUNT=15

# Or use a .env file
fastmcp install src/searxng_simple_mcp/server.py -f .env
```

The following environment variables are available for configuration:

| Environment Variable | Description | Default Value |
|----------------------|-------------|---------------|
| SEARXNG_MCP_SEARXNG_URL | URL of the SearxNG instance to use | <https://paulgo.io/> |
| SEARXNG_MCP_TIMEOUT | HTTP request timeout in seconds | 10 |
| SEARXNG_MCP_DEFAULT_RESULT_COUNT | Default number of results to return in searches | 10 |
| SEARXNG_MCP_DEFAULT_LANGUAGE | Language code for search results (e.g., 'en', 'ru', 'all') | all |
| SEARXNG_MCP_DEFAULT_FORMAT | Default format for search results ('text', 'json') | text |
| TRANSPORT_PROTOCOL | Transport protocol for MCP server ('stdio' or 'sse') | sse |

You can find a list of public SearxNG instances at [https://searx.space](https://searx.space) if you don't want to host your own.

## Development

For development and testing:

```bash
# Run in development mode
npm run dev
# Or directly:
# fastmcp dev src/searxng_simple_mcp/server.py

# This launches the MCP Inspector, a web interface for testing your server

# Run in development mode with editable dependencies
npm run dev:editable

# Install dependencies
npm run install:deps
# Or directly:
# uv pip install -e .

# Run linter
npm run lint
# Or fix linting issues automatically:
npm run lint:fix
# Format code:
npm run lint:format

# Run the server directly
npm start
# Or using FastMCP run:
npm run run

# Run with specific transport protocol
npm run run:stdio  # Use stdio transport
npm run run:sse    # Use sse transport
```

## Docker Usage

You can run this application using Docker in two ways:

1. Using the pre-built image from GitHub Container Registry (recommended)
2. Building the image locally

### Using the Pre-built Image

The project is automatically built and published to GitHub Container Registry when changes are pushed to the main branch.

```bash
# Pull the latest image
docker pull ghcr.io/sacode/searxng-simple-mcp:latest

# Run the container
docker run -p 8000:8000 --env-file .env ghcr.io/sacode/searxng-simple-mcp:latest

# Run with specific transport protocol
docker run -p 8000:8000 --env-file .env -e TRANSPORT_PROTOCOL=stdio ghcr.io/sacode/searxng-simple-mcp:latest
docker run -p 8000:8000 --env-file .env -e TRANSPORT_PROTOCOL=sse ghcr.io/sacode/searxng-simple-mcp:latest
```

### Using Docker with Pre-built Image

```bash
# Pull the latest image from GitHub Container Registry
npm run docker:pull

# Run the container (uses sse transport by default)
npm run docker:run

# Run with specific transport protocol
npm run docker:run:stdio  # Use stdio transport
npm run docker:run:sse    # Use sse transport
```

### Building Locally with Docker

```bash
# Build the Docker image
npm run docker:build

# Run the container (uses sse transport by default)
npm run docker:run:local

# Run with specific transport protocol
npm run docker:run:stdio:local  # Use stdio transport
npm run docker:run:sse:local    # Use sse transport
```

### Using Docker Compose with Pre-built Image

Docker Compose allows you to run the application along with any dependencies as a multi-container application. By default, the docker-compose.yml file is configured to use the pre-built image from GitHub Container Registry.

```bash
# Start services (uses sse transport by default)
npm run docker:compose:up

# Start services with specific transport protocol
npm run docker:compose:up:stdio  # Use stdio transport
npm run docker:compose:up:sse    # Use sse transport

# Stop services
npm run docker:compose:down

# View logs
npm run docker:compose:logs

# Build services
npm run docker:compose:build

# Restart services
npm run docker:compose:restart
```

### Docker Configuration and Image Sources

The Docker setup uses the following configuration:

- **Image Source**: By default, the image is pulled from GitHub Container Registry (`ghcr.io/sacode/searxng-simple-mcp:latest`)
- **Port**: The application runs on port 8000 inside the container, mapped to port 8000 on your host
- **Environment Variables**: Can be set in the `.env` file or in the `docker-compose.yml` file
- **Volume Mounts**: The `src` directory is mounted as a volume, allowing code changes without rebuilding the image
- **Transport Protocol**: Can be configured using the `TRANSPORT_PROTOCOL` environment variable (values: `stdio` or `sse`, default: `stdio`)

You can switch between using the pre-built image and building locally by editing the `docker-compose.yml` file (uncomment the build section and comment out the image line).

#### Transport Protocol Options

The MCP server supports two transport protocols:

- **STDIO (Standard Input/Output)**: Default protocol, useful for CLI applications and direct integration
- **SSE (Server-Sent Events)**: Alternative protocol, suitable for web-based clients and HTTP-based integrations

You can specify the transport protocol in several ways:

1. Using environment variables:

   ```
   TRANSPORT_PROTOCOL=stdio docker-compose up -d
   ```

2. Using the provided npm scripts:

   ```
   npm run docker:run:stdio
   npm run docker:compose:up:sse
   ```

3. By editing the `.env` file or `docker-compose.yml` file to set the `TRANSPORT_PROTOCOL` variable

## Continuous Integration and Deployment

This project uses GitHub Actions for continuous integration and deployment. When changes are pushed to the `main` branch, the following automated processes occur:

1. The code is checked out
2. A Docker image is built using the project's Dockerfile
3. The image is tagged with:
   - `latest` - Always points to the most recent build
   - Short SHA of the commit - For precise version tracking
   - Branch name - For feature branch identification
   - Semantic version (if tagged) - For release versioning
4. The image is published to GitHub Container Registry (ghcr.io)

You can find the published Docker images at: `ghcr.io/[your-username]/searxng-simple-mcp`

To use the published Docker image:

```bash
# Pull the latest image
docker pull ghcr.io/[your-username]/searxng-simple-mcp:latest

# Run the container
docker run -p 8000:8000 --env-file .env ghcr.io/[your-username]/searxng-simple-mcp:latest
```

The CI/CD workflow configuration can be found in `.github/workflows/docker-build-publish.yml`. The workflow has been configured with the minimum required permissions to push to the GitHub Container Registry.

### Automated Testing and Linting

In addition to the Docker build and publish workflow, this project also includes automated testing and linting:

- **When**: Runs on pull requests to the main branch and on pushes to the main branch
- **What**:
  - Runs code linting with Ruff to ensure code quality
  - Checks code formatting to maintain consistent style
  - (Future) Runs unit tests to verify functionality
This helps maintain code quality and catch issues early in the development process. The workflow configuration can be found in `.github/workflows/test-lint.yml`. This workflow uses read-only permissions for security.

### Automated Version Updates

When a new release is created on GitHub, the version number is automatically updated in the project files:

- **When**: Runs when a new release is created
- **What**:
  - Updates the version in package.json
  - Updates the version in pyproject.toml
  - Commits and pushes the changes back to the repository
This ensures that the version numbers in the project files always match the latest release. The workflow configuration can be found in `.github/workflows/release-version.yml`. This workflow has been granted write permissions to update files in the repository.

## Integration with MCP-Compatible Applications

Many applications support the Model Context Protocol (MCP) and allow configuring MCP servers through JSON configuration. Here's how to integrate this SearxNG MCP server with such applications:

### Using Docker Image with STDIO Transport (Default, Recommended for CLI Applications)

```json
{
  "mcpServers": {
    "searxng": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--network=host",
        "-e",
        "TRANSPORT_PROTOCOL=stdio",
        "-e",
        "SEARXNG_MCP_SEARXNG_URL=http://localhost:8080",
        "ghcr.io/sacode/searxng-simple-mcp:latest"
      ],
      "transport": "stdio"
    }
  }
}
```

**Note:** When using Docker with MCP servers:

1. Environment variables must be passed directly using the `-e` flag in the `args` array, as the `env` object is not properly passed to the Docker container.
2. If you need to access a SearxNG instance running on localhost (e.g., <http://localhost:8080>), you must use the `--network=host` flag to allow the container to access the host's network. Otherwise, "localhost" inside the container will refer to the container itself, not your host machine.
3. When using `--network=host`, port mappings (`-p`) are not needed and will be ignored, as the container shares the host's network stack directly.

### Using Docker Image with SSE Transport (Recommended for Web Applications)

```json
{
  "mcpServers": {
    "searxng": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "--network=host",
        "-e",
        "TRANSPORT_PROTOCOL=sse",
        "-e",
        "SEARXNG_MCP_SEARXNG_URL=http://localhost:8080",
        "ghcr.io/sacode/searxng-simple-mcp:latest"
      ],
      "transport": "sse",
      "transportOptions": {
        "url": "http://localhost:8000/mcp"
      }
    }
  }
}
```

For SSE transport, you can also deploy using docker-compose:

```yaml
# docker-compose.yml
# This example assumes using an external SearxNG instance
# You could also deploy SearxNG in the same docker-compose file
services:
  searxng-mcp:
    image: ghcr.io/sacode/searxng-simple-mcp:latest
    ports:
      - "8000:8000"
    environment:
      - TRANSPORT_PROTOCOL=sse
      - SEARXNG_MCP_SEARXNG_URL=https://searxng:8080
    restart: unless-stopped
```

Then in your MCP configuration:

```json
{
  "mcpServers": {
    "searxng": {
      "transport": "sse",
      "transportOptions": {
        "url": "http://localhost:8000/mcp"
      }
    }
  }
}
```

### Using Python with pip

If you have the package installed via pip:

```json
{
  "mcpServers": {
    "searxng": {
      "command": "python",
      "args": [
        "-m",
        "src.searxng_simple_mcp.server"
      ],
      "transport": "stdio",
      "env": {
        "TRANSPORT_PROTOCOL": "stdio",
        "SEARXNG_MCP_SEARXNG_URL": "https://your-instance.example.com"
      }
    }
  }
}
```

### Using fastmcp

If you have fastmcp installed:

```json
{
  "mcpServers": {
    "searxng": {
      "command": "fastmcp",
      "args": [
        "run",
        "path/to/searxng-simple-mcp/src/searxng_simple_mcp/server.py",
        "--transport",
        "stdio"
      ],
      "transport": "stdio"
    }
  }
}
```

### Configuration Options

You can customize the behavior by adding environment variables:

```json
{
  "mcpServers": {
    "searxng": {
      "command": "npx",
      "args": [
        "-y",
        "github:sacode/searxng-simple-mcp"
      ],
      "transport": "stdio",
      "env": {
        "SEARXNG_MCP_SEARXNG_URL": "https://your-instance.example.com",
        "SEARXNG_MCP_TIMEOUT": "15",
        "SEARXNG_MCP_DEFAULT_RESULT_COUNT": "20",
        "SEARXNG_MCP_LANGUAGE": "en"
      }
    }
  }
}
```

**Note:** For non-Docker commands like `npx` or `python`, the `env` object works correctly. Only Docker commands require passing environment variables directly via `-e` flags in the `args` array.

## Project Structure

```
searxng-simple-mcp/
│
├── src/
│   ├── run_server.py         # Entry point script
│   └── searxng_simple_mcp/
│       ├── __init__.py       # Package initialization
│       ├── server.py         # Main MCP server implementation
│       ├── searxng_client.py # Client for SearxNG API
│       └── config.py         # Configuration settings
│
├── docker-compose.yml        # Docker Compose configuration
├── Dockerfile                # Docker configuration
├── pyproject.toml            # Python project configuration
├── package.json              # NPM scripts and metadata
└── .env.example              # Example environment variables
```

## Why SearxNG?

SearxNG offers several advantages for AI-powered search:

1. **Privacy**: SearxNG doesn't track users or store search history
2. **Diverse Sources**: Aggregates results from multiple search engines
3. **Customization**: Configurable engines, filters, and result formats
4. **Self-hostable**: Can be run on your own infrastructure
5. **Open Source**: Transparent and community-driven

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

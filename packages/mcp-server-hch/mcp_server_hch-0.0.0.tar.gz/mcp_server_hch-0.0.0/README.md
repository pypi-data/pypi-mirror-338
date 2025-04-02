# Home Clean Home MCP Server

## Overview

A Model Context Protocol server for managing residential and commercial cleaning services. This server provides tools to retrieve service details, pricing, and booking requirements dynamically via Large Language Models.

Please note that Home Clean Home MCP Server is currently in active development. The functionality and available tools are subject to change and expansion as we continue to improve the server.

### Tools

#### Residential Services

1. `get_residential_service_general_info`

   - Provides general information about a selected residential cleaning service.
   - Input:
     - `service` (string, required): Select a residential service option from the following:
       - `Detail Cleaning`
       - `Move In Cleaning`
       - `Move Out Cleaning`
       - `Post-Renovation Cleaning`
       - `Spring Cleaning (Occupied Unit)`
       - `Floor Cleaning or Floor Care`
       - `Formaldehyde (VOC)`
       - `Disinfecting`
       - `Household Accessory Cleaning (e.g. Sofa, Mattress, Carpet, Curtains)`
       - `Customised or Combination Cleaning`
   - Returns: General information about the selected service.

2. `get_residential_service_price_info`

   - Provides pricing details for a selected residential cleaning service.
   - Input:
     - `service` (string, required): Same options as above.
   - Returns: Pricing details for the selected service.

3. `get_residential_service_booking_requirements`
   - Lists booking requirements for a selected residential cleaning service.
   - Input:
     - `service` (string, required): Same options as above.
   - Returns: Booking requirements for the selected service.

#### Commercial Services

4. `get_commercial_service_general_info`

   - Provides general information about a selected commercial cleaning service.
   - Input:
     - `service` (string, required): Select a commercial service option from the following:
       - `Commercial Cleaning`
       - `Placeholder Option`
   - Returns: General information about the selected service.

5. `get_commercial_service_price_info`

   - Provides pricing details for a selected commercial cleaning service.
   - Input:
     - `service` (string, required): Same options as above.
   - Returns: Pricing details for the selected service.

6. `get_commercial_service_booking_requirements`
   - Lists booking requirements for a selected commercial cleaning service.
   - Input:
     - `service` (string, required): Same options as above.
   - Returns: Booking requirements for the selected service.

## Installation

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/), no specific installation is needed. Use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run _mcp-server-hch_.

### Using PIP

Alternatively, you can install the server via pip:

```bash
pip install mcp-server-hch
```

After installation, you can run it as a script using:

```bash
python -m mcp_server_hch
```

## Configuration

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

1. Using uv/uvx(if already published to PYPI)

```json
"mcpServers": {
  "mcp-server-hch": {
    "command": "uv",
    "args": [
      "--directory",
      "local_path/to/mcp_server_hch",
      "run",
      "mcp-server-hch"
    ]
  }
}
```

```json
"mcpServers": {
  "mcp-server-hch": {
    "command": "uvx",
    "args": ["mcp-server-hch"]
  }
}
```

2. Using pip installation

```json
"mcpServers": {
  "mcp-server-hch": {
    "command": "python",
    "args": ["-m", "mcp_server_hch"]
  }
}
```

## Debugging

You can use the MCP inspector to debug the server. For uvx installations:

```bash
npx @modelcontextprotocol/inspector uvx mcp-server-hch
```

Or if you've installed the package in a specific directory or are developing locally:

```bash
npx @modelcontextprotocol/inspector uv --directory local_path/to/mcp_server_hch run mcp-server-hch
```

Running `tail -n 20 -f ~/Library/Logs/Claude/mcp*.log` will show the logs from the server and may help you debug any issues.

## Development

If you are doing local development, there are two ways to test your changes:

1. Run the MCP inspector to test your changes. See [Debugging](#debugging) for run instructions.

2. Test using the Claude desktop app. Add the following to your `claude_desktop_config.json`:

```json
"mcpServers": {
  "mcp-server-hch": {
    "command": "uv",
    "args": [
      "--directory",
      "local_path/to/mcp_server_hch",
      "run",
      "mcp-server-hch"
    ]
  }
}
```

## Build and publish to PYPI

To build the project:

```bash
uv sync --dev --all-extras
uv build
```

Publish project to PYPI(required PYPI account for API Token):

```bash
uv publish
```

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

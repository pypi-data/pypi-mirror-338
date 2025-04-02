#!/usr/bin/env python
"""
CLI entry point for MCP-NixOS server.

This handles the top-level execution of the MCP-NixOS server, allowing the FastMCP
framework to manage signal handling and graceful shutdown.
"""

import sys

# Import mcp from server
from mcp_nixos.server import mcp, logger
import os


def main():
    """Run the MCP-NixOS server."""
    # Check if we're running under Windsurf for specific debugging

    windsurf_detected = False
    for env_var in os.environ:
        if "WINDSURF" in env_var.upper() or "WINDSURFER" in env_var.upper():
            windsurf_detected = True
            logger.info(f"Detected Windsurf environment variable: {env_var}={os.environ[env_var]}")

    if windsurf_detected:
        logger.info("Running under Windsurf - monitoring for restart/refresh signals")

    try:
        # Run the server (this is a blocking call)
        logger.info("Starting server main loop")
        mcp.run()
    except KeyboardInterrupt:
        # Handle keyboard interrupt for cleaner exit
        logger.info("Server stopped by keyboard interrupt")
        sys.exit(0)
    except Exception as e:
        # Log unexpected errors and exit with error code
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)


# Expose mcp for entry point script
# This is needed for the "mcp-nixos = "mcp_nixos.__main__:mcp.run" entry point in pyproject.toml

if __name__ == "__main__":
    main()

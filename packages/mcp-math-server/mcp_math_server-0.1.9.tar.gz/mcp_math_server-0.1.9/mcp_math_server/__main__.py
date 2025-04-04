"""Main entry point for MCP Math Server."""
import sys
from mcp_math_server.server import main

if __name__ == "__main__":
    print("🚀 Running mcp_math_server package as main module", file=sys.stderr)
    main()

import argparse
import asyncio
from dataclasses import dataclass

from mcpport.gateway import MCPGateway
from mcpport.utils import setup_logger


@dataclass
class ServerSettings:
    host: str
    port: int
    debug: bool
    log_level: str
    sse_path: str
    message_path: str
    ipv6: bool = False  # Added IPv6 support flag
    timeout_rpc: int = 10
    timeout_run_tool: int = 120


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="MCP Gateway Server")

    # Server configuration
    parser.add_argument(
        "--host",
        type=str,
        default="::",
        help="Host address to bind (default: '::' for both IPv6 and IPv4)",
    )
    parser.add_argument(
        "--port", type=int, default=8765, help="Port to bind (default: 8765)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=True,
        help="Enable debug mode (default: True)",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level (default: INFO)",
    )

    parser.add_argument(
        "--ipv6",
        action="store_true",
        default=True,
        help="Enable dual-stack IPv6/IPv4 support (default: True)",
    )

    parser.add_argument(
        "--timeout-rpc",
        type=int,
        default=10,
        help="Timeout for RPC calls in seconds (default: 10)",
    )
    parser.add_argument(
        "--timeout-run-tool",
        type=int,
        default=120,
        help="Timeout for tool execution in seconds (default: 120)",
    )

    # Path configuration
    parser.add_argument(
        "--sse-path", type=str, default="/sse", help="SSE endpoint path (default: /sse)"
    )
    parser.add_argument(
        "--message-path",
        type=str,
        default="/messages/",
        help="Message endpoint path (default: /messages/)",
    )

    return parser.parse_args()


def main():
    # Parse command line arguments
    args = parse_arguments()

    # Create server settings from arguments
    settings = ServerSettings(
        host=args.host,
        port=args.port,
        debug=args.debug,
        log_level=args.log_level,
        sse_path=args.sse_path,
        message_path=args.message_path,
        ipv6=args.ipv6,
        timeout_rpc=args.timeout_rpc,
        timeout_run_tool=args.timeout_run_tool,
    )

    # Setup logging
    setup_logger(settings.log_level)

    # Create the MCP gateway
    gateway = MCPGateway(
        gateway_host=settings.host, gateway_port=settings.port, settings=settings
    )

    # Start the server (supports both SSE and WebSocket)
    asyncio.run(gateway.run_server())


if __name__ == "__main__":
    main()

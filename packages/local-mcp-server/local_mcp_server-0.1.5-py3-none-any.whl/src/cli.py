import sys
import asyncio
import argparse
from typing import Optional
import logging
from urllib.parse import urlparse

# Import your client modules
from src.client import MCPClient
from src.config import ClientConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("mcp_cli")

def validate_url(url: str) -> bool:
    """Validate if the provided string is a proper URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

async def run_client(url: str, timeout: int = 30) -> None:
    """
    Run the MCP client with proper error handling.
    
    Args:
        url: Server URL to connect to
        timeout: Connection timeout in seconds
    """
    try:
        logger.info(f"Connecting to server at {url}")
        config = ClientConfig(server_url=url)
        # Pass the logger to the MCPClient instance
        client = MCPClient(config, logger=logger)
        
        # Set timeout for the client connection
        await asyncio.wait_for(client.run(), timeout=timeout)
    except asyncio.TimeoutError:
        logger.error(f"Connection timed out after {timeout} seconds")
        sys.exit(1)
    except ConnectionError as e:
        logger.error(f"Failed to connect to server: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """Main entry point with argument parsing and validation."""
    parser = argparse.ArgumentParser(description="MCP Client CLI")
    parser.add_argument(
        "url", 
        help="URL of the MCP server to connect to"
    )
    parser.add_argument(
        "--timeout", 
        type=int, 
        default=30,
        help="Connection timeout in seconds (default: 30)"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Set log level based on verbosity
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Validate URL
    if not args.url:
        logger.error("Server URL must be provided")
        parser.print_help()
        sys.exit(1)
    
    if not validate_url(args.url):
        logger.error(f"Invalid URL format: {args.url}")
        sys.exit(1)
    
    try:
        asyncio.run(run_client(args.url, args.timeout))
    except KeyboardInterrupt:
        logger.info("Client terminated by user")
        sys.exit(0)
from . import server

def main():
    """Main entry point for the package."""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="MCP server to work with Obsidian remotely via REST plugin"
    )
    # Add arguments if needed

    args = parser.parse_args()
    asyncio.run(server.main_async())  # Rename current main to main_async

# Optionally expose other important items at package level
__all__ = ['main', 'server']

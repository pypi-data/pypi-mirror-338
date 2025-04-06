import click
from .server import serve

@click.command()
def main() -> None:
    """RAG MCP Server - RAG functionality for LLM"""
    import asyncio

    asyncio.run(serve("/Users/adityamishra/Documents/liv-doms/sw-liv-oms-parent"))

if __name__ == "__main__":
    main()

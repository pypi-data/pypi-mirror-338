from mcp.server.fastmcp import FastMCP

from youtube_mcp.core import _extractor

mcp = FastMCP("YouTube MCP")

@mcp.tool()
def get_transcript(url: str, languages: str = "ru,en"):
    """Get transcript of YouTube video"""
    return _extractor.process_transcript(url, languages)

@mcp.tool()
def get_languages(url: str):
    """Get languages of YouTube video"""
    return _extractor.list_languages(url)

def main():
    mcp.run()

if __name__ == "__main__":
    main()

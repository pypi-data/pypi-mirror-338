import os
import time
from typing import List

from mcp.server import  FastMCP
from mcp.types import TextContent

from .write_xiaohongshu import XiaohongshuPoster
mcp = FastMCP("xhs")
phone = os.getenv("phone","13336100172")
def login():
    poster = XiaohongshuPoster()
    poster.login(phone)
    time.sleep(1)
    poster.close()

@mcp.tool()
def create_note(title: str, content: str, images: list) -> list[TextContent]:
    """Create a note with title, description, and images"""
    poster = XiaohongshuPoster()
    poster.login(phone)
    res=""
    try:
        poster.post_article(title, content, images)
        poster.close()
        res="success"
    except Exception as e:
        res= "error:"+str(e)

    return [TextContent(type="text", text=res)]
def main():
    mcp.run()
if __name__ == "__main__":
    main()

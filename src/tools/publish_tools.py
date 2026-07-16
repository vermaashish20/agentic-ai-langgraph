import os
from langchain_core.tools import tool

@tool
def save_to_markdown(content: str, filename: str) -> str:
    """Saves the given text content to a local markdown file."""
    print(f"      [Tool Executing] Saving to file: {filename}")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Successfully saved document to {filename}"

@tool
def publish_to_social_media(content: str, platform: str) -> str:
    """Simulates publishing the content to a social media platform like LinkedIn or Twitter."""
    print(f"      [Tool Executing] Publishing to {platform}...")
    return f"Successfully posted to {platform}."

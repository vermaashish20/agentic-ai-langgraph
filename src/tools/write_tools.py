from langchain_core.tools import tool

@tool
def grammar_check(text: str) -> str:
    """Checks the grammar and tone of the provided text."""
    print(f"      [Tool Executing] Checking grammar...")
    return "Grammar check passed. The tone is highly engaging and professional."

@tool
def word_count(text: str) -> int:
    """Returns the word count of the text."""
    print(f"      [Tool Executing] Counting words...")
    return len(text.split())

from langchain_core.tools import tool

@tool
def search_web(query: str) -> str:
    """Searches the web for information about a given topic."""
    print(f"      [Tool Executing] Searching web for: {query}")
    return f"Search results for '{query}': Found detailed company vision and historical background."

@tool
def search_company_database(query: str) -> str:
    """Searches the local company RAG database."""
    print(f"      [Tool Executing] Searching company DB for: {query}")
    return f"Database results for '{query}': Found internal metrics and specific product details."

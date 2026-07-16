from typing import TypedDict, List
from langchain_core.documents import Document

class AgentState(TypedDict):
    """The state of our Simple RAG workflow."""
    question: str
    context: List[Document]
    answer: str

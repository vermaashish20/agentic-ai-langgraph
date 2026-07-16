from langchain_chroma import Chroma
from fastembed import TextEmbedding
from typing import List

# Sample mock documents for our RAG system
mock_documents = [
    "Our company, AgenticAI, was founded in 2026.",
    "Our flagship product is a state-of-the-art workflow orchestrator built on LangGraph.",
    "The vision of the company is to empower businesses to automate their internal processes.",
    "Our latest financial reports indicate a 300% growth in revenue this quarter.",
    "The technical stack heavily relies on Python, LangChain, and NVIDIA endpoints."
]

class FastEmbedWrapper:
    """Wrapper to make fastembed compatible with LangChain's Chroma expectations."""
    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        self.model = TextEmbedding(model_name=model_name)
        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return list(self.model.embed(texts))
        
    def embed_query(self, text: str) -> List[float]:
        return list(self.model.embed([text]))[0]

def build_vector_store():
    """Initializes the Chroma vector store with FastEmbed Embeddings."""
    print("--- 📚 BUILDING IN-MEMORY CHROMA VECTOR STORE ---")
    
    # Initialize the FastEmbed model wrapper
    embeddings = FastEmbedWrapper(model_name="BAAI/bge-small-en-v1.5")
    
    # Create the vector store from our mock texts (in-memory)
    vectorstore = Chroma.from_texts(mock_documents, embedding=embeddings)
    return vectorstore

# Create a global singleton instance to be used across the application
vectorstore = build_vector_store()

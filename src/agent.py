"""
Simple RAG Workflow using LangGraph and LangChain.
This workflow follows a linear pipeline: Retrieve -> Generate
"""

from langgraph.graph import StateGraph, START, END
from langchain_core.messages import SystemMessage, HumanMessage

from state import AgentState
from llm import llm
from vectordb.rag import retriever

def retrieve_node(state: AgentState):
    """Retrieves relevant documents from the vector store."""
    print("--- 🔍 RETRIEVE NODE: Fetching context ---")
    question = state["question"]
    
    # Query the retriever
    docs = retriever.invoke(question)
    
    print(f"    -> Found {len(docs)} relevant documents.")
    return {"context": docs}

def generate_node(state: AgentState):
    """Generates an answer using the retrieved context."""
    print("--- ✍️ GENERATE NODE: Writing answer ---")
    question = state["question"]
    context_docs = state.get("context", [])
    
    # Format the retrieved documents into a single string
    context_str = "\n\n".join([doc.page_content for doc in context_docs])
    
    sys_msg = SystemMessage(
        content=(
            "You are a helpful assistant. Use the following context to answer the user's question.\n"
            "If the answer is not in the context, simply say you don't know.\n\n"
            f"Context:\n{context_str}"
        )
    )
    user_msg = HumanMessage(content=question)
    
    # Invoke the central LLM
    response = llm.invoke([sys_msg, user_msg])
    
    return {"answer": response.content}

# --- Build the Graph ---
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)

# Set up the linear edges
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Compile the graph
app = workflow.compile()

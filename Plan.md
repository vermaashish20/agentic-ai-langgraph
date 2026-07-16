# Simple RAG System using LangGraph

## Goal Description
We will implement a standard Retrieval-Augmented Generation (RAG) system using LangChain for the components (Vector Store, Embeddings, Prompts) and LangGraph for the workflow orchestration.

Since all previous agentic files have been removed, we will build a clean, straightforward Retrieve -> Generate pipeline.

## Proposed Architecture

1. **State Definition (`AgentState`)**:
   - `question`: The user's query.
   - `context`: The documents retrieved from the vector database.
   - `answer`: The final generated answer.

2. **Vector Database (`src/vectordb/`)**:
   - `embed.py`: Logic to ingest sample documents, create embeddings (using NVIDIA embeddings), and store them in a local in-memory vector store (like FAISS or Chroma).
   - `rag.py`: Exposes a `retriever` instance that can be used by the graph.

3. **LangGraph Workflow (`src/agent.py`)**:
   - `retrieve_node`: Takes the user's `question`, calls the retriever, and populates the `context`.
   - `generate_node`: Takes the `question` and `context`, uses the central `llm` from `llm.py`, and generates the `answer`.
   - **Graph Edge Flow**: `START` -> `retrieve_node` -> `generate_node` -> `END`.

---

## File Structure

```text
src/
├── vectordb/               
│   ├── embed.py            # Initializes the vector store with dummy data
│   └── rag.py              # Exposes the retriever
├── llm.py                  # (Existing) Central ChatNVIDIA LLM
└── agent.py                # LangGraph StateGraph, Nodes, and Compilation
langgraph.json              # LangGraph Studio Configuration
```

> [!IMPORTANT] 
> **User Review Required**
> 1. **Vector Store**: Is it okay if I use **FAISS** (`langchain-community`, `faiss-cpu`) as a simple, fast local vector store for this RAG demo?
> 2. **Embeddings**: Since we are using `ChatNVIDIA`, I plan to use `NVIDIAEmbeddings` for generating vector embeddings. Is that acceptable, or would you prefer a free local alternative like HuggingFace embeddings?

Please approve this plan and I will begin the implementation!

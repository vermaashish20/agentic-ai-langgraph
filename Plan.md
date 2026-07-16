# Content Creation & Management Agentic System Plan

## Goal Description
We will build a comprehensive **Content Creation and Management System** utilizing three primary roles:
1. **Researcher**: Gathers information from the web or a local RAG database (company details, vision, etc.) and compiles a comprehensive report.
2. **Writer**: Consumes the research report to write targeted content (blogs, social media posts, etc.) based on the user's request.
3. **Publisher**: Takes the final written content and publishes it to various mediums (Instagram, Facebook, LinkedIn, CRM, or local Markdown files).

---

## Branching Strategy & Architectures

To keep the codebase clean, we will implement the four different architectures across four separate Git branches. Each branch will have its own dedicated file structure suited for that specific architecture.

1. **Branch: `langgraph-workflow` (CURRENT BRANCH)**
   - **Architecture**: LangGraph Workflow (Router Pattern).
   - **Focus**: A directed graph where a router node evaluates the user's request and routes to specific worker nodes (`researcher`, `writer`, `publisher`).
   - **File Structure**: Organized by nodes (`src/nodes/`) and vector db logic (`src/vectordb/`), tied together in `src/agent.py`.

2. **Branch: `langchain-workflow`**
   - **Architecture**: LangChain Sequential Chain.
   - **Focus**: A rigid sequence (`RunnableSequence`) executing the steps in a straight line.
   - **File Structure**: Will be refactored to emphasize linear chains instead of nodes.

3. **Branch: `langchain-agent`**
   - **Architecture**: LangChain Agent with Tools.
   - **Focus**: A central LLM agent empowered with `ResearchTool`, `WriteTool`, and `PublishTool` to dynamically decide its path.
   - **File Structure**: Will be refactored to focus on a central `agent.py` and a `src/tools/` directory.

4. **Branch: `langgraph-agent`**
   - **Architecture**: LangGraph Agentic/Supervisor.
   - **Focus**: A supervisor node in LangGraph that delegates to specialized agent nodes or tool nodes.
   - **File Structure**: Will include multi-agent definitions and a `tools` directory integrated via `ToolNode`.

---

## Implementation Plan for Current Branch (`langgraph-workflow`)

For this current branch, we will build the **LangGraph Workflow** using the existing file system.

```text
src/
├── vectordb/               # RAG Database and Embedding logic
│   ├── rag.py
│   └── embed.py
├── nodes/                  # LangGraph Worker Nodes
│   ├── researcher.py
│   ├── writer.py
│   └── publisher.py
├── state.py                # Shared AgentState definitions
└── agent.py                # LangGraph Router and Graph Compilation
langgraph.json              # LangGraph Studio Configuration
```

> [!IMPORTANT] 
> **User Review Required**
> 1. **RAG Database**: Should we use an in-memory vector store (like FAISS or Chroma) with mock data for the `vectordb` module?
> 2. **Publisher**: For the initial implementation, should we simulate publishing by writing the final output to a local Markdown file?

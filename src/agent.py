"""
Router-Based LangGraph Workflow
This workflow uses a central LLM "supervisor" to decide the flow of execution between
different agent nodes (researcher, writer, publisher).
"""

from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, START, END

from state import AgentState
from llm import llm
from nodes.researcher import research_node
from nodes.writer import write_node
from nodes.publisher import publish_node

def supervisor_node(state: AgentState):
    """The router that decides who should act next."""
    print("--- 🧠 SUPERVISOR: Deciding next step ---")
    
    # We provide a strict prompt so it only responds with the exact node name
    system_prompt = (
        "You are a supervisor managing a content creation workflow. "
        "Based on the task and current progress, decide who should act next.\n"
        "Respond strictly with ONE WORD ONLY, choosing from: researcher, writer, publisher, FINISH.\n"
        "- Choose 'researcher' if research data is missing.\n"
        "- Choose 'writer' if research is done but content is not written.\n"
        "- Choose 'publisher' if content is written but not published.\n"
        "- Choose 'FINISH' if the content has been successfully published."
    )
    
    # We just feed it the system prompt and whatever messages have accumulated
    messages = [SystemMessage(content=system_prompt)] + state.get("messages", [])
    response = llm.invoke(messages)
    
    # Parse the LLM's decision robustly
    decision = response.content.strip().lower()
    if "researcher" in decision: 
        next_node = "researcher"
    elif "writer" in decision: 
        next_node = "writer"
    elif "publisher" in decision: 
        next_node = "publisher"
    else: 
        next_node = "FINISH"
        
    print(f"    -> Routing to: {next_node.upper()}")
    return {"next_node": next_node}

def router_function(state: AgentState):
    """The conditional routing function for the graph."""
    next_node = state.get("next_node")
    if next_node == "FINISH":
        return END
    return next_node

# --- Build the Graph ---
workflow = StateGraph(AgentState)

# Add all nodes
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("researcher", research_node)
workflow.add_node("writer", write_node)
workflow.add_node("publisher", publish_node)

# Set entry point
workflow.add_edge(START, "supervisor")

# The supervisor dynamically decides where to go
workflow.add_conditional_edges(
    "supervisor",
    router_function,
    {
        "researcher": "researcher", 
        "writer": "writer", 
        "publisher": "publisher", 
        END: END
    }
)

# All workers report back to the supervisor when they are done
workflow.add_edge("researcher", "supervisor")
workflow.add_edge("writer", "supervisor")
workflow.add_edge("publisher", "supervisor")

# Compile the graph
app = workflow.compile()

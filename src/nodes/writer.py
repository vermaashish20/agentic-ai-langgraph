from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent
from state import AgentState
from llm import llm
from tools.write_tools import grammar_check, word_count

# Create a sub-agent with tools
write_agent = create_react_agent(llm, tools=[grammar_check, word_count])

def write_node(state: AgentState):
    """Writes the final content using tools."""
    print("--- ✍️ WRITER: Drafting content ---")
    task = state.get("task", "")
    research_data = state.get("research_data", "No research provided.")
    
    sys_msg = "You are an expert content writer. Write highly engaging content based ONLY on the provided research. Use your tools to check grammar and word count."
    user_msg = f"Task: {task}\n\nResearch Data:\n{research_data}\n\nPlease write the final content."
    
    # Run the sub-agent
    result = write_agent.invoke({"messages": [SystemMessage(content=sys_msg), HumanMessage(content=user_msg)]})
    final_content = result["messages"][-1].content
    
    return {
        "content": final_content, 
        "messages": [SystemMessage(content=f"Draft completed successfully.")]
    }
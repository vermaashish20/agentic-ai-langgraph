from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent
from state import AgentState
from llm import llm
from tools.research_tools import search_web, search_company_database

# Create a sub-agent with tools
research_agent = create_react_agent(llm, tools=[search_web, search_company_database])

def research_node(state: AgentState):
    """Gathers information using research tools."""
    print("--- 🔍 RESEARCHER: Gathering facts ---")
    task = state.get("task", "")
    
    sys_msg = "You are an expert researcher. Use your tools to gather facts and create a comprehensive report."
    user_msg = f"Topic to research: {task}"
    
    # Run the sub-agent
    result = research_agent.invoke({"messages": [SystemMessage(content=sys_msg), HumanMessage(content=user_msg)]})
    final_report = result["messages"][-1].content
    
    return {
        "research_data": final_report,
        "messages": [SystemMessage(content=f"Research completed successfully.")]
    }

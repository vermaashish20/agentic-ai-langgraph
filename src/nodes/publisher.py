from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent
from state import AgentState
from llm import llm
from tools.publish_tools import save_to_markdown, publish_to_social_media

# Create a sub-agent with tools
publish_agent = create_react_agent(llm, tools=[save_to_markdown, publish_to_social_media])

def publish_node(state: AgentState):
    """Simulates publishing using tools."""
    print("--- 🚀 PUBLISHER: Distributing content ---")
    content = state.get("content", "")
    task = state.get("task", "untitled")
    
    # Create a safe filename from the task name
    filename = "".join(c if c.isalnum() else "_" for c in task[:20]) + "_post.md"
    
    sys_msg = "You are an expert publisher. Use your tools to save the content to a markdown file and publish it to social media."
    user_msg = f"Save the following content to {filename} and simulate publishing it to LinkedIn:\n\n{content}"
    
    # Run the sub-agent
    result = publish_agent.invoke({"messages": [SystemMessage(content=sys_msg), HumanMessage(content=user_msg)]})
    status = result["messages"][-1].content
    
    print(f"    -> Publisher Finished")
    
    return {
        "publish_status": status, 
        "messages": [SystemMessage(content=status)]
    }
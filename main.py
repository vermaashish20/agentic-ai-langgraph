"""
Main entry point for testing the LangChain Agent
"""
import os
import sys
from langchain_core.messages import HumanMessage

# Add the project root to python path to resolve src modules correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.agent import app

def main():
    print("--- 🤖 Starting LangChain Agent ---")
    task = "Research the latest company metrics from the internal database, write a short summary of them, and save it to 'metrics_summary.md'"
    
    print(f"Task: {task}\n")
    
    # create_react_agent expects a state dict with messages
    response = app.invoke({"messages": [HumanMessage(content=task)]})
    
    print("\n--- ✅ Final Result ---")
    # The final message in the state contains the agent's response
    print(response["messages"][-1].content)

if __name__ == "__main__":
    main()

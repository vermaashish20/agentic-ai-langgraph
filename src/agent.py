"""
LangChain Agentic Workflow
This replaces the manual LangGraph state graph with a prebuilt ReAct agent
that has access to all tools.
"""

from langchain.agents import create_agent
# pyrefly: ignore [missing-import]
from src.llm import llm

# Import all tools
# pyrefly: ignore [missing-import]
from src.tools.research_tools import search_web, search_company_database
# pyrefly: ignore [missing-import]
from src.tools.write_tools import grammar_check, word_count
# pyrefly: ignore [missing-import]
from src.tools.publish_tools import save_to_markdown, publish_to_social_media

tools = [
    search_web,
    search_company_database,
    grammar_check,
    word_count,
    save_to_markdown,
    publish_to_social_media,
]

system_prompt = (
    "You are a helpful and intelligent AI assistant responsible for researching, "
    "writing, and publishing content. You have access to various tools to help you "
    "accomplish your tasks. Use them when necessary to provide accurate and "
    "comprehensive results. When asked to save to a file or publish, use the appropriate tools."
)

# Create the agent
app = create_agent(llm, tools=tools, system_prompt=system_prompt)

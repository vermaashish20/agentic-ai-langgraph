import operator
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    """The global state of our content creation workflow."""
    messages: Annotated[list[BaseMessage], operator.add]
    task: str
    research_data: str
    content: str
    publish_status: str
    next_node: str
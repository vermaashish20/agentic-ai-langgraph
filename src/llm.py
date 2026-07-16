from langchain_nvidia_ai_endpoints import ChatNVIDIA

# Centralized LLM instance used across the entire graph
llm = ChatNVIDIA(model="nvidia/nemotron-3-ultra-550b-a55b")

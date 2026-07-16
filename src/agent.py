"""
Build the graph with multiple agents/tools/llm nodes with Routing node here
[for invocation use different file to call this graph/agent workflow with user prompt]

To build the Multi-Agent system we have to use different pattern depending on NEED:[for not prefer Routing]
- Routing : most easy, a LLM says which agent to Invoke next -> a Router Node then executes the agent Graph/Node and goes to next LLM call
- SubGraph : sub agents of a Parent Agent , parent agent invokes the subagent -> subagents does work and respond to parent agent
- HandsOff : just invoke different agent based on a variable state (if LLM said, agent A done -> now as per logic invokes the agent B)
- 

As our is simple : 
user query -> LLM Node decides which to invoke-> router Node execute the Agent node -> invokes Agent A/B/C  -> goes back to LLM Node decides what to use.
thus its subagent but with simplification, agents stays at same level of Hierarchy.

We are building here Agent
---

WorkFlow vs Agent
Workflows have predefined paths to go -> LLM invokes a certain agent in as per defined. Researcher First -> writer -> publisher.
path is decided (could be cyclic/loop or simple or Dag) but overall flow is predefined.

Agentic AI: all agents are acts as Tools to LLM and LLM decides what to invoke or what to use.
  AgentA : Task it does(boundries) + tools it has
  AgentB : Task it does + tools it has
  WeatherAgent : task it does + tools it has [here agent is simple a tool or API call nothing complex] but When to use this is Entirely on LLM. 


Langchain provides Higher level things to build both of them  
Agent: [ create agent mostly ReAct--main one , add tools-here a agent can be tool also, pass all tools to agent ]
WorkFlow : using chains concept , pass one agent output to other chains in a predefined path

LangGraph provides fine controlled level to do this with cusomization. 
Agent: Main Agent with Global State-> create Agents as Nodes with thier tools -> make these agentsA,B,.. as tool for Main Agent to decide when to use. Issue is everything get a bit complicated a bit due to State/HITL,nested tools etc.
WorkFlow : Main Agent /LLm + Router Node -> create Agents as Nodes with their tools -> add them as per Flow in Main Graph with router node/conditional edges 

"""


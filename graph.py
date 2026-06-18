from langgraph.graph import StateGraph, START, END
from state import AgentState

def planner(state):
    return {
        "response": f"Planning task: {state['command']}"
    }


graph = StateGraph(AgentState)

graph.add_node('planner', planner)

graph.add_edge(START, 'planner')
graph.add_edge('planner', END)

app = graph.compile()


result = app.invoke({
    "command": "hello"})

print(result)
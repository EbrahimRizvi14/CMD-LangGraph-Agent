from langgraph.graph import StateGraph, START, END
from state import AgentState
from groq import Groq
from utils import read_file
from dotenv import load_dotenv
import subprocess

load_dotenv()

client = Groq()

def readFileNode(state):
    parts = state["command"].split(maxsplit=1)

    if len(parts) < 2:
        return {"response": "No file specified"}
    
    return {
        "response": read_file(parts[1].strip())
    }

def chatNode(state):

    completion = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[{"role": "user", "content": state["command"]}]
        )

    return {"response": completion.choices[0].message.content}

def runShellNode(state):
    try:
        result = subprocess.run(
            state["command"][4:].strip(),
            shell=True,
            capture_output=True,
            text=True
        )
        return {"response": result.stdout}
    
    except Exception as e:
        return {"response": f"Error occurred: {str(e)}"}

def planner(state):
    command = state["command"].lower()

    if command.startswith("read "):
        return {"action": "read_file"}
    
    elif command.startswith("run "):
        return {"action": "run_shell"}

    return {"action": "chat"}


def executor(state):
    if state['action'] == "read_file":

        return readFileNode(state)
    
    elif state['action'] == "chat":

        return chatNode(state)

    elif state['action'] == "run_shell":
        return runShellNode(state)

    else:
        return {
    "response": f"Unknown action: {state['action']}"
            }
    
    
graph = StateGraph(AgentState)

graph.add_node('planner', planner)
graph.add_node('executor', executor)

graph.add_edge(START, 'planner')
graph.add_edge('planner', 'executor')
graph.add_edge('executor', END)

app = graph.compile()


result = app.invoke({
    "command": "hello"})

if __name__ == "__main__":
    print(result)
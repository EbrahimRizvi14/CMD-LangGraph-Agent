from typing import TypedDict

class AgentState(TypedDict):
    command: str
    action: str
    response: str
    error: str
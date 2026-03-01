from typing import TypedDict

class AgentState(TypedDict):
    topic: str
    research: str
    report: str
    next_step: str
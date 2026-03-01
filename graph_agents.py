from graph_state import AgentState
from research_agent import run_research_agent
from writer_agent import run_writer_agent

def researcher_node(state: AgentState) -> dict:
    print(f"\n🔍 Researcher node: researching '{state['topic']}'...")
    result = run_research_agent(state["topic"])
    return {"research": result}

def writer_node(state: AgentState) -> dict:
    print(f"\n✍️  Writer node: writing report...")
    result = run_writer_agent(state["topic"], state["research"])
    return {"report": result}
from langgraph.graph import StateGraph, END
from graph_state import AgentState
from graph_supervisor import supervisor_node
from graph_agents import researcher_node, writer_node
from dotenv import load_dotenv

load_dotenv()

def build_graph():
    # Create the graph
    graph = StateGraph(AgentState)
    
    # Add nodes
    graph.add_node("supervisor", supervisor_node)
    graph.add_node("researcher", researcher_node)
    graph.add_node("writer", writer_node)
    
    # Fixed edges - always report back to supervisor
    graph.add_edge("researcher", "supervisor")
    graph.add_edge("writer", "supervisor")
    
    # Conditional edge - supervisor decides what to do next
    graph.add_conditional_edges(
        "supervisor",
        lambda state: state["next_step"],
        {
            "research": "researcher",
            "write": "writer",
            "end": END
        }
    )
    
    # Start with supervisor
    graph.set_entry_point("supervisor")
    
    return graph.compile()

def run_dynamic_supervisor(topic: str) -> str:
    print(f"\n🧠 Dynamic Supervisor: starting graph for '{topic}'...")
    
    app = build_graph()
    
    initial_state = AgentState(
        topic=topic,
        research="",
        report="",
        next_step=""
    )
    
    final_state = app.invoke(initial_state)
    return final_state["report"]
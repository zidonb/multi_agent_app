from research_agent import run_research_agent
from writer_agent import run_writer_agent

def run_supervisor(topic: str) -> str:
    print(f"\n🔍 Supervisor: Starting research on '{topic}'...")
    research_result = run_research_agent(topic)
    
    print(f"\n✍️ Supervisor: Research complete. Handing off to writer...")
    final_report = run_writer_agent(topic, research_result)
    
    print(f"\n✅ Supervisor: Report complete.\n")
    return final_report

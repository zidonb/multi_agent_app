from parallel_research_agent import run_research_agent_async
from writer_agent import run_writer_agent
import asyncio

async def run_parallel_supervisor(topics: list) -> str:
    print(f"\n🚀 Parallel Supervisor: Launching {len(topics)} research agents simultaneously...")
    
    # Run all research agents at the same time
    research_tasks = [run_research_agent_async(topic) for topic in topics]
    research_results = await asyncio.gather(*research_tasks)
    
    print(f"\n✍️  All research complete. Handing off to writer...")
    
    # Combine all research into one block
    combined_research = ""
    for result in research_results:
        combined_research += f"\n## {result['topic'].upper()}\n{result['research']}\n"
    
    final_report = run_writer_agent(", ".join(topics), combined_research)
    
    print(f"\n✅ Supervisor: Report complete.\n")
    return final_report
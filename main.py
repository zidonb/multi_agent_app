from supervisor import run_supervisor
from parallel_supervisor import run_parallel_supervisor
from dynamic_supervisor import run_dynamic_supervisor
from lcel_chain import run_facts_chain
from dotenv import load_dotenv
import asyncio

load_dotenv()

def main():
    print("🤖 Multi-Agent Research & Writing System")
    print("==========================================")
    print("Modes:")
    print("  1. Sequential  - research one topic deeply")
    print("  2. Parallel    - research multiple topics simultaneously")
    print("  3. Dynamic     - LLM supervised orchestration")
    print("  4. LCEL Chain  - simple fact generation pipeline")
    print("==========================================")
    
    mode = input("Choose mode (1, 2, 3 or 4): ").strip()
    
    if mode == "1":
        topic = input("Enter a topic to research (e.g. tesla, openai): ").strip()
        report = run_supervisor(topic)
        
    elif mode == "2":
        print("Enter topics separated by commas (e.g. tesla, apple, microsoft):")
        raw = input("> ").strip()
        topics = [t.strip() for t in raw.split(",")]
        report = asyncio.run(run_parallel_supervisor(topics))
        
    elif mode == "3":
        topic = input("Enter a topic to research (e.g. tesla, openai): ").strip()
        report = run_dynamic_supervisor(topic)
        
    elif mode == "4":
        topic = input("Enter a topic for facts (e.g. tesla, openai): ").strip()
        report = run_facts_chain(topic)
        
    else:
        print("Invalid choice.")
        return
    
    print("==========================================")
    print("📄 OUTPUT:")
    print("==========================================")
    print(report)

if __name__ == "__main__":
    main()
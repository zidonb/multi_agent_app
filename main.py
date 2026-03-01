from supervisor import run_supervisor
from parallel_supervisor import run_parallel_supervisor
from dynamic_supervisor import run_dynamic_supervisor
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
    print("==========================================")
    
    mode = input("Choose mode (1, 2 or 3): ").strip()
    
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
        
    else:
        print("Invalid choice.")
        return
    
    print("==========================================")
    print("📄 FINAL REPORT:")
    print("==========================================")
    print(report)

if __name__ == "__main__":
    main()
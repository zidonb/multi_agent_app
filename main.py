from supervisor import run_supervisor
from parallel_supervisor import run_parallel_supervisor
from dotenv import load_dotenv
import asyncio

load_dotenv()

def main():
    print("🤖 Multi-Agent Research & Writing System")
    print("==========================================")
    print("Modes:")
    print("  1. Sequential - research one topic deeply")
    print("  2. Parallel   - research multiple topics simultaneously")
    print("==========================================")
    
    mode = input("Choose mode (1 or 2): ").strip()
    
    if mode == "1":
        topic = input("Enter a topic to research (e.g. tesla, openai): ").strip()
        report = run_supervisor(topic)
        
    elif mode == "2":
        print("Enter topics separated by commas (e.g. tesla, apple, microsoft):")
        raw = input("> ").strip()
        topics = [t.strip() for t in raw.split(",")]
        report = asyncio.run(run_parallel_supervisor(topics))
        
    else:
        print("Invalid choice.")
        return
    
    print("==========================================")
    print("📄 FINAL REPORT:")
    print("==========================================")
    print(report)

if __name__ == "__main__":
    main()
from supervisor import run_supervisor
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🤖 Multi-Agent Research & Writing System")
    print("==========================================")
    topic = input("Enter a topic to research (e.g. tesla, openai): ")
    report = run_supervisor(topic)
    print("==========================================")
    print("📄 FINAL REPORT:")
    print("==========================================")
    print(report)

if __name__ == "__main__":
    main()

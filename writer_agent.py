from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

def run_writer_agent(topic: str, research: str) -> str:
    llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0.7)
    
    messages = [
        SystemMessage(content="""You are a professional report writer. 
        Your job is to take research notes and turn them into a clear, 
        structured short report with a title, summary, and key facts."""),
        HumanMessage(content=f"Topic: {topic}\n\nResearch notes:\n{research}\n\nPlease write a short report.")
    ]
    
    response = llm.invoke(messages)
    return response.content

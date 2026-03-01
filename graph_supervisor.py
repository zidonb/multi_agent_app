from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage
from graph_state import AgentState
from dotenv import load_dotenv
import json

load_dotenv()

def supervisor_node(state: AgentState) -> dict:
    llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
    
    messages = [
        SystemMessage(content="""You are a supervisor managing a research and writing pipeline.
        You have two agents available:
        - researcher: searches for information about a topic
        - writer: writes a report based on research
        
        Based on the current state, decide what to do next.
        You must respond with ONLY a JSON object in this exact format:
        {"next_step": "research"} or {"next_step": "write"} or {"next_step": "end"}
        
        Rules:
        - If research is empty, always do research first
        - If research is done but report is empty, do write
        - If both research and report are done, return end
        """),
        HumanMessage(content=f"""Current state:
        Topic: {state['topic']}
        Research done: {'Yes - ' + state['research'][:100] if state['research'] else 'No'}
        Report done: {'Yes' if state['report'] else 'No'}
        
        What should we do next?""")
    ]
    
    response = llm.invoke(messages)
    decision = json.loads(response.content)
    return {"next_step": decision["next_step"]}
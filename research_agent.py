from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain.tools import tool
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

@tool
def search_topic(query: str) -> str:
    """Search for information about a given topic."""
    mock_data = {
        "tesla": "Tesla was founded in 2003. It makes electric vehicles and energy products. CEO is Elon Musk. Main competitors are Rivian, Ford, and GM.",
        "openai": "OpenAI was founded in 2015. It created ChatGPT and GPT-4. It is backed by Microsoft. Main products are the GPT API and ChatGPT.",
    }
    query_lower = query.lower()
    for key in mock_data:
        if key in query_lower:
            return mock_data[key]
    return f"No specific data found for '{query}'. General topic noted."

def run_research_agent(topic: str) -> str:
    llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
    tools = [search_topic]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=2)
    result = executor.invoke({"input": f"Research the following topic: {topic}"})
    return result["output"]

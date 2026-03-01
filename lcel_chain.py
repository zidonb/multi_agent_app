from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def build_facts_chain():
    # Step 1 - the prompt template
    prompt = ChatPromptTemplate.from_template("""
    You are a knowledgeable assistant.
    Generate exactly 3 interesting facts about: {topic}
    Format them as a numbered list.
    """)
    
    # Step 2 - the model
    llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0.7)
    
    # Step 3 - the output parser
    parser = StrOutputParser()
    
    # LCEL - compose them into a chain with pipe syntax
    chain = prompt | llm | parser
    
    return chain

def run_facts_chain(topic: str) -> str:
    chain = build_facts_chain()
    print(f"\n⛓️  LCEL Chain: generating facts about '{topic}'...")
    result = chain.invoke({"topic": topic})
    return result
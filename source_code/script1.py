from crewai import Agent, LLM
# from crewai_tools import tool 
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import os

# tool -1
@tool("DuckDuckGoSearch")
def DuckDuckGo_Search(query: str):
    """Search the web for information on a given topic."""
    return DuckDuckGoSearchRun().run(query)
# ollama llm
ollama_llm = LLM(model="ollama/llama3.2:3b",base_url="http://localhost:11434")

# Create an agent
researcher = Agent(
    role="AI Technology Researcher",
    goal="Research the latest AI developments",
    backstory="You are an expert AI researcher who tracks the newest breakthroughs in artificial intelligence and language models.",
    tools=[DuckDuckGo_Search],
    llm=ollama_llm,
    verbose=True,
    max_iter = 10,
    max_execution_time=60
)

# Use kickoff() to interact directly with the agent
result = researcher.kickoff("What are the latest developments in language models?")

# Access the raw response
print(result.raw)
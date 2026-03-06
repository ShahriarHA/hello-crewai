# Agent + Task
from crewai import Agent, Task, LLM, Crew
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool



# tool 1
@tool("DuckDuckGoSearch")
def DuckDuck_Go_Search(query: str):
    """Search the web for information on a given topic."""
    return DuckDuckGoSearchRun().run(query)

llm_ = LLM(model="ollama/llama3.2:3b",base_url="http://localhost:11434")

researcher_agent = Agent(
    role="AI Technology Researcher",
    goal="Research the latest AI developments",
    backstory="You are an expert AI researcher who tracks the newest breakthroughs in artificial intelligence and language models.",
    llm=llm_,
    tools = [DuckDuck_Go_Search],
    verbose=True,
    max_iter=5,
    max_execution_time=300
)

researcher_task = Task(
    description="Identify the top 3 AI news stories from this week using one search query and summarize them.",
    expected_output="A bullet list summary of the top 5 most important AI news",
    agent=researcher_agent
)

crew_ = Crew(
    agents=[researcher_agent],
    tasks=[researcher_task],
    verbose=True
)

result = crew_.kickoff()

task_output = researcher_task.output

print(f"task description: {task_output.description}")
print(f"task raw output: {task_output.raw}")




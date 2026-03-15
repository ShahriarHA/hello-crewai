# Blog content generator agent

from crewai import Crew,Agent,Task,Process,LLM
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str

llm = LLM(model="ollama/llama3.2:3b",base_url="http://localhost:11434")

blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=False,
    max_iter = 5,
    max_execution_time=300,
    llm = llm,

)

blog_task = Task(
    description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
    expected_output="A compelling blog title and well-written content.",
    agent=blog_agent,
    markdown=True,
    output_pydantic=Blog,
    guardrail="""
    Content must:
    - under 200 words.
    - bold important words.
    - title would be italic format.
"""
)

crew_ = Crew(
    agents=[blog_agent],
    tasks=[blog_task],
    verbose=True,
    process=Process.sequential

)

result = crew_.kickoff()

print("Accessing Properties - Option 1")
title = result["title"]
content = result["content"]
print("Title:", title)
print("Content:", content)




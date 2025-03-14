from agno.agent.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an assistant. Please reply based on the user queries",
    markdown=True,
    tools=[DuckDuckGoTools()]
)

agent.print_response("Can you summarize cricket champions trophy 2025 final match?",stream=True)
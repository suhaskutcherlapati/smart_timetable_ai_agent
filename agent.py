import os
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from calendar_tools.create_event import create_event
from calendar_tools.view_events import get_events
from dotenv import load_dotenv
load_dotenv()
print("API KEY:", os.getenv("OPENAI_API_KEY"))

def get_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
    
    )
    tools = [create_calendar_event, view_calendar_events]

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent


@tool
def create_calendar_event(text: str):
    """Create a calendar event from natural language input."""
    return create_event(text)


@tool
def view_calendar_events(text: str):
    """View all upcoming events."""
    return get_events()


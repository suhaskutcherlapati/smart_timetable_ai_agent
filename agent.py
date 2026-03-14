from langchain.tools import tool
from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI

from calendar_tools.create_event import create_event
from calendar_tools.view_events import get_events


@tool
def create_calendar_event(text: str):
    """Create a calendar event."""
    return "Event created"


@tool
def view_calendar_events(text: str):
    """View upcoming events."""
    return get_events()


def get_agent():

    llm = ChatOpenAI(
        temperature=0
    )

    tools = [
        create_calendar_event,
        view_calendar_events
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    return agent
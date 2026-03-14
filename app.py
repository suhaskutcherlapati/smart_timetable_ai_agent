import streamlit as st
from calendar_tools.create_event import create_event
from calendar_tools.view_events import get_events
from agent.agent import get_agent

st.title("AI Student Calendar Agent")

menu = st.sidebar.selectbox(
    "Menu",
    ["View Events", "Create Event", "AI Assistant"]
)

if menu == "View Events":

    st.header("Upcoming Events")

    events = get_events()

    for e in events:
        st.write(e)


elif menu == "Create Event":

    st.header("Add Event")

    title = st.text_input("Event Title")

    start = st.text_input("Start Time (2026-03-10T10:00:00)")
    end = st.text_input("End Time (2026-03-10T11:00:00)")

    if st.button("Create"):

        link = create_event(title, start, end)

        st.success("Event Created")
        st.write(link)


elif menu == "AI Assistant":

    agent = get_agent()

    query = st.text_input("Ask AI")

    if st.button("Run"):

        response = agent.run(query)

        st.write(response)
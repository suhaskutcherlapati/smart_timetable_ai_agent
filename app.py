import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your modules
from agent.agent import get_agent
from calendar_tools.create_event import create_event
from calendar_tools.view_events import get_events
from calendar_tools.course_schedule import add_class, view_classes
from calendar_tools.assignments import add_assignment, view_assignments
from calendar_tools.study_planner import create_study_plan, study_with_breaks

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Smart Timetable", layout="wide")

st.title("📅 AI Smart Timetable Assistant")

# Sidebar menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Choose Feature",
    ["AI Assistant", "Events", "Classes", "Assignments", "Study Planner"]
)

# -----------------------------
# 1. AI ASSISTANT
# -----------------------------
if option == "AI Assistant":
    st.header("🤖 AI Assistant")

    agent = get_agent()

    query = st.text_input("Ask something (e.g., Schedule meeting tomorrow at 3pm)")

    if st.button("Run"):
        if query:
            response = agent.run(query)
            st.success(response)
        else:
            st.warning("Please enter a query")

# -----------------------------
# 2. EVENTS (Week 1–2)
# -----------------------------
elif option == "Events":
    st.header("📅 Event Manager")

    event_text = st.text_input("Enter event (e.g., Meeting tomorrow at 5pm)")

    if st.button("Add Event"):
        result = create_event(event_text)
        st.success(result)

    if st.button("View Events"):
        events = get_events()
        st.write(events)

# -----------------------------
# 3. CLASSES (Week 5)
# -----------------------------
elif option == "Classes":
    st.header("🎓 Class Scheduler")

    title = st.text_input("Subject Name")
    day = st.text_input("Day (e.g., Monday)")
    time = st.text_input("Time (e.g., 10 AM)")
    type_class = st.selectbox("Type", ["Lecture", "Lab", "Tutorial"])

    if st.button("Add Class"):
        result = add_class(title, day, time, type_class)
        st.success(result)

    if st.button("View Classes"):
        classes = view_classes()
        st.write(classes)

# -----------------------------
# 4. ASSIGNMENTS (Week 5)
# -----------------------------
elif option == "Assignments":
    st.header("📝 Assignment Tracker")

    title = st.text_input("Assignment Title")
    deadline = st.date_input("Deadline")
    priority = st.selectbox("Priority", [1, 2, 3])

    if st.button("Add Assignment"):
        result = add_assignment(title, str(deadline), priority)
        st.success(result)

    if st.button("View Assignments"):
        data = view_assignments()
        st.write(data)

# -----------------------------
# 5. STUDY PLANNER (Week 6)
# -----------------------------
elif option == "Study Planner":
    st.header("📚 Study Planner")

    subjects_input = st.text_input("Subjects (comma separated)")
    hours = st.slider("Study hours per day", 1, 10)

    if st.button("Generate Plan"):
        if subjects_input:
            subjects = subjects_input.split(",")

            plan = create_study_plan(subjects, hours)
            breaks = study_with_breaks(hours)

            st.subheader("📖 Study Plan")
            for p in plan:
                st.write(p)

            st.subheader("⏱️ Study + Break Schedule")
            for b in breaks:
                st.write(b)
        else:
            st.warning("Enter subjects")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("✅ Built with Streamlit | AI Timetable Assistant")

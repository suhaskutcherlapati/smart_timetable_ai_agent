from datetime import datetime, timedelta
import json
import re

FILE = "storage/events.json"


def parse_text(text):
    now = datetime.now()

    if "tomorrow" in text.lower():
        date = now + timedelta(days=1)
    else:
        date = now

    time_match = re.search(r"(\d+)(am|pm)", text.lower())
    if time_match:
        hour = int(time_match.group(1))
        if time_match.group(2) == "pm" and hour != 12:
            hour += 12
        date = date.replace(hour=hour, minute=0, second=0)

    duration_match = re.search(r"(\d+) hour", text.lower())
    duration = int(duration_match.group(1)) if duration_match else 1

    end = date + timedelta(hours=duration)

    return date, end


def load_events():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_events(events):
    with open(FILE, "w") as f:
        json.dump(events, f, indent=4)


def has_conflict(events, start, end):
    for e in events:
        s = datetime.fromisoformat(e["start"])
        en = datetime.fromisoformat(e["end"])
        if not (end <= s or start >= en):
            return True
    return False


def create_event(text):
    start, end = parse_text(text)

    events = load_events()

    if has_conflict(events, start, end):
        return "⚠ Conflict detected!"

    event = {
        "title": text,
        "start": start.isoformat(),
        "end": end.isoformat()
    }

    events.append(event)
    save_events(events)

    return f"✅ Event created: {text}"

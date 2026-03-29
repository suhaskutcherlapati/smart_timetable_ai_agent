import json

FILE = "storage/events.json"


def get_events():
    try:
        with open(FILE, "r") as f:
            events = json.load(f)
    except:
        return "No events found"

    if not events:
        return "No events scheduled"

    result = "\n📅 Events:\n"
    for e in events:
        result += f"{e['title']} -> {e['start']}\n"

    return result


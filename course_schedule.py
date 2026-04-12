import json
from datetime import datetime

FILE = "storage/class_schedule.json"

def load_schedule():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_schedule(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_class(title, day, time, type):
    schedule = load_schedule()
    
    schedule.append({
        "title": title,
        "day": day,
        "time": time,
        "type": type  # lecture/lab/tutorial
    })

    save_schedule(schedule)
    return f"{type} '{title}' added on {day} at {time}"

def view_classes():
    return load_schedule()
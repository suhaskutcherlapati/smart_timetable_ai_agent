import json

FILE = "storage/class_schedule.json"

def load_schedule():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []   # ✅ MUST be list

def save_schedule(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
        


def view_classes():
    return load_schedule()
def check_conflict(new_class, schedule):
    for c in schedule:
        if c["day"] == new_class["day"] and c["time"] == new_class["time"]:
            return True
    return False
def add_class(title, day, time, type_class):
    schedule = load_schedule()

    new_class = {
        "title": title,
        "day": day,
        "time": time,
        "type": type_class
    }

    if check_conflict(new_class, schedule):
        return "❌ Conflict detected!"

    schedule.append(new_class)
    save_schedule(schedule)

    return "✅ Class added"

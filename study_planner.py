def create_study_plan(subjects, hours_per_day):
    plan = []
    
    per_subject = hours_per_day // len(subjects)

    for subject in subjects:
        plan.append({
            "subject": subject,
            "hours": per_subject
        })

    return plan
def study_with_breaks(total_hours):
    sessions = []

    for i in range(total_hours * 2):  # 25min study + 5min break
        sessions.append("📚 Study 25 mins")
        sessions.append("☕ Break 5 mins")

    return sessions
def create_study_plan(subjects, hours_per_day):
    plan = []
    per_subject = hours_per_day // len(subjects)

    for subject in subjects:
        plan.append({
            "subject": subject.strip(),
            "hours": per_subject
        })

    return plan


def study_with_breaks(total_hours):
    sessions = []

    for i in range(total_hours * 2):
        sessions.append("📚 Study 25 mins")
        sessions.append("☕ Break 5 mins")

    return sessions
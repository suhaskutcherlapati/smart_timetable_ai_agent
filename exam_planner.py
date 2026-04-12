from datetime import datetime, timedelta

def plan_study(exam_date, subject):
    exam = datetime.strptime(exam_date, "%Y-%m-%d")
    today = datetime.today()

    days_left = (exam - today).days
    study_plan = []

    for i in range(days_left):
        study_day = today + timedelta(days=i)
        study_plan.append({
            "date": study_day.strftime("%Y-%m-%d"),
            "task": f"Study {subject} - Day {i+1}"
        })

    return study_plan
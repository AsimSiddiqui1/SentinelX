from datetime import datetime, timedelta

def generate_timeline():

    start = datetime.now()

    events = [
        "Attack Started",
        "Initial Compromise",
        "Privilege Escalation",
        "Suspicious Activity Detected",
        "SOC Alert Generated"
    ]

    timeline = []

    for i, event in enumerate(events):
        timestamp = start + timedelta(minutes=i)
        timeline.append(
            f"{timestamp.strftime('%H:%M:%S')} - {event}"
        )

    return timeline

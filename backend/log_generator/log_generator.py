from datetime import datetime
import random

logs = [
    "Failed Login Attempt",
    "Successful Login",
    "Firewall Blocked IP",
    "Malicious File Detected",
    "Suspicious Network Connection"
]

event = random.choice(logs)

print({
    "timestamp": str(datetime.now()),
    "event": event,
    "severity": random.choice(["Low", "Medium", "High"])
})

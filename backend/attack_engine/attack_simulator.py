import random
from datetime import datetime

attacks = {
    "Brute Force": {
        "mitre": "T1110",
        "logs": [
            "Multiple failed login attempts",
            "Account lockout triggered",
            "Suspicious authentication request"
        ]
    },

    "Phishing": {
        "mitre": "T1566",
        "logs": [
            "Phishing email received",
            "User clicked malicious link",
            "Credential submission detected"
        ]
    },

    "Ransomware": {
        "mitre": "T1486",
        "logs": [
            "Suspicious file execution",
            "Mass file encryption detected",
            "Ransom note created"
        ]
    },

    "Web Exploitation": {
        "mitre": "T1190",
        "logs": [
            "SQL Injection attempt detected",
            "Webshell upload attempt",
            "Unauthorized admin access"
        ]
    }
}

attack = random.choice(list(attacks.keys()))

print("\n===== SentinelX Attack Simulator =====")
print(f"Time: {datetime.now()}")
print(f"Attack: {attack}")
print(f"MITRE: {attacks[attack]['mitre']}")

print("\nGenerated Logs:")

for log in attacks[attack]["logs"]:
    print(f"[LOG] {log}")

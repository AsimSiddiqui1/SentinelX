import random
from backend.shared.attack_data import attacks

# Select random attack
attack = random.choice(list(attacks.keys()))

# Get attack details
data = attacks[attack]

# Calculate severity
if data["risk"] >= 90:
    severity = "Critical"
elif data["risk"] >= 80:
    severity = "High"
elif data["risk"] >= 60:
    severity = "Medium"
else:
    severity = "Low"

# Recommendations
recommendations = {
    "Phishing": [
        "Reset affected credentials",
        "Block malicious domain",
        "Enable MFA"
    ],

    "Brute Force": [
        "Block attacking IP",
        "Enable account lockout",
        "Enforce MFA"
    ],

    "Ransomware": [
        "Isolate infected host",
        "Disconnect network access",
        "Restore from backup"
    ],

    "Web Exploitation": [
        "Patch vulnerable application",
        "Review web server logs",
        "Block malicious requests"
    ]
}

print("\n===== SentinelX AI Defender =====\n")

print(f"Detected Attack : {attack}")
print(f"MITRE Technique : {data['mitre']}")
print(f"Risk Score      : {data['risk']}/100")
print(f"Severity        : {severity}")

print("\nGenerated Logs:")
for log in data["logs"]:
    print(f"  [LOG] {log}")

print("\nRecommended Actions:")
for rec in recommendations[attack]:
    print(f"  - {rec}")

print("\n=================================\n")

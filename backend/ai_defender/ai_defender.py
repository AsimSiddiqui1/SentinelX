from backend.shared.attack_data import attacks

attack = "Phishing"

data = attacks[attack]

print("\n===== SentinelX AI Defender =====")

print(f"Detected Attack : {attack}")
print(f"MITRE Technique : {data['mitre']}")
print(f"Risk Score      : {data['risk']}/100")

if data["risk"] >= 90:
    severity = "Critical"
elif data["risk"] >= 80:
    severity = "High"
elif data["risk"] >= 60:
    severity = "Medium"
else:
    severity = "Low"

print(f"Severity        : {severity}")

print("\nRecommended Actions:")

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

for rec in recommendations[attack]:
    print(f"- {rec}")

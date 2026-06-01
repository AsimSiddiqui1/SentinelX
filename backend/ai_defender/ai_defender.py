from backend.shared.attack_data import attacks


def detect_attack(logs):

    text = " ".join(logs).lower()

    if "failed login" in text:
        return "Brute Force"

    elif "credential submission" in text:
        return "Phishing"

    elif "mass file encryption" in text:
        return "Ransomware"

    elif "sql injection" in text:
        return "Web Exploitation"

    elif "multiple accounts targeted" in text:
        return "Password Spray"

    elif "repeated password attempts" in text:
        return "Password Spray"

    elif "privilege escalation" in text:
        return "Privilege Escalation"

    elif "admin token abuse" in text:
        return "Privilege Escalation"

    return "Unknown"

def calculate_attack_severity(attack):

    if attack not in attacks:
        return "Low"

    risk = attacks[attack]["risk"]

    if risk >= 90:
        return "Critical"

    elif risk >= 80:
        return "High"

    elif risk >= 60:
        return "Medium"

    return "Low"


def get_recommendations(attack):

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

        "Password Spray": [
            "Force password reset",
            "Enable MFA",
            "Monitor authentication logs"
        ],
        
        "Privilege Escalation": [
            "Review admin permissions",
            "Patch vulnerable systems",
            "Investigate compromised accounts"
        ],

        "Web Exploitation": [
            "Patch vulnerable application",
            "Review web server logs",
            "Block malicious requests"
        ]
    }

    return recommendations.get(
        attack,
        ["No recommendations available"]
    )

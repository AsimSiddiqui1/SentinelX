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
    },

    "Password Spray": {
        "mitre": "T1110.003",
        "logs": [
            "Multiple accounts targeted",
            "Repeated password attempts detected",
            "Authentication anomaly observed"
        ]
    },

    "Privilege Escalation": {
        "mitre": "T1068",
        "logs": [
            "Unauthorized privilege request",
            "Admin token abuse detected",
            "Local privilege escalation observed"
        ]
    }
}

def simulate_attack(attack_type):

    if attack_type not in attacks:
        return {
            "attack": "Unknown",
            "mitre": "N/A",
            "logs": ["Unknown security event"]
        }

    return {
        "attack": attack_type,
        "mitre": attacks[attack_type]["mitre"],
        "logs": attacks[attack_type]["logs"]
    }

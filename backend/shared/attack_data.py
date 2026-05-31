attacks = {
    "Brute Force": {
        "mitre": "T1110",
        "risk": 70,
        "logs": [
            "Multiple failed login attempts",
            "Account lockout triggered",
            "Suspicious authentication request"
        ]
    },

    "Phishing": {
        "mitre": "T1566",
        "risk": 85,
        "logs": [
            "Phishing email received",
            "User clicked malicious link",
            "Credential submission detected"
        ]
    },

    "Ransomware": {
        "mitre": "T1486",
        "risk": 95,
        "logs": [
            "Suspicious file execution",
            "Mass file encryption detected",
            "Ransom note created"
        ]
    },

    "Web Exploitation": {
        "mitre": "T1190",
        "risk": 80,
        "logs": [
            "SQL Injection attempt detected",
            "Webshell upload attempt",
            "Unauthorized admin access"
        ]
    }
}

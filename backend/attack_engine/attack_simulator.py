def simulate_attack(attack_type):

    if attack_type == "Brute Force":
        return [
            "Multiple failed login attempts",
            "Account lockout triggered",
            "Suspicious authentication request"
        ]

    elif attack_type == "Phishing":
        return [
            "Phishing email received",
            "User clicked malicious link",
            "Credential submission detected"
        ]

    elif attack_type == "Ransomware":
        return [
            "Suspicious file execution",
            "Mass file encryption detected",
            "Ransom note created"
        ]

    elif attack_type == "Web Exploitation":
        return [
            "SQL Injection attempt detected",
            "Webshell upload attempt",
            "Unauthorized admin access"
        ]

    return [
        "Unknown security event"
    ]

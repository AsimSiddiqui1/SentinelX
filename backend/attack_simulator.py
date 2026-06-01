def simulate_attack(attack_type):

    if attack_type == "Brute Force":
        return [
            "Failed login attempt from 192.168.1.10",
            "Failed login attempt from 192.168.1.10",
            "Failed login attempt from 192.168.1.10",
            "Failed login attempt from 192.168.1.10",
            "Account lockout triggered"
        ]

    elif attack_type == "Phishing":
        return [
            "Email received from suspicious domain",
            "User clicked malicious link",
            "Credential submission detected"
        ]

    elif attack_type == "Ransomware":
        return [
            "Unknown executable launched",
            "Mass file encryption detected",
            "Ransom note created"
        ]

    elif attack_type == "Password Spray":
        return [
            "Multiple accounts targeted",
            "Repeated password attempts detected",
            "Authentication anomaly observed"
        ]

    elif attack_type == "Web Exploitation":
        return [
            "Suspicious HTTP request detected",
            "SQL Injection pattern observed",
            "Unauthorized database access attempt"
        ]

    return [
        "Unknown security event"
    ]

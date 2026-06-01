def detect_attack(logs):

    text = " ".join(logs)

    if "Failed login attempt" in text:
        return "Brute Force"

    elif "Credential submission detected" in text:
        return "Phishing"

    elif "Mass file encryption" in text:
        return "Ransomware"

    elif "Authentication anomaly" in text:
        return "Password Spray"

    elif "SQL Injection" in text:
        return "Web Exploitation"

    return "Unknown"

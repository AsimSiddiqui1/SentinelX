def calculate_severity(risk_score, criticality):

    if criticality == "Critical":
        risk_score += 10

    elif criticality == "High":
        risk_score += 5

    if risk_score >= 95:
        return "Critical"

    elif risk_score >= 80:
        return "High"

    elif risk_score >= 60:
        return "Medium"

    return "Low"

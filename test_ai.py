from backend.ai_defender.llm_analyzer import analyze_incident

logs = [
    "Multiple failed login attempts",
    "Account lockout triggered",
    "Suspicious authentication request"
]

result = analyze_incident(logs)

print(result)

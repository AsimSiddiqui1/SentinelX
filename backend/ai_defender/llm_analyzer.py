import google.generativeai as genai

API_KEY = "AQ.Ab8RN6IKgWOjIBt6bMGzl-7bv76n4fL3UZXT4dmxHH-b7rtGLA"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def analyze_incident(logs):

    prompt = f"""
You are a SOC Analyst.

Analyze these security logs:

{logs}

Provide:

1. Incident Summary
2. Business Impact
3. Recommendations
4. Confidence Score (0-100)
5. Verdict (Malicious, Suspicious, Under Investigation)
"""

    response = model.generate_content(prompt)

    return response.text

from google import genai

API_KEY = "AQ.Ab8RN6Jno6bKXeYcOE-P_VyCiHoXmw8dLhe0zUUhxxljnV4MxA"

client = genai.Client(api_key=API_KEY)


def analyze_incident(logs):

    prompt = f"""
You are a SOC Analyst.

Analyze these logs:

{logs}

Provide:
1. Incident Summary
2. Business Impact
3. Recommendations
4. Confidence Score (0-100)
5. Verdict (Malicious, Suspicious, Under Investigation)
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text

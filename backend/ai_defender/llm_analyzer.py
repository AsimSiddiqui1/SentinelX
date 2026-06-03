from google import genai

API_KEY = "AQ.Ab8RN6Jno6bKXeYcOE-P_VyCiHoXmw8dLhe0zUUhxxljnV4MxA"

client = genai.Client(api_key=API_KEY)


def analyze_incident(logs):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception:
        return """
Summary:
AI analysis unavailable.

Business Impact:
Unable to generate analysis.

Recommendations:
- Review logs manually
- Check API quota
- Retry later

Confidence:
N/A

Verdict:
Under Investigation
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text

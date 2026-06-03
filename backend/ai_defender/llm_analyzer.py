from google import genai

API_KEY = "AQ.Ab8RN6Jno6bKXeYcOE-P_VyCiHoXmw8dLhe0zUUhxxljnV4MxA"

client = genai.Client(api_key=API_KEY)


def analyze_incident(logs):

    prompt = f"""
You are a Senior SOC Analyst.

Analyze these security logs:

{logs}

Return ONLY this format:

Summary:
(max 2 lines)

Business Impact:
(max 2 lines)

Recommendations:
- recommendation 1
- recommendation 2
- recommendation 3

Confidence:
XX%

Verdict:
Malicious / Suspicious / Under Investigation

Keep the entire response under 120 words.
"""

    try:
        print("Sending to Gemini:", logs)

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        print("Gemini Response:")
        print(response.text)

        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        return f"""
Summary:
AI analysis unavailable.

Business Impact:
{str(e)}

Recommendations:
- Review logs manually
- Check API quota
- Retry later

Confidence:
N/A

Verdict:
Under Investigation
"""

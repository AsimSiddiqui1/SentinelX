import google.generativeai as genai

API_KEY = "AQ.Ab8RN6KmlYOw4gmplgCkevUPLbpiyCx1WNVOMqWcsW4CR2j1kQ"

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel(
    "models/gemini-2.5-flash-lite"
)

response = model.generate_content(
    "What is phishing? Answer in one sentence."
)

print(response.text)

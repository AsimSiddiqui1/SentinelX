import google.generativeai as genai

API_KEY = "AQ.Ab8RN6IKgWOjIBt6bMGzl-7bv76n4fL3UZXT4dmxHH-b7rtGLA"

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel(
    "models/gemini-2.5-flash-lite"
)

response = model.generate_content(
    "What is phishing? Answer in one sentence."
)

print(response.text)

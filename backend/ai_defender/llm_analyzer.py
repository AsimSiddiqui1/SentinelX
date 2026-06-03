import google.generativeai as genai

API_KEY = "AQ.Ab8RN6IKgWOjIBt6bMGzl-7bv76n4fL3UZXT4dmxHH-b7rtGLA"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "models/gemini-2.5-computer-use-preview-10-2025"
)

response = model.generate_content(
    "Say hello in one sentence."
)

print(response.text)

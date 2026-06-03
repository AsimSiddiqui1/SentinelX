import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6IKgWOjIBt6bMGzl-7bv76n4fL3UZXT4dmxHH-b7rtGLA")

for model in genai.list_models():
    if (
        "flash" in model.name.lower()
        and "generateContent" in str(model.supported_generation_methods)
    ):
        print(model.name)

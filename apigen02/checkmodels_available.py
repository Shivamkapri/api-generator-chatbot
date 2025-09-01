import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

models = genai.list_models()
for m in models:
    print(m.name)

# import google.generativeai as genai

# genai.configure(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# models = genai.list_models()
# for m in models:
#     print(m.name)
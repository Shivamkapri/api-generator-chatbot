
import google.generativeai as genai

def generate_code_gemini(api_key, request, language, prompt_template_path):
    with open(prompt_template_path, 'r') as f:
        prompt_template = f.read()
    prompt = prompt_template.format(
        method=request["method"],
        url=request["url"],
        headers=request["headers"],
        body=request["body"] or "",
        language=language
    )
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config={'temperature': 0.7}
    )
    response = model.generate_content(
        prompt,
        request_options={'timeout': 60}  # 60 second timeout for API call
    )
    return response.text
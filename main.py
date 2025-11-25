from flask import Flask, render_template, request, jsonify
from postman_parser import parse_postman_collection
from langchain_codegen import generate_code_gemini
import os
import tempfile
from dotenv import load_dotenv   # added

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")   # now pulled from .env
PROMPT_PATH = "prompts/codegen_prompt.txt"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    language = request.form.get('language', 'python')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    # Save uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
        file.save(tmp.name)
        tmp_path = tmp.name

    try:
        requests = parse_postman_collection(tmp_path)
        codes = []
        for req in requests:
            code = generate_code_gemini(API_KEY, req, language, PROMPT_PATH)
            codes.append(f"# {req['name']}\n" + code)
        result = '\n\n'.join(codes)
    except Exception as e:
        result = f"Error: {str(e)}"
    finally:
        os.remove(tmp_path)

    return jsonify({'code': result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

# from flask import Flask, render_template, request, jsonify
# from postman_parser import parse_postman_collection
# from langchain_codegen import generate_code_gemini
# import os
# import tempfile

# app = Flask(__name__, static_folder='static', template_folder='templates')

# API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
# PROMPT_PATH = "prompts/codegen_prompt.txt"

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

# @app.route('/generate', methods=['POST'])
# def generate():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400
#     file = request.files['file']
#     language = request.form.get('language', 'python')
#     if not file:
#         return jsonify({'error': 'No file uploaded'}), 400
#     # Save uploaded file to a temp file
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
#         file.save(tmp.name)
#         tmp_path = tmp.name
#     try:
#         requests = parse_postman_collection(tmp_path)
#         codes = []
#         for req in requests:
#             code = generate_code_gemini(API_KEY, req, language, PROMPT_PATH)
#             codes.append(f"# {req['name']}\n" + code)
#         result = '\n\n'.join(codes)
#     except Exception as e:
#         result = f"Error: {str(e)}"
#     finally:
#         os.remove(tmp_path)
#     return jsonify({'code': result})

# if __name__ == "__main__":
#     app.run(debug=True)
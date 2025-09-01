


# API Code Generator from Postman Collection

This project takes a Postman collection and generates code for API requests in your chosen programming language using Google Gemini (Generative AI).

## Features

- Parse Postman collection JSON files
- Generate code in Python, JavaScript, etc. using Gemini LLM


## Setup

1. **Clone the repository:**
using git clone ......

2. **Create and activate a virtual environment (optional but recommended):**

   python -m venv myenv
   # On Windows:
   myenv\Scripts\activate
   # On Mac/Linux:
   source myenv/bin/activate
 

3. **Install dependencies:**
   pip install -r requirements.txt


</br>
4.Create gemmi api key n check the models which u can use by running 
apigen02/checkmodels_available.py

5.**Run the main script:**
   python main.py

6. run static/index.html   ( http://127.0.0.1:5000/ )
7. upload postman collection (documentation/input/acme.postman_collection.json)
8. select language
9. generating code will take 1-2 min depending upon the model which u are using



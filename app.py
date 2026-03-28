import os
import re
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10mb limit resumes shouldnt be this big but just in case

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    prompt = """You are an expert resume reviewer with 15+ years in tech hiring.

Analyze this resume and respond in this exact format:

Overall Score: X/10

**Strengths:**
- (3-5 specific strengths)

*Weaknesses / Areas to Improve:**
- (3-5 specific weaknesses)

**Quick Wins (easy fixes):**
- (2-3 things they can fix today)

**Missing Sections or Keywords:**
- (important missing sections or ATS keywords)

**One Sentence Summary:**
(one honest sentence about this resume's current state)

Roast:
Give a short, funny, friendly roast of this resume in 2-3 sentences. Be witty and playful, not mean. Like a friend who happens to be a hiring manager.

Do not use any markdown formatting, asterisks, or special characters in your response.
Be specific, honest, and reference actual content from the resume."""


    response = model.generate_content([
        prompt,
        {
            "mime_type": "application/pdf",
            "data": pdf_data
        }
    ])
    return response.text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are supported'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        feedback = analyze_resume(filepath)
        return jsonify({'feedback': feedback})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(filepath):  # always delete after, dont want resumes sitting on the serve
            os.remove(filepath)


if __name__ == '__main__':
    app.run(debug=True)

# AI Resume Analyzer

Upload a PDF resume and get instant AI-powered feedback — strengths, weaknesses, quick wins, and an overall score. Built with Flask + Google Gemini API.

## Features

- Upload any PDF resume
- Gemini reads the PDF natively (no text extraction needed)
- Structured feedback: score, strengths, weaknesses, quick wins, missing keywords
- Clean dark UI
- Ready to deploy on Render

## Setup

### 1. Clone & install

```bash
git clone <your-repo-url>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Get a Gemini API key

Go to [aistudio.google.com](https://aistudio.google.com) → Get API key (free)

### 3. Configure environment

```bash
.env
# Edit .env and add your GEMINI_API_KEY
```

### 4. Run locally

```bash
python app.py
```

Visit `http://localhost:5000`

## Deploy to Render

1. Push this project to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set environment variable: `GEMINI_API_KEY = your_key_here`
5. Build command: `pip install -r requirements.txt`
6. Start command: `gunicorn app:app`

## Tech Stack

- **Backend**: Python, Flask
- **AI**: Google Gemini 2.5 Flash (native PDF reading)
- **Deployment**: Render
- **Frontend**: HTML, CSS, Vanilla JS

# AI-RESUME

built this because i wanted feedback on my own resume without paying for those resume review sites. you upload a pdf and gemini reads it and gives you a score, strengths, weaknesses, and a few quick fixes. also roasts you a little at the end.

## how it works

you upload your resume as a pdf, flask saves it temporarily, sends it to gemini as raw binary (no text extraction needed, gemini reads it natively), gets the feedback back, then deletes the file. nothing is stored.

## stack

- python + flask
- google gemini api
- html css js frontend

## setup
```
get a free gemini api key from https://aistudio.google.com
git clone https://github.com/X-4bys5/AI-Resume.git
cd AI-Resume
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
create a .env file:
```
GEMINI_API_KEY=your_key_here
```
run it:
python app.py

go to http://localhost:5000

## known issues
```
- sometimes gemini returns markdown formatting even though i told it not to
- very large pdfs can be slow
```

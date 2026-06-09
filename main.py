import json
import requests
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

STARTOCODE_QUESTION_GENERATOR = "https://startocode-ai-api-v1.fly.dev/ask"


def build_page(results_html=""):
    with open("static/index.html") as file:
        html = file.read()

    return html.replace("<!-- RESULTS -->", results_html)


@app.get("/")
def home():
    return HTMLResponse(build_page())


@app.post("/generate")
def generate(
    subject: str = Form(...),
    topic: str = Form(...),
    num_questions: int = Form(...)
):

    response = requests.post(
        STARTOCODE_QUESTION_GENERATOR,
        json={"question": f"Generate {num_questions} questions about {topic} in {subject}"},
        timeout=30
    )

    data = response.json()

    return HTMLResponse(f"""
        <h2>DEBUG OUTPUT</h2>
        <pre>{data}</pre>
    """)
    answers = data.get("answer", "")

    if "used up your api credit" in answers.lower():
        results_html = f"""
        <div class="results">
            <h2>API Error</h2>
            <p style="color:red;">{answers}</p>
        </div>
        """
        return HTMLResponse(build_page(results_html))


    try:
        questions = json.loads(answers)
    except:
        questions = answers.split("\n")

    questions_html = ""

    for question in questions:
        questions_html += f"<li>{question}</li>"

    results_html = f"""
    <div class="results">
        <h2>{subject} - {topic}</h2>
        <ol>{questions_html}</ol>
    </div>
    """

    return HTMLResponse(build_page(results_html))
from fastapi import FastAPI, UploadFile, File, Form
import shutil
from service import analyze_candidate

app = FastAPI(
    title="AI Skill Gap & Career Readiness API",
    version="1.0"
)

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_path = f"temp_{resume.filename}"

    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    result = analyze_candidate(resume_path, job_description)
    return result

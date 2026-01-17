from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
from service import analyze_candidate

app = FastAPI(
    title="AI Skill Gap & Career Readiness API",
    version="1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

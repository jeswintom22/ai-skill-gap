from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.models.schemas import AnalysisResponse
from app.dependencies.config import get_settings
from app.core.logging import logger
import shutil
import os
from service import analyze_candidate

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Analyze resume against job description and generate skill gap report.
    
    - **resume**: PDF file containing the candidate's resume
    - **job_description**: Text description of the job requirements
    """
    logger.info(f"Received analysis request for resume: {resume.filename}")
    
    if not resume.filename.lower().endswith('.pdf'):
        logger.warning(f"Invalid file type: {resume.filename}")
        raise HTTPException(status_code=400, detail="Resume must be a PDF file")
    
    if not job_description.strip():
        logger.warning("Empty job description provided")
        raise HTTPException(status_code=400, detail="Job description cannot be empty")
    
    settings = get_settings()
    
    # Save uploaded file temporarily
    resume_path = f"temp_{resume.filename}"
    
    try:
        with open(resume_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)
        
        logger.info("Starting skill analysis...")
        # Perform analysis
        result = analyze_candidate(
            resume_path, 
            job_description,
            skills_db_path=settings.skills_db_path,
            weights_db_path=settings.weights_db_path
        )
        
        logger.info(f"Analysis completed. Readiness score: {result['analysis']['readiness_score']}%")
        return AnalysisResponse(**result)
    
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    
    finally:
        # Clean up temp file
        if os.path.exists(resume_path):
            os.remove(resume_path)
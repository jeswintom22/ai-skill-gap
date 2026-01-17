from fastapi import FastAPI, Request, Form, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.config import settings
from app.routers.analyze import router as analyze_router
from app.models.schemas import AnalysisResponse
from app.dependencies.config import get_settings
from app.core.logging import logger
import shutil
import os
from service import analyze_candidate

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(analyze_router)

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    """Serve the main UI"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/results")
async def show_results(request: Request):
    """Serve the results page"""
    return templates.TemplateResponse("results.html", {"request": request})

@app.post("/analyze-form")
async def analyze_form(
    request: Request,
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """Handle form submission and redirect to results"""
    logger.info(f"Received form analysis request for resume: {resume.filename}")
    
    if not resume.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Resume must be a PDF file")
    
    if not job_description.strip():
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
        
        # Return results page with data
        return templates.TemplateResponse("results.html", {
            "request": request,
            "user_skills": result["user_skills"],
            "job_skills": result["job_skills"],
            "analysis": result["analysis"],
            "ai_roadmap": result["ai_roadmap"]
        })
    
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    
    finally:
        # Clean up temp file
        if os.path.exists(resume_path):
            os.remove(resume_path)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": settings.version}
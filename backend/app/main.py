from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.config import settings
from app.routers.analyze import router as analyze_router

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

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": settings.version}
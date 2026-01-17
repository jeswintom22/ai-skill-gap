🧠 AI Skill Gap & Career Readiness Analyzer

An end-to-end AI-powered system that analyzes a candidate’s resume against job requirements, computes a weighted job readiness score, and generates a personalized learning roadmap using an LLM.

Built with Machine Learning + NLP + FastAPI + Local LLM (Ollama)

🚀 Problem Statement

Students and early-career professionals often struggle to answer:

Why am I not shortlisted?

What exact skills am I missing?

What should I learn next, and in what order?

Most tools provide generic advice.
This project provides data-driven, explainable, and actionable insights.

💡 Solution Overview

This system:

Extracts skills from a resume (PDF)

Extracts required skills from a job description

Uses hybrid AI (keyword + semantic ML) for accurate matching

Computes a weighted readiness score

Generates a 30-day personalized learning roadmap using an LLM

Exposes everything via a FastAPI REST API

🏗️ System Architecture
Resume (PDF)
   ↓
Resume Parser (pdfplumber)
   ↓
Skill Extraction (Rule-based NLP)
   ↓
Job Skill Extraction
   ├── Keyword Matching
   └── Semantic Matching (Sentence Embeddings)
   ↓
Weighted Skill Gap Engine
   ↓
Readiness Score
   ↓
Roadmap Generator
   ├── Rule-based prioritization
   └── LLM (Ollama - Mistral)
   ↓
FastAPI Response (JSON)

🧠 Key Features

✅ Resume skill extraction (NLP)

✅ Hybrid job skill detection (Keyword + Semantic ML)

✅ Sentence Embeddings using sentence-transformers

✅ Weighted readiness scoring (industry-style ATS logic)

✅ AI-generated learning roadmap (offline LLM)

✅ Clean FastAPI backend with Swagger UI

✅ Fully explainable & modular design

🛠️ Tech Stack
Backend

Python 3.10+

FastAPI

Uvicorn

AI / ML

pdfplumber – Resume text extraction

scikit-learn – Similarity & utilities

sentence-transformers – Semantic embeddings

Ollama (Mistral) – Local LLM for roadmap generation

Others

JSON-based skill & weight databases

Swagger UI for API testing

📂 Project Structure
ai-skill-gap/
│
├── backend/
│   ├── api.py                 # FastAPI app with CORS
│   ├── service.py             # Main analysis orchestrator
│   ├── resume_parser.py       # PDF text extraction
│   ├── skill_extractor.py     # Rule-based skill extraction
│   ├── job_analyzer.py        # Job description analysis
│   ├── semantic_matcher.py    # ML-based semantic matching
│   ├── job_skill_extractor.py # Hybrid job skill detection
│   ├── skill_gap.py           # Weighted gap calculation
│   ├── roadmap_generator.py   # Rule-based roadmap
│   ├── ai_roadmap_generator.py # LLM-powered roadmap
│   ├── requirements.txt       # Python dependencies
│   └── test_*.py              # Unit tests
│
├── frontend/
│   ├── index.html             # Main UI
│   ├── app.js                 # Frontend logic
│   └── styles.css             # Styling
│
├── data/
│   ├── skills.json            # Skill database
│   ├── skill_weights.json     # Skill importance weights
│   └── job_descriptions/      # Sample job descriptions
│
├── .gitignore
└── README.md

⚙️ Setup & Installation

1️⃣ Clone Repository
```bash
git clone https://github.com/jeswintom22/ai-skill-gap.git
cd ai-skill-gap
```

2️⃣ Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

3️⃣ Install & Run Ollama (for AI Roadmap)
```bash
# Download and install Ollama from https://ollama.ai/
ollama pull mistral
ollama serve
```

4️⃣ Frontend Setup
```bash
cd ../frontend
# No installation needed - just open index.html in browser
# Or serve with any static server (e.g., python -m http.server 3000)
```

▶️ Run the Application

1. Start Backend:
```bash
cd backend
uvicorn api:app --reload
```
Backend will run at: http://127.0.0.1:8000

2. Open Frontend:
- Open `frontend/index.html` in your browser
- Or serve frontend: `cd frontend && python -m http.server 3000`
- Access at: http://localhost:3000

3. Test API:
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

🧪 API Usage

**Endpoint:** `POST /analyze`

**Inputs:**
- `resume`: PDF file upload
- `job_description`: Text string

**Output (JSON):**
```json
{
  "user_skills": ["python", "sql", "machine learning"],
  "job_skills": ["python", "django", "docker", "git", "linux", "sql", "kubernetes"],
  "analysis": {
    "missing_skills": ["django", "docker", "git", "linux", "kubernetes"],
    "readiness_score": 42.86
  },
  "ai_roadmap": "Week 1: Learn Django basics and build a simple web app...\nWeek 2: Master Docker containerization...\n..."
}
```

**Frontend Usage:**
1. Upload your resume (PDF)
2. Paste job description
3. Click "Analyze Skills"
4. View readiness score, missing skills, and personalized 30-day roadmap

� Testing

Run unit tests:
```bash
cd backend
python -m pytest test_*.py -v
```

Or run individual tests:
```bash
python test_resume.py
python test_skill_gap.py
python test_semantic.py
# etc.
```

�🧠 Why This Project Is Different

❌ Not a black-box AI

✅ Explainable, deterministic core logic

✅ ML used only where it adds real value

✅ LLM used for guidance, not decision-making

✅ Mimics real-world ATS & career intelligence systems

📈 Future Enhancements

Frontend UI (React / HTML)

GitHub & LinkedIn profile analysis

Multiple job role comparison

Skill trend analytics

Deployment on cloud

Authentication & user profiles

👨‍💻 Author

Jeswin Tom
AI / ML Enthusiast | Backend Developer

⭐ If You Like This Project

Give it a ⭐ on GitHub — it really helps!
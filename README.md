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
│   ├── api.py
│   ├── service.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── job_analyzer.py
│   ├── semantic_matcher.py
│   ├── job_skill_extractor.py
│   ├── skill_gap.py
│   ├── roadmap_generator.py
│   ├── ai_roadmap_generator.py
│   └── requirements.txt
│
├── data/
│   ├── skills.json
│   ├── skill_weights.json
│   └── job_descriptions/
│
├── .gitignore
└── README.md

⚙️ Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/jeswintom22/ai-skill-gap.git
cd ai-skill-gap/backend

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install & Run Ollama
ollama pull mistral
ollama serve

▶️ Run the Application
uvicorn api:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

🧪 API Usage
Endpoint
POST /analyze

Inputs

Resume (PDF upload)

Job Description (text)

Output (JSON)
{
  "user_skills": ["python", "sql"],
  "job_skills": ["python", "django", "docker", "git", "linux", "sql"],
  "analysis": {
    "missing_skills": ["django", "docker", "git", "linux"],
    "readiness_score": 41.67
  },
  "ai_roadmap": "Week 1-2: Django...\nWeek 3: Docker..."
}

🧠 Why This Project Is Different

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
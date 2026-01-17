import os
from resume_parser import extract_text_from_pdf
from skill_extractor import load_skills, extract_skills

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "sample_resume.pdf")
SKILL_PATH = os.path.join(BASE_DIR, "../data/skills.json")

text = extract_text_from_pdf(PDF_PATH)
skills_db = load_skills(SKILL_PATH)

skills = extract_skills(text, skills_db)
print("Extracted skills:", skills)

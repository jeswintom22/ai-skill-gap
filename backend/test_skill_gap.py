from resume_parser import extract_text_from_pdf
from skill_extractor import load_skills, extract_skills
from job_analyzer import analyze_job_description
from skill_gap import calculate_skill_gap

resume_text = extract_text_from_pdf("sample_resume.pdf")

skills_db = load_skills("../data/skills.json")
user_skills = extract_skills(resume_text, skills_db)

with open("../data/job_descriptions/software_engineer.txt") as f:
    job_text = f.read()

job_skills = analyze_job_description(job_text, skills_db)
result = calculate_skill_gap(user_skills, job_skills)

print("User skills:", user_skills)
print("Job skills:", job_skills)
print("Result:", result)

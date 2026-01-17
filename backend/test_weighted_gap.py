from skill_gap import load_skill_weights, calculate_weighted_skill_gap
from job_skill_extractor import extract_job_skills
from skill_extractor import load_skills, extract_skills
from resume_parser import extract_text_from_pdf

resume_text = extract_text_from_pdf("sample_resume.pdf")

skills_db = load_skills("../data/skills.json")
user_skills = extract_skills(resume_text, skills_db)

with open("../data/job_descriptions/software_engineer.txt") as f:
    job_text = f.read()

job_skills = extract_job_skills(job_text, skills_db)
weights = load_skill_weights("../data/skill_weights.json")

result = calculate_weighted_skill_gap(user_skills, job_skills, weights)

print("User skills:", user_skills)
print("Job skills:", job_skills)
print("Weighted result:", result)

from skill_extractor import load_skills
from job_skill_extractor import extract_job_skills

with open("../data/job_descriptions/software_engineer.txt") as f:
    job_text = f.read()

skills_db = load_skills("../data/skills.json")

job_skills = extract_job_skills(job_text, skills_db)

print("Final job skills (keyword + semantic):")
print(job_skills)

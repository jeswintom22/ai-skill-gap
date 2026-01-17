from semantic_matcher import semantic_skill_match
from skill_extractor import load_skills

with open("../data/job_descriptions/software_engineer.txt") as f:
    job_text = f.read()

skills_db = load_skills("../data/skills.json")

matched = semantic_skill_match(job_text, skills_db)

print("Semantically detected skills:")
print(matched)

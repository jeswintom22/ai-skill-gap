import json

def load_skills(skill_file="data/skills.json"):
    with open(skill_file, "r") as f:
        return json.load(f)

def extract_skills(text: str, skill_db: dict):
    found_skills = set()

    for category in skill_db.values():
        for skill in category:
            if skill.lower() in text:
                found_skills.add(skill)

    return list(found_skills)

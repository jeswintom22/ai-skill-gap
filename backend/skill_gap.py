import json

def load_skill_weights(path="../data/skill_weights.json"):
    with open(path, "r") as f:
        return json.load(f)

def calculate_weighted_skill_gap(user_skills, job_skills, weights):
    user_set = set(user_skills)
    job_set = set(job_skills)

    matched = user_set & job_set
    missing = job_set - user_set

    total_weight = sum(weights.get(skill, 1) for skill in job_set)
    matched_weight = sum(weights.get(skill, 1) for skill in matched)

    readiness_score = (matched_weight / total_weight) * 100 if total_weight else 0

    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "matched_weight": matched_weight,
        "total_weight": total_weight,
        "readiness_score": round(readiness_score, 2)
    }

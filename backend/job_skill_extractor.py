from job_analyzer import analyze_job_description
from semantic_matcher import semantic_skill_match

def extract_job_skills(job_text, skills_db):
    keyword_skills = set(analyze_job_description(job_text, skills_db))
    semantic_skills = set(semantic_skill_match(job_text, skills_db))

    combined_skills = keyword_skills.union(semantic_skills)
    return list(combined_skills)

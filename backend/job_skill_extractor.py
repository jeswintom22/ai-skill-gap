from job_analyzer import analyze_job_description

def extract_job_skills(job_text, skills_db):
    keyword_skills = set(analyze_job_description(job_text, skills_db))
    
    # Lazy import to avoid startup issues
    try:
        from semantic_matcher import semantic_skill_match
        semantic_skills = set(semantic_skill_match(job_text, skills_db))
    except RuntimeError as e:
        # If semantic matching fails, fall back to keyword matching only
        semantic_skills = set()
    
    combined_skills = keyword_skills.union(semantic_skills)
    return list(combined_skills)

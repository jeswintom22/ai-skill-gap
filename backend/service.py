from resume_parser import extract_text_from_pdf
from skill_extractor import load_skills, extract_skills
from job_skill_extractor import extract_job_skills
from skill_gap import load_skill_weights, calculate_weighted_skill_gap
from roadmap_generator import prioritize_skills
from ai_roadmap_generator import generate_ai_roadmap

def analyze_candidate(resume_path, job_text, skills_db_path="../data/skills.json", weights_db_path="../data/skill_weights.json"):
    # Load databases
    skills_db = load_skills(skills_db_path)
    weights = load_skill_weights(weights_db_path)

    # Resume → skills
    resume_text = extract_text_from_pdf(resume_path)
    user_skills = extract_skills(resume_text, skills_db)

    # Job → skills
    job_skills = extract_job_skills(job_text, skills_db)

    # Skill gap + weighted score
    gap_result = calculate_weighted_skill_gap(
        user_skills,
        job_skills,
        weights
    )

    # Roadmap
    prioritized = prioritize_skills(
        gap_result["missing_skills"],
        weights
    )
    roadmap = generate_ai_roadmap(prioritized)

    return {
        "user_skills": user_skills,
        "job_skills": job_skills,
        "analysis": gap_result,
        "ai_roadmap": roadmap
    }

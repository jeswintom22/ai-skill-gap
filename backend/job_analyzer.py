from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_job_description(job_text: str, skills_db: dict):
    job_text = job_text.lower()
    required_skills = set()

    for category in skills_db.values():
        for skill in category:
            if skill.lower() in job_text:
                required_skills.add(skill)

    return list(required_skills)
    


def calculate_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return float(similarity[0][0])

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer("all-MiniLM-L6-v2")

def split_into_sentences(text):
    return [s.strip() for s in re.split(r"[.\n]", text) if s.strip()]

def semantic_skill_match(job_text: str, skills_db: dict, threshold=0.5):
    sentences = split_into_sentences(job_text)
    sentence_embeddings = model.encode(sentences)

    matched_skills = set()

    for category in skills_db.values():
        for skill in category:
            skill_embedding = model.encode([skill])

            for sent_emb in sentence_embeddings:
                similarity = cosine_similarity(skill_embedding, [sent_emb])[0][0]

                if similarity >= threshold:
                    matched_skills.add(skill)
                    break

    return list(matched_skills)

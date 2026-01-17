from roadmap_generator import prioritize_skills
from ai_roadmap_generator import generate_ai_roadmap
from skill_gap import load_skill_weights

missing_skills = ['linux', 'django', 'docker', 'git']
weights = load_skill_weights("../data/skill_weights.json")

prioritized = prioritize_skills(missing_skills, weights)

roadmap_text = generate_ai_roadmap(prioritized, duration_days=30)

print(roadmap_text)

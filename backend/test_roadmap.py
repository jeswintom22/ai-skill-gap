from roadmap_generator import generate_roadmap
from skill_gap import load_skill_weights

missing_skills = ['linux', 'django', 'docker', 'git']
weights = load_skill_weights("../data/skill_weights.json")

roadmap = generate_roadmap(missing_skills, weights, duration_days=30)

for week, skills in roadmap.items():
    print(week, ":", skills)

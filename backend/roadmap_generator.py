from collections import defaultdict

def prioritize_skills(missing_skills, weights):
    return sorted(
        missing_skills,
        key=lambda skill: weights.get(skill, 1),
        reverse=True
    )

def generate_roadmap(missing_skills, weights, duration_days=30):
    prioritized = prioritize_skills(missing_skills, weights)

    weeks = duration_days // 7
    roadmap = defaultdict(list)

    for i, skill in enumerate(prioritized):
        week = (i % weeks) + 1
        roadmap[f"Week {week}"].append(skill)

    return roadmap

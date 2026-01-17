import subprocess

def generate_ai_roadmap(prioritized_skills, duration_days=30):
    skills_text = ", ".join(prioritized_skills)

    prompt = f"""
You are a career mentor AI.

Create a {duration_days}-day learning roadmap for a student with the following missing skills:
{skills_text}

Rules:
- Prioritize important skills first
- Divide learning week-wise
- For each skill, explain why it is important
- Suggest one mini-project per skill
- Keep it beginner friendly
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        encoding="utf-8",
        capture_output=True
    )

    return result.stdout

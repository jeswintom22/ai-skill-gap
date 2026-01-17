import subprocess
import logging

logger = logging.getLogger(__name__)

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

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            text=True,
            encoding="utf-8",
            capture_output=True,
            timeout=60  # Add timeout
        )

        if result.returncode != 0:
            logger.error(f"Ollama error: {result.stderr}")
            return "Error: Could not generate AI roadmap. Please ensure Ollama is running."

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        logger.error("Ollama request timed out")
        return "Error: AI roadmap generation timed out."
    except FileNotFoundError:
        logger.error("Ollama not found")
        return "Error: Ollama not installed or not in PATH."
    except Exception as e:
        logger.error(f"Unexpected error in AI roadmap generation: {e}")
        return f"Error: {str(e)}"

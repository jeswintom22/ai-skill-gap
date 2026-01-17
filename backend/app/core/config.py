from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Skill Gap Analyzer"
    version: str = "1.0.0"
    description: str = "AI-powered skill gap analysis and learning roadmap"
    
    # File paths
    skills_db_path: str = "../data/skills.json"
    weights_db_path: str = "../data/skill_weights.json"
    
    # Ollama settings
    ollama_model: str = "mistral"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
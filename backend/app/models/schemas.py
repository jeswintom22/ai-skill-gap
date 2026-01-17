from pydantic import BaseModel
from typing import List


class SkillGapAnalysis(BaseModel):
    missing_skills: List[str]
    readiness_score: float


class AnalysisResponse(BaseModel):
    user_skills: List[str]
    job_skills: List[str]
    analysis: SkillGapAnalysis
    ai_roadmap: str
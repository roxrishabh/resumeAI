from pydantic import BaseModel, Field


class BulletEvaluation(BaseModel):
    original_bullet: str
    score: int = Field(..., ge=0, le=10)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    improved_bullet: str


class BulletReport(BaseModel):
    overall_score: float
    strong_bullets: list[BulletEvaluation] = Field(default_factory=list)
    weak_bullets: list[BulletEvaluation] = Field(default_factory=list)
    summary: str
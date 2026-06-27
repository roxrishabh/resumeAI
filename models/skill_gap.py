from pydantic import BaseModel, Field


class SkillGapSchema(BaseModel):

    matched_skills: list[str] = Field(default_factory=list)

    missing_skills: list[str] = Field(default_factory=list)

    partial_matches: list[str] = Field(default_factory=list)

    match_percentage: float

    reasoning: str
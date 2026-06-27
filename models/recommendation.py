from pydantic import BaseModel, Field


class RecommendationSchema(BaseModel):

    priority_changes: list[str] = Field(default_factory=list)

    keyword_additions: list[str] = Field(default_factory=list)

    bullet_improvements: list[str] = Field(default_factory=list)

    formatting_changes: list[str] = Field(default_factory=list)

    skills_to_highlight: list[str] = Field(default_factory=list)

    skills_missing: list[str] = Field(default_factory=list)

    overall_strategy: str
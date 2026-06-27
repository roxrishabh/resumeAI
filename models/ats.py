from pydantic import BaseModel, Field


class ATSReport(BaseModel):

    score: int

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    formatting_issues: list[str] = Field(default_factory=list)

    keyword_coverage: float

    recommendations: list[str] = Field(default_factory=list)
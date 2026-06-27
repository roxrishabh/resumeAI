from pydantic import BaseModel, Field


class JobRequirement(BaseModel):
    skill: str
    required: bool = True
    category: str = ""


class JDSchema(BaseModel):

    job_title: str = ""

    company: str = ""

    experience_required: str = ""

    education_required: str = ""

    responsibilities: list[str] = Field(default_factory=list)

    required_skills: list[JobRequirement] = Field(default_factory=list)

    preferred_skills: list[str] = Field(default_factory=list)

    tools: list[str] = Field(default_factory=list)

    programming_languages: list[str] = Field(default_factory=list)

    frameworks: list[str] = Field(default_factory=list)

    soft_skills: list[str] = Field(default_factory=list)

    keywords: list[str] = Field(default_factory=list)
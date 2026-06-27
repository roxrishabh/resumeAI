from pydantic import BaseModel, Field


class Education(BaseModel):
    degree: str = Field(default="")
    institution: str = Field(default="")
    duration: str = Field(default="")


class Experience(BaseModel):
    company: str = Field(default="")
    role: str = Field(default="")
    duration: str = Field(default="")
    responsibilities: list[str] = []


class Project(BaseModel):
    title: str = Field(default="")
    description: str = Field(default="")
    technologies: list[str] = []


class ResumeSchema(BaseModel):

    name: str

    email: str = ""

    phone: str = ""

    linkedin: str = ""

    github: str = ""

    summary: str = ""

    education: list[Education]

    skills: list[str]

    experience: list[Experience]

    projects: list[Project]

    achievements: list[str]

    certifications: list[str]
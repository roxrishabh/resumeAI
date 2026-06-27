from typing import TypedDict

class ResumeState(TypedDict):

    resume_path: str

    jd_path: str

    resume_text: str

    jd_text: str

    parsed_resume: dict

    parsed_jd: dict

    skill_gap: dict

    ats_report: dict

    bullet_report: dict

    recommendations: dict
    recommendation_plan: dict
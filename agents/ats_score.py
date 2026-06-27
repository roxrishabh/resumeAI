from llm import llm

from models.ats import ATSReport
from prompts.ats_prompt import ATS_PROMPT

structured_llm = llm.with_structured_output(ATSReport)


def ats_checker(state):

    print("Running ATS Evaluation...")

    response = structured_llm.invoke(
        [
            ("system", ATS_PROMPT),
            (
                "human",
                f"""
Resume

{state["parsed_resume"]}

Job Description

{state["parsed_jd"]}
"""
            )
        ]
    )

    return {
        "ats_report": response.model_dump()
    }
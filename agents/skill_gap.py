from llm import llm

from prompts.skill_gap_prompt import SKILL_GAP_PROMPT

from models.skill_gap import SkillGapSchema


structured_llm = llm.with_structured_output(
    SkillGapSchema
)


def analyze_skill_gap(state):

    print("Analyzing Skill Gap...")

    resume = state["parsed_resume"]

    jd = state["parsed_jd"]

    response = structured_llm.invoke(
        [
            ("system", SKILL_GAP_PROMPT),
            (
                "human",
                f"""
Resume:

{resume}

Job Description:

{jd}
"""
            ),
        ]
    )

    print("✓ Skill Gap Analysis Complete")

    return {
        "skill_gap": response.model_dump()
    }
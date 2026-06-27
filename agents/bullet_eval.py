from llm import llm

from prompts.bullet_eval_prompt import BULLET_EVALUATOR_PROMPT
from models.bullet_eval import BulletReport

structured_llm = llm.with_structured_output(BulletReport)


def evaluate_bullets(state):

    print("Evaluating Resume Bullets...")

    resume = state["parsed_resume"]

    response = structured_llm.invoke(
        [
            (
                "system",
                BULLET_EVALUATOR_PROMPT,
            ),
            (
                "human",
                f"""
Resume:

{resume}
"""
            ),
        ]
    )

    print("✓ Bullet Evaluation Complete")

    return {
        "bullet_report": response.model_dump()
    }
from llm import llm

from models.resume import ResumeSchema

from prompts.resume_prompt import RESUME_ANALYZER_PROMPT


structured_llm = llm.with_structured_output(ResumeSchema)


def analyze_resume(state):

    response = structured_llm.invoke(

        [
            (
                "system",
                RESUME_ANALYZER_PROMPT,
            ),
            (
                "human",
                state["resume_text"],
            ),
        ]
    )

    return {
        "parsed_resume": response.model_dump()
    }
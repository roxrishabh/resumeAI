from llm import llm

from models.jd import JDSchema
from prompts.jd_prompt import JD_ANALYZER_PROMPT


structured_llm = llm.with_structured_output(JDSchema)


def analyze_job_description(state):

    response = structured_llm.invoke(
        [
            ("system", JD_ANALYZER_PROMPT),
            ("human", state["jd_text"]),
        ]
    )

    return {
        "parsed_jd": response.model_dump()
    }
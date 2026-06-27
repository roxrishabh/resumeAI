from llm import llm

from prompts.recommendation_prompt import RECOMMENDATION_PROMPT

from models.recommendation import RecommendationSchema

structured_llm = llm.with_structured_output(RecommendationSchema)


def generate_recommendations(state):
    print("Generating Optimization Plan...")
    response = structured_llm.invoke(
        [
            ("system", RECOMMENDATION_PROMPT),
            ("human",
                    f"""
                    ATS Report

                    {state["ats_report"]}


                    Skill Gap

                    {state["skill_gap"]}


                    Bullet Report

                    {state["bullet_report"]}
                    """)
        ]
    )

    print("✓ Recommendation Plan Ready")

    return {"recommendation_plan": response.model_dump()}
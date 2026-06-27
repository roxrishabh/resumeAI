def merge_results(state):

    print("Merging Results...")

    return {

        "recommendations": {

            "skill_gap": state["skill_gap"],

            "ats": state["ats_report"],

            "bullet_feedback": state["bullet_report"]

        }

    }
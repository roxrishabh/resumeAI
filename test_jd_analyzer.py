from agents.jd_parser import parse_job_description
from agents.jd_analyzer import analyze_job_description

state = {
    "jd_path": "D:\\ResumeAI\\jd\\Electronic Arts.docx"
}

# Parse the JD
state.update(parse_job_description(state))

# Analyze the JD
state.update(analyze_job_description(state))

from pprint import pprint

pprint(state["parsed_jd"])
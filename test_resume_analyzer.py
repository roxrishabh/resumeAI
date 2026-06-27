from agents.resume_parser import parse_resume
from agents.resume_analyzer import analyze_resume

state = {
    "resume_path": "D:\\ResumeAI\\resume\\Rishabh_Srivastava_FlowCV_Resume_2026-06-26.pdf"
}

# Parse the resume
state.update(parse_resume(state))

# Analyze it
state.update(analyze_resume(state))

print(state["parsed_resume"])
from agents.resume_parser import parse_resume

state = {
    "resume_path": "D:\\ResumeAI\\resume\\Rishabh_Srivastava_FlowCV_Resume_2026-06-26.pdf"
}

result = parse_resume(state)

print(result["resume_text"][:1000])
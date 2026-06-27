from langgraph.graph import StateGraph, START, END

from state import ResumeState

from agents.resume_parser import parse_resume
from agents.jd_parser import parse_job_description
from agents.resume_analyzer import analyze_resume
from agents.jd_analyzer import analyze_job_description


builder = StateGraph(ResumeState)

# Nodes
builder.add_node("resume_parser", parse_resume)
builder.add_node("jd_parser", parse_job_description)
builder.add_node("resume_analyzer", analyze_resume)
builder.add_node("jd_analyzer", analyze_job_description)

# Flow
builder.add_edge(START, "resume_parser")

builder.add_edge("resume_parser", "jd_parser")

builder.add_edge("jd_parser", "resume_analyzer")

builder.add_edge("resume_analyzer", "jd_analyzer")

builder.add_edge("jd_analyzer", END)

graph = builder.compile()
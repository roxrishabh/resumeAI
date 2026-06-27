from langgraph.graph import StateGraph, START, END

from state import ResumeState

from agents.resume_parser import parse_resume
from agents.jd_parser import parse_job_description
from agents.resume_analyzer import analyze_resume
from agents.jd_analyzer import analyze_job_description
from agents.skill_gap import analyze_skill_gap
from agents.ats_score import ats_checker
from agents.bullet_eval import evaluate_bullets
from agents.merge_results import merge_results
from agents.recommendation_agent import generate_recommendations

builder = StateGraph(ResumeState)

# Nodes
builder.add_node("resume_parser", parse_resume)
builder.add_node("jd_parser", parse_job_description)
builder.add_node("resume_analyzer", analyze_resume)
builder.add_node("jd_analyzer", analyze_job_description)
builder.add_node("skill_gap", analyze_skill_gap)
builder.add_node("ats_checker", ats_checker)
builder.add_node("bullet_evaluator", evaluate_bullets)
builder.add_node("merge_results", merge_results)
builder.add_node("planner", generate_recommendations)

# Flow
builder.add_edge(START, "resume_parser")

builder.add_edge("resume_parser", "jd_parser")

builder.add_edge("jd_parser", "resume_analyzer")

builder.add_edge("resume_analyzer", "jd_analyzer")

builder.add_edge("jd_analyzer", "skill_gap")
builder.add_edge("jd_analyzer", "ats_checker")
builder.add_edge("jd_analyzer", "bullet_evaluator")

builder.add_edge("skill_gap", "planner")
builder.add_edge("ats_checker", "planner")
builder.add_edge("bullet_evaluator", "planner")

builder.add_edge("planner", END)

graph = builder.compile()
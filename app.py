from pprint import pprint

from graph import graph

initial_state = {

    "resume_path": "D:\\ResumeAI\\resume\\Rishabh_Srivastava_FlowCV_Resume_2026-06-26.pdf",

    "jd_path": "D:\\ResumeAI\\jd\\Electronic Arts.docx",

}

result = graph.invoke(initial_state)

from graph import graph

png = graph.get_graph().draw_mermaid_png()

with open("workflow.png", "wb") as f:
    f.write(png)

    
print("\nParsed Resume\n")
pprint(result["parsed_resume"])

print("\nParsed JD\n")
pprint(result["parsed_jd"])
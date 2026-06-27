from pathlib import Path

from parsers.pdf_parser import parse_pdf
from parsers.docx_parser import parse_docx


SUPPORTED_FORMATS = {
    ".pdf": parse_pdf,
    ".docx": parse_docx,
}


def parse_resume(state):
    """
    LangGraph node.

    Reads the resume from disk and stores
    the extracted text inside the graph state.
    """

    resume_path = Path(state["resume_path"])

    suffix = resume_path.suffix.lower()

    if suffix not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported resume format: {suffix}"
        )

    parser = SUPPORTED_FORMATS[suffix]

    resume_text = parser(str(resume_path))

    if not resume_text.strip():
        raise ValueError("Resume appears to be empty.")

    return {
        "resume_text": resume_text
    }
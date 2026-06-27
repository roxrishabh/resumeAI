from pathlib import Path

from parsers.pdf_parser import parse_pdf
from parsers.docx_parser import parse_docx


SUPPORTED_FORMATS = {
    ".pdf": parse_pdf,
    ".docx": parse_docx,
}


def parse_job_description(state):

    jd_path = Path(state["jd_path"])

    suffix = jd_path.suffix.lower()

    if suffix not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported JD format: {suffix}"
        )

    parser = SUPPORTED_FORMATS[suffix]

    jd_text = parser(str(jd_path))

    if not jd_text.strip():
        raise ValueError("Job Description is empty.")

    return {
        "jd_text": jd_text
    }
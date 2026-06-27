from docx import Document


def parse_docx(file_path: str) -> str:
    """
    Extract text from a DOCX resume.
    """

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:

        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)
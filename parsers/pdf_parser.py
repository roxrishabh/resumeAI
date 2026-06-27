import fitz  # PyMuPDF


def parse_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_path: Path to the PDF resume.

    Returns:
        Extracted text as a single string.
    """

    document = fitz.open(file_path)

    pages = []

    for page in document:
        text = page.get_text("text")

        if text.strip():
            pages.append(text)

    document.close()

    return "\n".join(pages)
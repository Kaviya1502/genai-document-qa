from pypdf import PdfReader


def load_pdf(file_path: str):
    """
    Load a PDF and extract its text page by page.
    """

    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages):
        # Ignore the reference section at the end of the paper
        if page_number + 1 > 16:
            continue

        text = page.extract_text() or ""

        documents.append(
            {
                "page_content": text,
                "metadata": {
                    "source": file_path,
                    "page": page_number + 1,
                },
            }
        )

    return documents


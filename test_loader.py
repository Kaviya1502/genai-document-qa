from src.document_loader import load_pdf


pdf_path = "data/sample.pdf"

documents = load_pdf(pdf_path)

print(f"Number of pages loaded: {len(documents)}")

for document in documents[:2]:
    print("\n--- Page ---")
    print(document["page_content"][:500])
    print("\nMetadata:")
    print(document["metadata"])
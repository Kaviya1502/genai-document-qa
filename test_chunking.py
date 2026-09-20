from src.document_loader import load_pdf
from src.text_splitter import split_documents


pdf_path = "data/sample.pdf"

documents = load_pdf(pdf_path)

chunks = split_documents(documents)

print(f"Number of pages: {len(documents)}")
print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk.page_content[:500])
    print("\nMetadata:")
    print(chunk.metadata)
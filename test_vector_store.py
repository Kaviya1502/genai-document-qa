from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store


pdf_path = "data/sample.pdf"

documents = load_pdf(pdf_path)

chunks = split_documents(documents)

print(f"Pages loaded: {len(documents)}")
print(f"Chunks created: {len(chunks)}")

print("\nCreating vector store...")

vector_store = create_vector_store(chunks)

print("Vector store created successfully!")
from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store


pdf_path = "data/sample.pdf"

print("Loading PDF...")

documents = load_pdf(pdf_path)

print(f"Pages loaded: {len(documents)}")

print("\nSplitting document...")

chunks = split_documents(documents)

print(f"Chunks created: {len(chunks)}")

print("\nCreating vector store...")

vector_store = create_vector_store(chunks)

print("Vector store created!")

question = "What is RAG?"

print(f"\nQuestion: {question}")

results = vector_store.similarity_search(
    question,
    k=4
)

print("\n========== RETRIEVED CHUNKS ==========\n")

for i, result in enumerate(results):

    print(
        f"--- Chunk {i + 1} | "
        f"Page {result.metadata['page']} ---"
    )

    print(result.page_content[:1000])

    print("\n")

print("======================================")
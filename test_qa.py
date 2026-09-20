from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.qa_chain import answer_question


# Load PDF
pdf_path = "data/sample.pdf"

documents = load_pdf(pdf_path)

# Split into chunks
chunks = split_documents(documents)

# Create FAISS vector store
vector_store = create_vector_store(chunks)

# Ask a question
question = "What are the limitations of Retrieval-Augmented Generation?"

# Get answer
answer, sources = answer_question(
    vector_store,
    question
)

print("\n================ ANSWER ================\n")
print(answer)

print("\n================ SOURCES ================\n")

for source in sources:
    print(f"Page: {source.metadata['page']}")
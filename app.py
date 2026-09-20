import streamlit as st

from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.qa_chain import answer_question


st.set_page_config(
    page_title="GenAI Document Q&A",
    page_icon="📄",
    layout="wide"
)


st.title("📄 GenAI Document Q&A Assistant")

st.write(
    "Upload a PDF and ask questions about its contents using "
    "Retrieval-Augmented Generation (RAG)."
)


uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    # Save the uploaded PDF temporarily
    file_path = "uploaded_document.pdf"

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    # Store the vector store in session state
    # so it is created only once per uploaded document
    if "vector_store" not in st.session_state:

        with st.spinner("Processing document..."):

            documents = load_pdf(file_path)

            chunks = split_documents(documents)

            vector_store = create_vector_store(chunks)

            st.session_state.vector_store = vector_store
            st.session_state.page_count = len(documents)
            st.session_state.chunk_count = len(chunks)

    vector_store = st.session_state.vector_store

    st.success(
        f"Document processed: "
        f"{st.session_state.page_count} pages and "
        f"{st.session_state.chunk_count} chunks created."
    )

    # Question input
    question = st.text_input(
        "Ask a question about the document:"
    )

    if question:

        with st.spinner("Finding the answer..."):

            answer, sources = answer_question(
                vector_store,
                question
            )

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        pages = sorted(
            set(
                source.metadata["page"]
                for source in sources
            )
        )

        for page in pages:
            st.write(f"📄 Page {page}")
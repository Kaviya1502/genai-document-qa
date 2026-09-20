from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller chunks for retrieval.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.create_documents(
        [doc["page_content"] for doc in documents],
        metadatas=[doc["metadata"] for doc in documents],
    )

    return chunks
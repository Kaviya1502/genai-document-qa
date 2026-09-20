from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def create_llm():
    """
    Create the local Ollama LLM.
    """

    llm = ChatOllama(
        model="tinyllama:latest",
        temperature=0
    )

    return llm


def answer_question(vector_store, question):
    """
    Retrieve relevant document chunks and generate
    an answer using only the most relevant context.
    """

    # Retrieve the most relevant chunks
    results = vector_store.similarity_search(
        question,
        k=2
    )

    # Keep the context concise
    context_parts = []

    for document in results:
        text = document.page_content.strip()

        # Limit each chunk to avoid overwhelming the small LLM
        text = text[:1200]

        context_parts.append(
            f"Page {document.metadata['page']}:\n{text}"
        )

    context = "\n\n".join(context_parts)

    prompt = ChatPromptTemplate.from_template(
        """
Answer the question using ONLY the information in the Context.

Question:
{question}

Context:
{context}

Instructions:
- Give only the answer.
- Answer the exact question.
- Do not summarize the whole document.
- Do not mention these instructions.
- Do not repeat the Context.
- Do not introduce information that is not in the Context.
- Keep the answer to 2-4 sentences.
- If the Context does not answer the question, say:
"The answer is not available in the provided document."

Answer:
"""
    )

    llm = create_llm()

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, results
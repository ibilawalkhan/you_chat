from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)
from langchain_core.output_parsers import StrOutputParser
from chat.prompts import RAGPROMPT
from chat.llm import create_llm


def format_docs(retrieved_docs):
    return "\n\n".join([doc.page_content for doc in retrieved_docs])


def create_rag_chain(retriever, llm=None):
    if llm is None:
        llm = create_llm()

    parallel_chain = RunnableParallel(
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
    )

    main_chain = parallel_chain | RAGPROMPT | llm | StrOutputParser()

    return main_chain

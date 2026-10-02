from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_classic.retrievers import (
    MultiQueryRetriever,
    ContextualCompressionRetriever,
)


def create_retriever(vector_store, llm):

    base_retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 20,
            "lambda_mult": 0.5,
        },
    )

    multi_query_retriever = MultiQueryRetriever.from_llm(
        retriever=base_retriever,
        llm=llm,
    )

    compressor = LLMChainExtractor.from_llm(llm)

    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=multi_query_retriever,
    )

    return compression_retriever

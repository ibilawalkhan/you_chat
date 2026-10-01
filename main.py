from ingestion.transcript import get_transcript
from retrieval.chunking import split_transcript
from retrieval.vector_store import create_vector_store
from retrieval.retriever import create_retriever
from chat.chain import create_rag_chain
from dotenv import load_dotenv

load_dotenv()

video_id = "Gfr50f6ZBvo"

transcript = get_transcript(video_id)

chunks = split_transcript(transcript)

vector_store = create_vector_store(chunks)

retriever = create_retriever(vector_store)

rag_chain = create_rag_chain(retriever)     

question = "What is the main topic of discussion in this video?"

answer = rag_chain.invoke(question)

print(f"Question: {question}")
print(f"Answer: {answer}")
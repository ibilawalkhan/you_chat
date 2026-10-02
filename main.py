from ingestion.transcript import get_transcript
from retrieval.chunking import split_transcript
from retrieval.vector_store import create_vector_store
from retrieval.retriever import create_retriever
from chat.chain import create_rag_chain
from chat.llm import create_llm
from dotenv import load_dotenv

load_dotenv()

video_id = "Gfr50f6ZBvo"

transcript = get_transcript(video_id)

print("Transcript characters:", len(transcript))
print("Transcript preview:", transcript[:500])

chunks = split_transcript(transcript)

print("Number of chunks:", len(chunks))

vector_store = create_vector_store(chunks)

llm = create_llm()

retriever = create_retriever(vector_store, llm=llm)

docs = retriever.invoke("What is the main topic of discussion in this video?")

print("\n========== RETRIEVED DOCUMENTS ==========\n")

for i, doc in enumerate(docs, 1):
    print(f"\n--- Document {i} ---")
    print(doc.page_content)

rag_chain = create_rag_chain(
    retriever,
    llm=llm,
)

question = "What is the main topic of discussion in this video?"

answer = rag_chain.invoke(question)

print(f"Question: {question}")
print(f"Answer: {answer}")

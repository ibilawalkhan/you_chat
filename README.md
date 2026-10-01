🎙️ Youchat

Chat with YouTube podcasts and videos using RAG (Retrieval-Augmented Generation).

Youchat lets users provide a YouTube video URL and ask questions about the video's content. The application retrieves the video's transcript, splits it into meaningful chunks, creates vector embeddings, retrieves relevant sections, and uses Gemini to generate answers grounded in the transcript.

🚀 How It Works
YouTube URL
     │
     ▼
YouTube Transcript
     │
     ▼
Text Chunking
     │
     ▼
Hugging Face Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Similarity Retriever
     │
     ▼
Relevant Transcript Chunks
     │
     ▼
RAG Prompt
     │
     ▼
Gemini Flash
     │
     ▼
Answer


The goal is to allow users to interact with long-form content such as:

Podcasts

Interviews

Lectures

Educational videos

Conference talks

Tutorials

Discussions

🛠️ Tech Stack

Python — Application language

YouTube Transcript API — Retrieves video transcripts

LangChain — RAG pipeline and orchestration

Hugging Face Sentence Transformers — Local text embeddings

FAISS — Vector similarity search

Google Gemini — Answer generation

Git — Version control

📁 Project Structure
pod_chat/
│
├── chat/
│   ├── __init__.py
│   ├── chain.py
│   └── prompts.py
│
├── ingestion/
│   ├── __init__.py
│   └── transcript.py
│
├── retrieval/
│   ├── __init__.py
│   ├── chunking.py
│   ├── retriever.py
│   └── vector_store.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md

Responsibilities

ingestion/

Handles obtaining the transcript from YouTube.

retrieval/chunking.py

Splits the transcript into smaller documents suitable for embedding and retrieval.

retrieval/vector_store.py

Creates embeddings and stores them in a FAISS vector store.

retrieval/retriever.py

Configures the retriever used to find relevant transcript chunks.

chat/prompts.py

Contains the prompt used to instruct the language model.

chat/chain.py

Builds the RAG pipeline that connects retrieval, prompting, and Gemini.

main.py

Orchestrates the complete pipeline.

⚙️ Setup
1. Clone the repository
git clone <your-repository-url>
cd pod_chat

2. Create a virtual environment
python -m venv .venv


Activate it on Git Bash:

source .venv/Scripts/activate


On Windows Command Prompt:

.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file:

GOOGLE_API_KEY=your_google_api_key


Never commit .env to Git.

The project includes .env in .gitignore to prevent accidentally exposing API keys.

5. Run the application
python main.py

🧠 Current RAG Pipeline

The current implementation uses:

1. Transcript ingestion

A YouTube video ID is used to retrieve the available transcript.

2. Chunking

The transcript is split using RecursiveCharacterTextSplitter.

Current configuration:

chunk_size=1000
chunk_overlap=200

3. Embeddings

Transcript chunks are embedded locally using:

sentence-transformers/all-MiniLM-L6-v2


This avoids sending the transcript to an external embedding API.

4. Vector storage

The resulting embeddings are stored in:

FAISS

5. Retrieval

The current retriever uses similarity search:

search_type="similarity"
k=4


Four relevant chunks are retrieved for each question.

6. Generation

The retrieved transcript context is passed to Gemini with instructions to answer only from the provided context.

🔐 Grounded Responses

The RAG prompt instructs the model:

Answer ONLY from the provided transcript context.
If the context is insufficient, just say you don't know.


This is intended to reduce answers based on information outside the video's transcript.

However, RAG does not guarantee that every answer will be correct. Retrieval quality is an important part of the system and will be evaluated and improved as the project develops.

🧪 Planned Improvements

The initial implementation focuses on getting the basic RAG pipeline working.

Potential improvements include:

 Accept complete YouTube URLs instead of only video IDs

 Better transcript error handling

 Persist FAISS indexes

 Avoid regenerating embeddings for the same video

 Improve chunking strategy

 Experiment with MMR retrieval

 Add MultiQueryRetriever

 Add ContextualCompressionRetriever

 Evaluate retrieval quality

 Add conversation history

 Support multiple videos

 Add a web interface

 Add transcript timestamps to answers

 Add source references to retrieved transcript sections

 Add automated tests

 Deploy the application

⚠️ Important Edge Cases

The application needs to account for several practical cases:

YouTube / Transcript

Transcripts disabled

No transcript available

Requested language unavailable

Invalid, private, or deleted videos

YouTube/API/network errors

Chunking

Empty transcripts

Very short transcripts

Extremely long transcripts

Embeddings

Model download/authentication failures

Network failures

Large numbers of chunks

Embedding API rate limits when using hosted embedding models

Retrieval

No sufficiently relevant chunks

Relevant information not being retrieved

Too few retrieved chunks

Too many irrelevant chunks

Generation

Retrieved context does not contain the answer

Conflicting information within the retrieved context

Excessively large context

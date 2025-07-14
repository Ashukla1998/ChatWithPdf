# qa_engine.py

import os
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from chromadb.config import Settings
from gpt4all import GPT4All

# === 1. Load Embedding Model ===
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# === 2. Initialize Vector DB ===
chroma_client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = chroma_client.get_or_create_collection("pdf_chunks")

# === 3. Load LLM from local .gguf ===
MODEL_NAME = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"
MODEL_DIR = os.path.join(os.getcwd(), "model")  # <- Folder must be named "models"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

llm = GPT4All(
    model_name=MODEL_NAME,
    model_path=MODEL_DIR,
    allow_download=False  # ✅ prevent trying to fetch online (causing 404)
)

# === 4. PDF to Text ===
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = " ".join([page.get_text() for page in doc])
    return text

# === 5. Text to Embeddings + Store in Chroma ===
def process_pdf(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    embeddings = embedding_model.encode(chunks).tolist()

    for i, chunk in enumerate(chunks):
        collection.add(documents=[chunk], embeddings=[embeddings[i]], ids=[str(i)])
    return True

# === 6. Handle Question + Generate Answer ===
def get_answer(query):
    query_embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    context = "\n".join(results["documents"][0])

    prompt = f"""### Instruction:
Answer the following question based on the context below:

### Context:
{context}

### Question:
{query}

### Answer:"""

    with llm.chat_session():
        response = llm.generate(prompt)
    return response

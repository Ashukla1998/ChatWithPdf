# 🤖 PDF Question Answering Chatbot (100% Local & Free)

This project is a local, privacy-focused chatbot that can answer questions about any uploaded PDF document using:

- 🧠 Local Language Models (Mistral-7B)
- 📚 Embedding with `sentence-transformers`
- 🔍 Context Retrieval via `ChromaDB`
- 🌐 Interactive UI built with `Streamlit`

> ✅ No internet access or OpenAI API key required  
> ✅ 100% free and offline — perfect for personal, secure, or enterprise use cases

---

## 🚀 Features

- 📥 Upload any PDF document
- 💬 Ask natural language questions about its content
- 🧠 Uses a local LLM (like Mistral) via `gpt4all`
- 🔐 Works entirely offline

---

## 🧰 Tech Stack

| Component              | Tool / Library                     |
|------------------------|------------------------------------|
| PDF Parsing            | PyMuPDF (`fitz`)                   |
| Text Embedding         | `sentence-transformers` (MiniLM)   |
| Vector Store           | `ChromaDB`                         |
| Language Model         | `Mistral-7B` GGUF via `gpt4all`    |
| Frontend UI            | `Streamlit`                        |
| LLM Inference Backend  | `gpt4all` (precompiled, no build)  |

---

## 📂 Folder Structure


---

## 🔧 Installation

### 1. 🐍 Clone the repository

```bash
git clone https://github.com/Ashukla1998/pdf-qa-chatbot.git
cd pdf-qa-chatbot

Install dependencies
pip install streamlit
pip install chromadb
pip install sentence-transformers
pip install PyMuPDF
pip install langchain
pip install gpt4all

Download a GGUF model
Visit: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

Download a file like: mistral-7b-instruct-v0.1.Q4_K_M.gguf

Place it in the models/ folder

Run the app
streamlit run app.py

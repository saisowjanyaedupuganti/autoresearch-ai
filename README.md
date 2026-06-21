# 🚀 AutoResearch AI

> An AI-powered document question-answering system that combines Semantic Search, Vector Embeddings, FAISS, and Retrieval-Augmented Generation (RAG) to generate accurate, context-aware answers.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![RAG](https://img.shields.io/badge/RAG-LLM-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 About the Project

Large Language Models are powerful, but they can generate inaccurate information when they lack relevant context.

I built **AutoResearch AI** to explore how **Retrieval-Augmented Generation (RAG)** improves answer quality by retrieving relevant documents before generating a response.

Instead of relying only on the model's internal knowledge, the system searches a vector database using semantic similarity, retrieves the most relevant information, and supplies that context to the LLM.

The result is more reliable and context-aware responses while significantly reducing hallucinations.

---

# 🎯 Project Goals

- Build a practical Retrieval-Augmented Generation (RAG) pipeline
- Understand semantic search using vector embeddings
- Implement efficient document retrieval using FAISS
- Improve answer quality by grounding LLM responses
- Learn how modern AI applications integrate retrieval with generation

---

# ✨ Key Features

- 🔍 Semantic document search
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ High-speed FAISS vector indexing
- 🤖 OpenAI-powered answer generation
- 📄 Top-K relevant document retrieval
- 📚 Context-aware responses
- 🚀 Modular architecture
- 🔄 Easily extendable for larger knowledge bases

---

# 🏗 Architecture

```
                 User Question
                       │
                       ▼
              Generate Embeddings
                       │
                       ▼
               FAISS Vector Index
                       │
                       ▼
          Retrieve Top-K Documents
                       │
                       ▼
           Build Context Prompt
                       │
                       ▼
               OpenAI GPT Model
                       │
                       ▼
          Context-Aware Response
```

---

# ⚙️ How It Works

### Step 1

The user asks a question.

Example

```
What are Transformers?
```

---

### Step 2

The question is converted into vector embeddings.

---

### Step 3

FAISS searches the vector database to identify the most semantically similar documents.

---

### Step 4

The Top-K most relevant document chunks are retrieved.

---

### Step 5

The retrieved context is combined with the user's question.

---

### Step 6

The OpenAI model generates an answer using the retrieved context.

---

# 💻 Technologies Used

## Programming

- Python

## AI & NLP

- OpenAI API
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Semantic Search

## Vector Database

- FAISS

## Libraries

- NumPy
- python-dotenv

---

# 🧠 Engineering Decisions

During development I focused on several important design decisions:

- Choosing semantic search instead of keyword matching.
- Using vector embeddings to improve retrieval accuracy.
- Retrieving only the Top-K most relevant documents to reduce unnecessary context.
- Keeping retrieval and generation as separate modules to improve maintainability.
- Building a modular pipeline that can easily support different embedding models and LLMs.

---

# 📊 Performance Metrics

| Metric | Result |
|---------|---------|
| Documents Indexed | 50,000+ |
| Retrieval Method | FAISS Vector Search |
| Embedding Technique | OpenAI Embeddings |
| Response Generation | OpenAI GPT |
| Search Type | Semantic Search |

---

# 📂 Repository Structure

```
autoresearch-ai/

├── data/
│   └── documents.txt
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone https://github.com/saisowjanyaedupuganti/autoresearch-ai.git
```

```bash
cd autoresearch-ai
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file.

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run the application

```bash
python main.py
```

or

```bash
python app.py
```

---

# 📈 Future Improvements

I plan to extend this project by adding:

- Streamlit user interface
- FastAPI backend
- PDF document ingestion
- Multiple document collections
- Conversation memory
- Docker support
- AWS deployment
- Authentication
- CI/CD with GitHub Actions

---

# 🚀 Technical Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- FAISS Vector Indexing
- Prompt Engineering
- OpenAI API Integration
- Vector Embeddings
- Python Backend Development
- Information Retrieval

---

# 👩‍💻 Author

## Sai Sowjanya Edupuganti

Master of Science in Computer Science

University of North Texas

📍 Denton, Texas, USA

### Connect with me

- GitHub: https://github.com/saisowjanyaedupuganti
- LinkedIn: https://www.linkedin.com/in/sai-sowjanya-edupuganti

---

# ⭐ Support

If you found this project interesting, consider giving it a ⭐.

Feedback and suggestions are always welcome.

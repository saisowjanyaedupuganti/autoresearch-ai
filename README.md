# AutoResearch AI 🚀

This project is my attempt to understand how semantic search works behind the scenes.

Instead of relying only on exact keyword matching, this system tries to understand the meaning of the query and return more relevant results using vector similarity.

---

## What this project does

- Reads text data from a local file
- Converts each text entry into a vector representation
- Stores those vectors using FAISS
- Takes a user query as input
- Returns the most relevant matches based on similarity

---

## Progress

### Day 1

- Set up the project structure
- Learned how virtual environments work
- Built the first version of the semantic search system
- Used FAISS for similarity search
- Tested the system with sample AI/ML-related queries

### Day 2

- Improved the project structure
- Added `.env` for configuration
- Made the system interactive so multiple queries can be asked in one run
- Cleaned up the code into smaller functions
- Uploaded the project to GitHub

---
### Day 4
- Added final answer generation using retrieved results
- Combined top search results into a single response
- Improved output structure with a clear "Final Answer" section
- Moved from basic search → retrieval + response system

## How it works

1. The system loads documents from `data/documents.txt`
2. Each line is converted into a vector using a custom embedding approach
3. All vectors are stored in a FAISS index
4. When the user asks a question, the query is also converted into a vector
5. FAISS finds the closest matching vectors
6. The system displays the top relevant results

## How to run

# bash
pip install -r requirements.txt
python main.py

## Project structure

```text
autoresearch-ai/
│
├── data/
│   └── documents.txt
├── main.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
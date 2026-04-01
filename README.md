AutoResearch AI
🧠 From Simple Search → Intelligent AI System

When I started this project, my goal was simple:
👉 build a basic search system that can find relevant information.

But as I progressed, I realized something important:

Retrieval alone is not intelligence.

So I pushed this project step by step — and by Day 5, it evolved into a system that can:

✔ understand
✔ filter
✔ generate meaningful answers

📌 Project Overview

AutoResearch AI is a semantic search + RAG (Retrieval-Augmented Generation) system that takes natural language queries and returns context-aware answers, instead of just showing raw text.

It simulates how modern AI systems like ChatGPT combine:

retrieval (finding relevant info)
generation (producing answers)
🛤️ My Learning Journey (Day 1 → Day 5)
🔹 Day 1 – Basic Setup
Set up Python project structure
Created document dataset (documents.txt)
Built simple file-based data loading

👉 At this stage, it was just reading text.

🔹 Day 2 – Text Processing
Implemented tokenization
Converted text into structured format
Started thinking in terms of "data → representation"

👉 Learned how raw text becomes usable data.

🔹 Day 3 – Embeddings & Vectorization
Built custom embedding function using hashing
Converted text into numerical vectors
Normalized embeddings

👉 This is where the system started understanding meaning instead of keywords

🔹 Day 4 – Semantic Search with FAISS
Integrated FAISS for fast similarity search
Implemented vector indexing
Retrieved Top-K relevant documents

👉 Now the system could search based on meaning, not exact words.

🔹 Day 5 – RAG (Retrieval + Generation)

This was the biggest shift.

Instead of just retrieving results:

I combined retrieval with an LLM
Built a context-aware answer generation system

👉 Now the system:

filters noise
focuses on relevant context
generates clean, human-like answers

⚙️ How the System Works
User Query
   ↓
Tokenization
   ↓
Embedding Generation
   ↓
FAISS Similarity Search
   ↓
Top-K Relevant Documents
   ↓
LLM (OpenAI)
   ↓
Final Answer (Context-aware)

🔍 Example

Question:

What are transformers?

Output:

Transformers are neural network architectures widely used in modern language models.

🔥 Key Features
Semantic search using vector embeddings
FAISS-based fast similarity search
Retrieval-Augmented Generation (RAG) pipeline
Context-aware answer generation
Noise filtering and relevance selection
Modular pipeline design

🧠 Concepts I Worked With
Vector Embeddings
Cosine Similarity
FAISS Indexing
Retrieval-Augmented Generation (RAG)
Prompt Engineering
Natural Language Processing (NLP)

🛠️ Tech Stack
Python
FAISS
NumPy
OpenAI API
dotenv
💡 What I Learned
This project completely changed how I think about AI systems.

I understood that:

👉 Search systems retrieve data
👉 AI systems understand + filter + generate
And the real power comes from combining all three.

🚀 Future Improvements
Improve retrieval quality with better embeddings
Add UI (Streamlit or web app)
Optimize performance for larger datasets
Introduce caching and ranking improvements

👩‍💻 About Me
I am actively learning and building projects in:
AI Engineering
Machine Learning
NLP

This project is part of my journey to build real-world AI systems.

⭐ Final Thought
Understanding + Filtering + Generating
is where real AI begins.

🚀 Run Locally
pip install -r requirements.txt
python main.py

🔐 Environment Setup
Create a .env file:
OPENAI_API_KEY=your_api_key_here


🧑‍💻 Author

Sai Sowjanya Edupuganti
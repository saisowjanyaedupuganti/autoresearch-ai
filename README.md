# AutoResearch AI 🚀

This project is my attempt to understand how semantic search works behind the scenes.

Instead of just matching keywords, this system tries to find results based on meaning using vector similarity.

---

## What I Built

- A local semantic search system  
- Converts text into vectors (custom embedding logic)  
- Uses FAISS for fast similarity search  
- Takes user queries and returns the most relevant results  

---

## Progress

### Day 1
- Built the base system  
- Learned how tokenization works  
- Created a simple embedding approach using hashing  
- Integrated FAISS to store and search vectors  

### Day 2
- Made the system interactive (can ask multiple questions)  
- Cleaned up and structured the code better  
- Added `.env` for configuration  
- Improved output formatting  

---

## How It Works (Simple)

1. Read text data from a file  
2. Convert each line into a vector  
3. Store vectors in FAISS  
4. Take user input  
5. Find closest matching vectors  
6. Show the results  

---

## Example

Input:
What are transformers?

Output:
Transformers are neural network architectures widely used in modern language models.

---

## How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
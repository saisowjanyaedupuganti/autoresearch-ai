import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from main import load_documents, build_index, search_documents

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME", "AutoResearch AI")
TOP_K = int(os.getenv("TOP_K", 1))
DATA_FILE = Path("data/documents.txt")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_final_answer(query, results):
    if not results:
        return "No relevant information found for the given query."

    context = "\n".join([item["document"] for item in results])

    prompt = f"""
You are an AI assistant.

Answer the question ONLY using relevant information.

Question:
{query}

Context:
{context}

Instructions:
- Ignore unrelated information
- Give a clear and concise answer
- Do not include irrelevant sentences

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()


@st.cache_resource
def load_system():
    documents = load_documents(DATA_FILE)
    index = build_index(documents)
    return documents, index

def main():
    st.set_page_config(
        page_title="AutoResearch AI",
        page_icon="🧠",
        layout="centered"
    )

    st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        margin: 0;
        color: black;
    }

    .sub-title {
        text-align: center;
        font-size: 22px;
        margin: 4px 0 4px 0;
        color: #444;
    }

    .desc-text {
        text-align: center;
        font-size: 16px;
        color: gray;
        margin: 0 0 6px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    documents, index = load_system()

    # ---------- TITLE ----------
    st.markdown("""
    <p class="main-title">🧠 AutoResearch AI</p>
    <p class="sub-title">Semantic Search + Retrieval-Augmented Generation (RAG)</p>
    <p class="desc-text">
    Ask anything. The system retrieves relevant context and generates a clean, intelligent answer.
    </p>
    """, unsafe_allow_html=True)

    # ---------- INPUT ----------
    query = st.text_input(
        "",
        placeholder="🔎 Ask anything... (e.g., What are transformers?)"
    )

    search = st.button("🚀 Generate Answer")

    # ---------- LOGIC ----------
    if search:

        if not query.strip():
            st.warning("Please enter a valid question.")
            return

        with st.spinner("🔎 Searching and generating answer..."):

            results = search_documents(index, documents, query, TOP_K)
            final_answer = generate_final_answer(query, results)

        # ---------- FINAL ANSWER ----------
        st.markdown("### 💡 Final Answer")
        st.success(final_answer)

        # ---------- RETRIEVED CONTEXT ----------
        st.markdown("### 📄 Retrieved Context")

        for item in results:
            st.markdown(f"""
            <div style="font-size:14px; margin-bottom:6px;">
            <b>Result {item['rank']}</b><br>
            <b>Score:</b> {item['score']:.4f}<br>
            <b>Text:</b> {item['document']}
            </div>
            """, unsafe_allow_html=True)

    # ---------- FOOTER ----------
    st.markdown(
        "<p style='text-align:center; color:gray; font-size:14px;'>Built with ❤️ using FAISS + OPENAI</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
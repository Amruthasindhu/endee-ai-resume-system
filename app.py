import streamlit as st
from utils.pdf_parser import extract_text
from utils.chunking import chunk_text
from backend.rag import add_documents, query_rag

st.title("AI Resume + Interview Assistant")

uploaded_file = st.file_uploader("Upload Resume (PDF)")

job_desc = st.text_area("Paste Job Description")

if uploaded_file:
    text = extract_text(uploaded_file)
    chunks = chunk_text(text)
    add_documents(chunks)
    st.success("Resume processed!")

question = st.text_input("Ask a question")

if st.button("Get Answer"):
    answer = query_rag(question)
    st.write(answer)
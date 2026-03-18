import streamlit as st
from utils.pdf_parser import extract_text
from utils.chunking import chunk_text
from backend.rag import add_documents, query_rag

st.set_page_config(page_title="AI Resume + Interview Assistant", layout="centered")
st.title("🤖 AI Resume + Interview Assistant")
st.markdown("Upload your resume and paste a job description to get a detailed eligibility analysis.")

# --- Upload Resume ---
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# --- Job Description ---
job_desc = st.text_area("📋 Paste Job Description", height=200, placeholder="Paste the full job description here...")

if uploaded_file and job_desc:
    with st.spinner("Processing resume..."):
        text = extract_text(uploaded_file)
        chunks = chunk_text(text)
        add_documents(chunks, job_desc)
    st.success("✅ Resume processed and indexed!")

    st.divider()
    st.subheader("📊 Resume Analysis")

    with st.spinner("Analyzing resume against job description..."):
        result = query_rag("Evaluate this resume against the job description.", job_desc)

    # Display structured output
    st.markdown(result)

    st.divider()
    st.subheader("💬 Ask a Custom Question")

question = st.text_input("Ask anything about the resume-job fit", placeholder="e.g. Is the candidate suitable for a senior role?")

if st.button("Get Answer"):
    if not uploaded_file or not job_desc:
        st.warning("Please upload a resume and paste a job description first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = query_rag(question, job_desc)
        st.markdown(answer)

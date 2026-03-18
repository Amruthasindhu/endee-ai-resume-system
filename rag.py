from backend.embeddings import get_embeddings
from backend.endee_store import EndeeStore
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

store = EndeeStore()

def add_documents(chunks, job_desc=""):
    """Embed resume chunks and optionally include job description as context."""
    store.clear()
    embeddings = get_embeddings(chunks)
    store.add(chunks, embeddings)

def query_rag(question, job_desc=""):
    """Retrieve relevant resume chunks and generate a structured evaluation."""
    query_embedding = get_embeddings([question])[0]
    results = store.search(query_embedding)

    resume_context = "\n".join(results)

    if question.lower().startswith("evaluate"):
        prompt = f"""
You are an expert AI recruiter and resume analyst.

**Job Description:**
{job_desc}

**Resume Content (relevant sections):**
{resume_context}

Carefully analyze the resume against the job description and provide the following structured output:

**Eligibility Score:** (a number from 0 to 100)

**Matched Skills:**
- List each matched skill on a new line starting with "- "

**Missing Skills:**
- List each missing skill on a new line starting with "- "

**Final Verdict:**
(One sentence summary: Eligible / Partially Eligible / Not Eligible — with a brief reason)

**Suggestions:**
- List each actionable suggestion on a new line starting with "- "

Be specific, honest, and constructive.
"""
    else:
        prompt = f"""
You are an expert AI recruiter and resume analyst.

**Job Description:**
{job_desc}

**Resume Content (relevant sections):**
{resume_context}

**Question:** {question}

Answer clearly and concisely, referencing specific details from the resume and job description where relevant.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response['choices'][0]['message']['content']

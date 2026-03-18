from backend.embeddings import get_embeddings
from backend.endee_store import EndeeStore
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

store = EndeeStore()

def add_documents(chunks):
    embeddings = get_embeddings(chunks)
    store.add(chunks, embeddings)

def query_rag(question):
    query_embedding = get_embeddings([question])[0]
    results = store.search(query_embedding)

    context = "\n".join(results)

    prompt = f"""
    You are an AI recruiter.

    Analyze the resume based on this context:

    {context}

    Question: {question}

    Give:
    - Match evaluation
    - Missing skills
    - Suggestions
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embeddings(texts):
    """Generate embeddings using OpenAI text-embedding-ada-002."""
    response = openai.Embedding.create(
        input=texts,
        model="text-embedding-ada-002"
    )
    return [item["embedding"] for item in response["data"]]

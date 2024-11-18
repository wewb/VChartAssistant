from langchain.embeddings import OpenAIEmbeddings
from src.config.config import config

def get_embeddings():
    return OpenAIEmbeddings(
        openai_api_key=config.OPENAI_API_KEY
    ) 
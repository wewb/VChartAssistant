from langchain.document_loaders import GitLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.config.config import config

class DocumentLoader:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP
        )
    
    def load_documents(self):
        # Load documents from VChart GitHub repository
        loader = GitLoader(
            repo_path=self.repo_path,
            branch=config.REPO_BRANCH,
            file_filter=lambda file_path: file_path.endswith(".md")
        )
        documents = loader.load()
        return self.text_splitter.split_documents(documents) 
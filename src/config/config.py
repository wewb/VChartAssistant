import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.GITHUB_REPO = "https://github.com/VisActor/VChart"
        self.REPO_BRANCH = "develop"
        self.DOCS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "docs")
        
        # API Settings
        self.HOST = "0.0.0.0"
        self.PORT = 8000
        
        # Embedding Settings
        self.CHUNK_SIZE = 1000
        self.CHUNK_OVERLAP = 200

config = Config() 
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
import os

class QAChain:
    def __init__(self, embeddings, documents):
        self.vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embeddings
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(
                model="Qwen/Qwen2-1.5B-Instruct",
                temperature=0,
                openai_api_key=os.getenv("OPENAI_API_KEY"),
                openai_api_base=os.getenv("OPENAI_BASE_URL")
            ),
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(),
            return_source_documents=True
        )
    
    async def get_answer(self, question: str):
        response = self.qa_chain({"query": question})
        return {
            "answer": response["result"],
            "sources": [doc.metadata for doc in response["source_documents"]]
        } 
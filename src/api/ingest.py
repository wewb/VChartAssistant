import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# 设置 OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-shznpcktusnwqdzzsbwzoimnjwjgismyrgsyskxsglgwuesv"
os.environ["OPENAI_BASE_URL"] = "https://api.siliconflow.cn/v1"

def load_docs():
    loader = DirectoryLoader(
        './docs',
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={'encoding': 'utf-8'},
        show_progress=True
    )
    
    try:
        documents = loader.load()
        print(f"Loaded {len(documents)} documents")
        
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        splits = text_splitter.split_documents(documents)
        
        print(f"Split into {len(splits)} chunks")
        
        # 初始化 embeddings，指定模型
        embeddings = OpenAIEmbeddings(
            model="netease-youdao/bce-embedding-base_v1",
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_api_base=os.getenv("OPENAI_BASE_URL")
        )
        
        # 创建向量存储
        vectorstore = Chroma(
            persist_directory="src/db",
            embedding_function=embeddings
        )
        
        # 添加文档到向量存储
        vectorstore.add_documents(splits)
        vectorstore.persist()
        
        print("Documents have been processed and stored")
        
        return vectorstore
        
    except Exception as e:
        print(f"Error processing documents: {str(e)}")
        raise

if __name__ == "__main__":
    load_docs() 
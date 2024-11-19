import os
from tqdm import tqdm
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from tenacity import retry, stop_after_attempt, wait_exponential

# 设置 OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-shznpcktusnwqdzzsbwzoimnjwjgismyrgsyskxsglgwuesv"
os.environ["OPENAI_BASE_URL"] = "https://api.siliconflow.cn/v1"

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def process_batch(batch, embeddings, persist_directory):
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    vectorstore.add_documents(batch)
    vectorstore.persist()
    return vectorstore

def load_docs():
    loader = DirectoryLoader(
        'data/docs',
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={'encoding': 'utf-8'},
        show_progress=True
    )
    
    try:
        documents = loader.load()
        print(f"Loaded {len(documents)} documents")
        
        # 使用递归分割器，根据模型最大token限制(512)调整
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,          # 考虑到中文字符，设置较小的块大小
            chunk_overlap=40,        # 10%的重叠
            length_function=len,
            separators=["\n\n", "\n", "。", "！", "？", ".", " ", ""]
        )
        splits = text_splitter.split_documents(documents)
        print(f"Split into {len(splits)} chunks")
        
        # 初始化 embeddings
        embeddings = OpenAIEmbeddings(
            model="netease-youdao/bce-embedding-base_v1",
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_api_base=os.getenv("OPENAI_BASE_URL"),
            max_retries=3,
            chunk_size=16  # 根据模型维度(768)和内存优化
        )
        
        # 创建向量存储
        vectorstore = Chroma(
            persist_directory="src/db",
            embedding_function=embeddings
        )
        
        # 使用tqdm显示总体进度
        batch_size = 16  # 根据模型性能优化的批处理大小
        total_batches = (len(splits) + batch_size - 1) // batch_size
        
        with tqdm(total=len(splits), desc="Processing documents") as pbar:
            for i in range(0, len(splits), batch_size):
                batch = splits[i:i + batch_size]
                try:
                    # 添加文档到向量存储
                    vectorstore.add_documents(batch)
                    # 更新进度条
                    pbar.update(len(batch))
                except Exception as e:
                    print(f"\nError in batch {i//batch_size + 1}/{total_batches}: {str(e)}")
                    continue
        print("\nDocuments have been processed and stored")
        return vectorstore
        
    except Exception as e:
        print(f"Error processing documents: {str(e)}")
        raise

if __name__ == "__main__":
    load_docs() 
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

# 设置 OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-shznpcktusnwqdzzsbwzoimnjwjgismyrgsyskxsglgwuesv"
os.environ["OPENAI_BASE_URL"] = "https://api.siliconflow.cn/v1"

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    text: str
    chat_history: list = []

# 初始化组件
embeddings = OpenAIEmbeddings(
    model="netease-youdao/bce-embedding-base_v1",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL")
)
vectorstore = Chroma(
    persist_directory="src/db",
    embedding_function=embeddings
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
llm = ChatOpenAI(
    model="Qwen/Qwen2-1.5B-Instruct",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL")
)

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是 VChart 框架的专家助手。使用以下上文来回答问题。如果你不知道答案，就说你不知道。\n\n上下文: {context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{question}"),
])

# 创建检索链
chain = (
    {
        "context": lambda x: retriever.get_relevant_documents(x["question"]),
        "chat_history": lambda x: x.get("chat_history", []),
        "question": lambda x: x.get("question", "")
    }
    | prompt
    | llm
    | StrOutputParser()
)

# Mount static files
app.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="src/frontend/templates")

@app.post("/api/ask")
async def ask_question(question: Question):
    try:
        chat_history = []
        for msg in question.chat_history:
            if msg["role"] == "user":
                chat_history.append(HumanMessage(content=msg["content"]))
            else:
                chat_history.append(AIMessage(content=msg["content"]))
        
        # 获取相关文档
        docs = retriever.get_relevant_documents(question.text)
        sources = [doc.page_content for doc in docs]
        
        # 调用链处理
        response = await chain.ainvoke({
            "question": question.text,
            "chat_history": chat_history
        })
        
        return {
            "answer": response,
            "sources": sources
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

@app.get("/api/status")
async def status():
    return {"message": "The server is running"}

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) 
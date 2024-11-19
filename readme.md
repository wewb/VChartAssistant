# VChart QA Bot

A question-answering chatbot for VChart documentation powered by LangChain and ChromaDB.

一个基于 LangChain 和 ChromaDB 的 VChart 文档问答聊天机器人。

### Background​
VisActor is a data visualization rendering engine that has won the love of many front-end developers in the open source community. You are a development contributor of the VChart framework in the VisActor project. Every day, many users ask you questions about the use of the warehouse. In order to reduce the burden of operating open source projects and better serve users, you hope to develop an intelligent question and answer robot with the help of LLM + LangChain. The robot can answer users' frequently asked questions based on the user documentation of the open source project.

https://github.com/VisActor/VChart/tree/develop

### Requirements description​
The VChart intelligent question and answer robot needs to provide a visual interactive interface for developers to use when they encounter problems. Typical user questions are as follows:​
1. Framework introduction class: Introduce the VChart chart and what parts it consists of.
2. Function usage category: How to download VChart? How to use VChart to configure a correlation scatter plot?​
3. Scenario consultation: I find that if the number has a long decimal point, it looks unsightly. Is there any way to control the length of the decimal place displayed on the label?​

The system needs to refer to the content in user documents, locate the most relevant information and generate corresponding answers through large models. If necessary, it can output multi-modal data such as code/pictures to better answer user questions.

## Features 功能特点

- 🤖 Intelligent QA based on VChart documentation
  
  基于 VChart 文档的智能问答

- 💬 Chat history support for contextual conversations
  
  支持上下文的对话历史记录

- 🔍 Source document references for answers
  
  回答带有文档来源引用

- ⚡ Fast vector similarity search with ChromaDB
  
  使用 ChromaDB 进行快速的向量相似度搜索

## Installation 安装

1. Clone the repository 克隆仓库

```bash
git clone https://github.com/yourusername/vchart-qa-bot.git
cd vchart-qa-bot
```

2. Create virtual environment 创建虚拟环境

```bash 
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install dependencies 安装依赖

```bash
pip install -r requirements.txt
```

4. Set environment variables 设置环境变量

Create a `.env` file with your API keys:
创建包含 API 密钥的 .env 文件：

```
OPENAI_API_KEY=your_openai_api_key
OPENAI_BASE_URL=your_openai_base_url 
```

## Usage 使用方法

1. Download VChart documentation 下载 VChart 文档

```bash
python src/utils/download_docs.py
```

2. Process documents and create vector store 处理文档并创建向量存储

```bash
python src/api/ingest.py
```

3. Start the server 启动服务器

```bash
python src/api/main.py
```

4. Open http://localhost:8000 in your browser
   
   在浏览器中打开 http://localhost:8000

## API Examples API 示例

### Ask a Question 提问

Request 请求:

```bash
curl -X POST http://localhost:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{
    "text": "How to create a line chart?",
    "chat_history": []
  }'
```

Response 响应:

```json
{
  "answer": "To create a line chart in VChart, you can follow these steps...",
  "sources": [
    "docs/tutorials/line-chart.md",
    "docs/examples/basic-line.md"
  ]
}
```

### Chat with History 带历史记录的对话

Request 请求:

```bash
curl -X POST http://localhost:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{
    "text": "What other chart types are available?",
    "chat_history": [
      {
        "role": "user",
        "content": "How to create a line chart?"
      },
      {
        "role": "assistant", 
        "content": "To create a line chart in VChart..."
      }
    ]
  }'
```

## Architecture 架构

The system consists of the following main components:
系统由以下主要组件构成：

- FastAPI backend for handling requests
  用于处理请求的 FastAPI 后端

- LangChain for orchestrating the QA chain
  用于编排问答链的 LangChain

- ChromaDB for vector storage and similarity search
  用于向量存储和相似度搜索的 ChromaDB

- OpenAI embeddings and chat completion
  OpenAI 的嵌入和聊天补全功能

## Contributing 贡献

Contributions are welcome! Please feel free to submit a Pull Request.
欢迎贡献！请随时提交 Pull Request。

## License 许可

This project is licensed under the MIT License.
本项目采用 MIT 许可证。

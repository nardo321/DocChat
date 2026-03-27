# DocChat
 
A RAG-based tool that lets you ask questions about any PDF document in plain language.
 
## How it works
 
DocChat uses Retrieval Augmented Generation (RAG) to answer questions based on the content of your documents. Rather than training a model on your data, it retrieves the most relevant sections of your PDF at query time and passes them to an LLM to generate an answer.
 
1. Load a PDF → split into chunks → convert to embeddings → store in vector database
2. User asks a question → question is embedded → similar chunks are retrieved
3. Retrieved chunks are injected into a prompt → LLM generates an answer
 
## Stack
 
- **Python** — core logic
- **LangChain** — RAG pipeline
- **ChromaDB** — local vector database
- **GitHub Models API** — LLM inference
 
## Status
 
In development. Basic RAG pipeline is the first milestone.

# 🧠 Rag-chatbot
*A production-ready Retrieval-Augmented Generation (RAG) chatbot MVP with LangChain, Qdrant, and pluggable LLMs.*

---

## 🔎 About

This repository is a **production-ready MVP** implementation of a Retrieval-Augmented Generation (RAG) system.  
It is designed as a **practice and learning project**, but follows real-world engineering principles so it can be extended for production use.

The goal of this project is to explore **AI, Machine Learning, and scalable system design** while building a modular and extensible RAG pipeline.  
It demonstrates how to ingest, process, and query unstructured data (PDF, JSON, XML, Text, and API data) with **LangChain**, store embeddings in **Qdrant**, and use different **LLMs (OpenAI, Google, Local models)** for retrieval-based question answering.

### Key Highlights
- ⚡ **Modular architecture** for ingestion, retrieval, and API serving.  
- 📂 Supports multiple data sources: PDF, JSON, XML, plain text, and APIs.  
- 🧠 **Multi-LLM support**: OpenAI, Google, and local models.  
- 📦 **Vector store integration** with Qdrant.  
- 🌍 Ready for **local development** but designed for deployment on **AWS / GCP**.  
- 🧪 Future-ready with **LangGraph** (advanced workflow control) and **LangSmith** (observability, tracing).  

This repository is open-source and meant to be a **learning-friendly but industry-relevant RAG boilerplate** for engineers, students, and researchers.

---

## 🚀 Features

This project is more than just a practice repo — it is structured like a **real-world RAG system**.  

### 🔹 Data Ingestion
- Handles **multiple data formats**: PDF, JSON, XML, plain text, and APIs.  
- Includes **cleaning & preprocessing pipelines** to ensure high-quality embeddings.  
- Modular design for easy addition of new data connectors.  

### 🔹 Retrieval
- Uses **Qdrant vector database** for scalable storage & fast semantic search.  
- Supports **hybrid search** (semantic + keyword-based) for more accurate results.  
- Embeddings generated using **state-of-the-art LLM models**.  

### 🔹 LLM Integration
- Plug-and-play support for multiple providers:  
  - **OpenAI** (high-quality proprietary models)  
  - **Google** (Gemini family)  
  - **Local models** (Ollama / HuggingFace) for cost-effective offline use  
- Easy to extend for additional LLMs.  

### 🔹 API & Serving
- Built with **FastAPI** for lightweight, production-ready serving.  
- REST endpoints for query handling, ingestion, and retrieval.  
- Dockerized for **local and cloud deployment** (AWS/GCP).  

### 🔹 Advanced RAG Capabilities
- **Context-aware querying** with LangChain pipelines.  
- Support for **multi-turn conversations** (maintains context).  
- Designed to integrate with **LangGraph** for advanced control flow.  
- Future-ready with **LangSmith** for tracing, observability, and evaluation.  

### 🔹 Engineering Best Practices
- ✅ Modular, clean architecture for maintainability.  
- ✅ `.dockerignore` and `.gitignore` to optimize builds.  
- ✅ Suitable for experimentation **and** production-scale adaptation.  

---

## 💡 Use Cases

This RAG system can power real-world applications such as:
- 🧑‍💻 **AI Assistants & Chatbots** – contextual Q&A over documents, manuals, or websites.  
- 🏢 **Enterprise Knowledge Search** – query across internal PDFs, reports, and knowledge bases.  
- 📊 **Data Insights** – extract and summarize information from large unstructured datasets.  
- 📚 **Education & Research** – assist students/researchers with quick access to knowledge.  

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Vector Database:** Qdrant  
- **Orchestration & Pipelines:** LangChain (future: LangGraph)  
- **LLMs:** OpenAI, Google Gemini, Ollama (local)  
- **Deployment:** Docker (local + cloud ready)  
- **Others:** Async I/O, modular architecture, clean code practices  


---

## 📦 Repository Structure
```text
rag-chatbot/
├─ apps/              # FastAPI service, routers, workers
├─ core/              # Core library: LLMs, embeddings, retrievers, chains, ingestion
├─ configs/           # Environment configs & provider selection
├─ data/              # Local documents (sources, staging, outputs)
├─ evals/             # Offline evaluation datasets & scripts
├─ infra/             # Cloud (Terraform, K8s, CI/CD)
├─ notebooks/         # Jupyter experiments
├─ scripts/           # CLI tools for ingestion & querying
└─ tests/             # Unit, integration, end-to-end tests
```

---

## ⚡ Quickstart (Local Dev)

### Prerequisites

- Python 3.11+
- Qdrant database (can run via Docker)
- Virtual environment (recommended)

1. **Clone the repository**
```bash
# Clone the repository
git clone https://github.com/AJakif/rag-chatbot.git
cd rag-chatbot

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

2. Configure Environment
```bash
# Copy and edit environment variables
cp configs/.env.example .env
# Edit .env with your actual API keys
```
⚠️ Never commit your `.env` file.
Only `.env.example` should be tracked.


3. Run Tests
```bash
make test
```

4. Start the API
```bash
make run
```

5. Test the API
```bash
curl http://localhost:8000/api/v1/health
curl http://localhost:8000/
```

6. View Logs
```bash
make logs
```
---

## 🔑 Environment Variables
See `configs/.env.example`[link](configs/.env.example)

Important ones:
* `APP_ENV` → Application environment (development/production)
* `QDRANT_HOST`, `QDRANT_PORT` → Qdrant vector database connection
* `OPENAI_API_KEY`, `GOOGLE_API_KEY` → Cloud LLM API keys
* `LOCAL_LLM_PROVIDER`, `LOCAL_LLM_MODEL` → Local LLM configuration

---

## 📊 Roadmap
* [x] Project scaffolding FastAPI
* [x] Configuration management with Pydantic Settings
* [x] Environment variable support
* [x] Structured logging with rotation
* [x] Health check endpoint
* [x] Test infrastructure
* [ ] Multi-provider LLM support (OpenAI, Google, Local/Ollama)
* [ ] Qdrant vector database integration
* [ ] Document ingestion pipeline (PDF, JSON, XML, Text, API)
* [ ] RAG chain implementation
* [ ] LangGraph integration
* [ ] LangSmith observability
* [ ] Cloud deployment (AWS ECS/GCP GKE)
* [ ] Evaluation scripts with sample datasets

---


## 🤝 Contributing

This is a practice repo — contributions are welcome if you’re experimenting with RAG, LLMs, or scaling strategies.
Feel free to fork, PR, or open issues with ideas, bugs, or learning notes.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-change`
3. Commit: `git commit -m "feat: add my change"`
4. Push: `git push origin feature/my-change`
5. Open a Pull Request

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🙌 Acknowledgements
* Mentor [Jasim Uddin dipu](https://www.linkedin.com/in/jasim-uddin-dipu-011663102/)

* [LangChain](https://www.langchain.com/)
* [Qdrant](https://qdrant.tech/)
* [LangSmith](https://smith.langchain.com/)
* [LangGraph](https://www.langchain.com/langgraph)
* [Ollama](https://ollama.ai/)

---

This README will be updated as the project progresses.
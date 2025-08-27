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

## 🗂 Project Structure
```text
apps/         → FastAPI service, routers, workers, (optional UI)  
core/         → Core library: LLMs, embeddings, retrievers, chains, ingestion  
configs/      → Environment configs & provider selection  
data/         → Local documents (sources, staging, outputs)  
evals/        → Offline evaluation datasets & scripts  
infra/        → Cloud (Terraform, K8s, CI/CD)  
notebooks/    → Jupyter experiments (LangGraph, retriever tests)  
scripts/      → CLI tools for ingestion & querying  
tests/        → Unit, integration, end-to-end tests  
```

---

## 📦 Repository Structure
```text
rag-chatbot/
├─ apps/
│ ├─ api/                                         # FastAPI service (HTTP endpoints, auth, rate limits)
│ │ ├─ main.py
│ │ ├─ routers/
│ │ │ ├─ health.py
│ │ │ ├─ query.py                                   # /query RAG endpoint (streaming)
│ │ │ ├─ ingest.py                                  # trigger/monitor ingestion jobs
│ │ ├─ schemas/
│ │ │ ├─ query_models.py
│ │ │ ├─ ingest_models.py
│ │ ├─ deps/
│ │ │ ├─ providers.py                               # DI: get_llm(), get_retriever(), get_qdrant()
│ │ ├─ middlewares/
│ │ └─ settings.py                                  # Pydantic Settings for API service
│ ├─ ingest_worker/                                 # Optional background worker (RQ/Celery/Arq)
│   ├─ worker.py
│   └─ settings.py
│
├─ core/                                          # Reusable library code (framework-agnostic)
│ ├─ config/
│ │ ├─ base.py                                    # Pydantic BaseSettings, env/yaml merge
│ │ ├─ providers.yaml                             # Provider selection & models per env
│ │ └─ settings.yaml                              # Chunking, embedding dims, retriever params
│ ├─ logging/
│ │ ├─ setup.py                                   # structlog/loguru JSON logs + uvicorn config
│ ├─ telemetry/
│ │ ├─ langsmith.py                               # LangSmith/LC tracing helpers (toggle via env)
│ ├─ llm/
│ │ ├─ base.py                                    # Unified LLM interface (sync/stream)
│ │ ├─ openai_provider.py
│ │ ├─ google_provider.py                         # Gemini via google-generativeai
│ │ ├─ local_ollama.py                            # Local models via Ollama API
│ │ └─ router.py                                  # Provider registry & failover logic
│ ├─ embeddings/
│ │ ├─ base.py
│ │ ├─ openai_embed.py
│ │ ├─ google_embed.py
│ │ ├─ hf_local_embed.py                          # e.g., intfloat/e5-base-v2 via sentence-transformers
│ │ └─ router.py
│ ├─ vectorstores/
│ │ ├─ qdrant_client.py                           # Qdrant client init + collections mgmt
│ │ └─ qdrant_store.py                            # LangChain VectorStore wrapper helpers
│ ├─ retrievers/
│ │ ├─ base.py
│ │ ├─ dense_retriever.py                         # Qdrant dense kNN
│ │ ├─ hybrid_retriever.py                        # (optional) BM25 + dense
│ │ └─ rerankers.py                               # (optional) Cross-encoder reranking
│ ├─ chains/
│ │ ├─ rag_chain.py                               # LC runnable for RAG (retrieve→compose→generate)
│ │ ├─ ingest_chain.py                            # file→load→chunk→embed→upsert
│ │ └─ graphs/                                    # LangGraph versions of the above (later)
│ ├─ ingestion/
│ │ ├─ loaders/
│ │ │ ├─ pdf_loader.py                            # PDF via pymupdf/pdfminer/unstructured
│ │ │ ├─ json_loader.py
│ │ │ ├─ xml_loader.py
│ │ │ ├─ text_loader.py
│ │ │ └─ api_loader.py                            # Pull from HTTP APIs with pagination
│ │ ├─ splitters.py                               # langchain text splitters + heuristics
│ │ ├─ cleaners.py                                # normalize whitespace, tables, metadata
│ │ ├─ dedupe.py                                  # hashing & source_id deduplication
│ │ ├─ schemas.py                                 # Document/Chunk schemas
│ │ └─ pipeline.py                                # Orchestrates loaders→clean→split→embed→upsert
│ ├─ utils/
│ │ ├─ id.py                                      # content hashing, ULIDs
│ │ ├─ timing.py
│ │ └─ io.py
│ └─ __init__.py
│
├─ configs/
│ ├─ .env.example
│ ├─ dev.yaml
│ ├─ prod.yaml
│ └─ providers/
│   ├─ dev.providers.yaml
│   └─ prod.providers.yaml
│
├─ data/
│ ├─ sources/                                     # put sample PDFs/JSON/XML/TXT here (gitignored)
│ ├─ staging/                                     # intermediate artifacts (gitignored)
│ └─ outputs/                                     # evals/exports (gitignored)
│
├─ evals/                                         # Offline evals & datasets
│ ├─ prompts/
│ ├─ datasets/
│ ├─ scripts/
│ └─ README.md
│
├─ notebooks/                                     # experiments (LangGraph nodes, retriever tests)
│ └─ 00_dev_scratch.ipynb
│
├─ scripts/
│ ├─ dev_up.sh                                    # start qdrant + api (docker-compose)
│ ├─ reset_qdrant.py                              # wipe/create collections
│ ├─ ingest_path.py                               # CLI: ingest local folder/file
│ ├─ ingest_api.py                                # CLI: ingest from URL/API
│ └─ query_cli.py                                 # quick CLI for RAG testing
│
├─ docker/
│ ├─ Dockerfile.api
│ ├─ Dockerfile.worker
│ ├─ docker-compose.dev.yml                       # api + qdrant (+ worker) for local dev
│ └─ qdrant.env                                   # optional auth/seeds for local
│
├─ infra/
│ ├─ terraform/
│ │ ├─ aws/
│ │ │ ├─ main.tf                                  # ECR/ECS or EKS + Qdrant (managed/self-host)
│ │ │ └─ variables.tf
│ │ └─ gcp/
│ │   ├─ main.tf                                  # GKE/Cloud Run + Qdrant on GKE or Qdrant Cloud
│ │   └─ variables.tf
│ ├─ k8s/
│ │ ├─ base/
│ │ │ ├─ api-deployment.yaml
│ │ │ ├─ api-service.yaml
│ │ │ └─ qdrant-statefulset.yaml
│ │ └─ overlays/
│ │ ├─ dev/
│ │ └─ prod/
│ └─ ci/
│   └─ github-actions.yml                         # lint, test, build, push, deploy
│
├─ tests/
│ ├─ unit/
│ ├─ integration/
│ └─ e2e/
│
├─ .gitignore
├─ .dockerignore
├─ pyproject.toml                                 # deps (langchain, qdrant-client, pydantic, etc.)
├─ README.md
├─ LICENSE
└─ Makefile                                       # common tasks (lint/test/run)
```

---

## ⚡ Quickstart (Local Dev)

1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/AJakif/rag-chatbot.git
cd rag-chatbot

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
# or if using Poetry:
poetry install

# Run the FastAPI app
uvicorn apps.main:app --reload
```

2. Configure Environment
Copy `.env.example` → `.env` and set values.
```bash
cp configs/.env.example .env
```
⚠️ Never commit your `.env` file.
Only `.env.example` should be tracked.


3. Run Qdrant + API
```bash
docker-compose -f docker/docker-compose.dev.yml up
```

4. Test Health
```bash
curl http://localhost:8000/health
```
---

## 🔑 Environment Variables
See `.env.example`[link](configs/.env.example)

Important ones:
* `QDRANT_URL` → vector DB location (local or cloud)
* `OPENAI_API_KEY`, `GOOGLE_API_KEY` → cloud LLMs
* `OLLAMA_HOST`, `OLLAMA_MODEL` → local LLMs
* `LANGSMITH_API_KEY` → for tracing/observability

---

## 🧩 Example Workflow
1. Ingest a PDF/JSON/XML/Text/API
```bash
python scripts/ingest_path.py data/sources/sample.pdf
```
2. Query with RAG
```bash
python scripts/query_cli.py "What are the main points in the PDF?"
```

3. Switch LLM provider via `configs/providers/dev.providers.yaml`

---

## 📊 Roadmap
* [ ] Project scaffolding (FastAPI + LangChain + Qdrant)
* [ ] Multi-provider LLM support (OpenAI, Google, Local/Ollama)
* [ ] Ingestion pipeline (PDF/JSON/XML/Text/API)
* [ ] LangGraph integration
* [ ] LangSmith observability
* [ ] Hybrid retrievers (BM25 + dense)
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
* Mentor **[Jasim Uddin dipu]** [link](https://www.linkedin.com/in/jasim-uddin-dipu-011663102/)

* LangChain [link](https://www.langchain.com/)
* Qdrant [link](https://qdrant.tech/)
* LangSmith [link](https://smith.langchain.com/)
* LangGraph [link](https://www.langchain.com/langgraph)
* Ollama [link](https://ollama.ai/)
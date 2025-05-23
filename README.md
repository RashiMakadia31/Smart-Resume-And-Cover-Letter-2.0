# Smart Resume & Cover Letter Generator Agent

An end-to-end AI assistant that analyzes your resume and job description to generate:
- Tailored resume bullet points
- Personalized cover letters
- Interview preparation Q&A

This project uses the **Mistral-7B-Instruct** model (`.gguf`) locally via `llama-cpp-python`, and leverages **LangChain**, **FAISS**, and **Streamlit**.

---

## Features

- Upload your Resume & Job Description
- Local LLM with Mistral (GGUF) using `llama-cpp-python`
- LangChain-powered RAG pipeline with FAISS vector store
- Resume bullet enhancement with job-specific tailoring
- Cover letter generation with customizable tone
- Interview Questions generator
- Frontend UI built using Streamlit

---

## Folder Structure

```

Job\_Help/
├── app.py                      # Streamlit app entry point
├── Backend/
│   ├── llm_agent.py           # Core logic with LangChain + Mistral
│   └── utils.py                # Helper functions  

├── Models/
│   └── mistral-7b-instruct-v0.1.Q4\_K\_M.gguf  # Mistral model file

├── requirements.txt
└── README.md

````

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/job-help-agent.git
cd job-help-agent
````

### 2. Install dependencies

Ensure Python 3.10+ is installed.

```bash
pip install -r requirements.txt
```

### 3. Download Mistral GGUF Model

Download `mistral-7b-instruct-v0.1.Q4_K_M.gguf` from:

* [https://huggingface.co/TheBloke/Mistral-7B-Instruct-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-GGUF)

Place it inside the `Models/` directory.

---

## Running the App

```bash
streamlit run app.py
```

---

## Tech Stack

| Layer        | Technology                                   |
| ------------ | -------------------------------------------- |
|    LLM       | Mistral-7B-Instruct via `llama-cpp-python`   |
|    RAG       | LangChain + FAISS                            |
|    Frontend  | Streamlit                                    |
|   Embedding  | SentenceTransformers / OpenAI (configurable) |

---


## TODO

* Add memory module for interactive chat
* Save session history
* Upload to HuggingFace Spaces / deploy to Streamlit Cloud

---

## Author

Rashi Makadia



from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from Backend.utils import clean_text
import os

MODEL_PATH = os.getenv("Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

llm = LlamaCpp(
    model_path='Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf',
    n_ctx=4096,
    temperature=0.7,
    max_tokens=1024,
    verbose=True
)

embeddings = HuggingFaceEmbeddings()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def generate_resume_and_cover(resume_text, jd_text):
    resume_chunks = text_splitter.split_text(clean_text(resume_text))
    jd_chunks = text_splitter.split_text(clean_text(jd_text))

    db = FAISS.from_texts(resume_chunks + jd_chunks, embeddings)
    retriever = db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    resume_output = qa_chain.run("Generate tailored resume bullet points based on this job description.")
    cover_letter = qa_chain.run("Write a personalized cover letter based on this resume and job description.")

    return resume_output, cover_letter

def generate_interview_qa(jd_text):
    jd_chunks = text_splitter.split_text(clean_text(jd_text))
    db = FAISS.from_texts(jd_chunks, embeddings)
    retriever = db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    questions = [
        "What are 3 possible interview questions for this job?",
        "Give ideal answers for the above questions."
    ]

    qa_list = []
    for q in questions:
        ans = qa_chain.run(q)
        qa_list.append((q, ans))

    return qa_list


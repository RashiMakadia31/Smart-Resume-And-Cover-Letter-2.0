import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import streamlit as st
from Backend.llm_agent import generate_resume_and_cover, generate_interview_qa
from Backend.file_parser import parse_resume, parse_job_description
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

st.set_page_config(page_title="Smart Resume Agent", layout="wide")
st.title("🧠 Smart Resume & Cover Letter Generator")

st.sidebar.header("Upload Files")
resume_file = st.sidebar.file_uploader("Upload your Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
jd_file = st.sidebar.file_uploader("Upload Job Description (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

if resume_file and jd_file:
    resume_text = parse_resume(resume_file)
    jd_text = parse_job_description(jd_file)

    if st.button("Generate Insights"):
        with st.spinner("Generating tailored resume and cover letter..."):
            resume_output, cover_letter = generate_resume_and_cover(resume_text, jd_text)
            qa_pairs = generate_interview_qa(jd_text)

        st.subheader("📌 Tailored Resume Suggestions")
        st.write(resume_output)

        st.subheader("✉️ Cover Letter")
        st.write(cover_letter)

        st.subheader("❓ Interview Prep Questions")
        for q, a in qa_pairs:
            st.markdown(f"**Q:** {q}")
            st.markdown(f"**A:** {a}\n")
       

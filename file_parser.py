import PyPDF2
import docx2txt

def parse_resume(uploaded_file):
    return extract_text(uploaded_file)

def parse_job_description(uploaded_file):
    return extract_text(uploaded_file)

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return file.read().decode("utf-8")

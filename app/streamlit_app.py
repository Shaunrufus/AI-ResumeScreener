import streamlit as st
import joblib
import re
import fitz  # PyMuPDF for PDF
import docx  # python-docx for DOCX
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from ResumeEvaluator import evaluate_resume, extract_keywords_from_jd


# Load model components
model = joblib.load("model/resume_classifier_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")
encoder = joblib.load("model/label_encoder.pkl")

# Text cleaning function
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|[^a-zA-Z\s]", " ", text)
    return re.sub(r"\s+", " ", text.lower()).strip()

# Text extractors
def extract_text_from_pdf(file):
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        return "".join(page.get_text() for page in doc)

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file):
    filetype = file.name.split('.')[-1].lower()
    if filetype == "pdf":
        return extract_text_from_pdf(file)
    elif filetype == "docx":
        return extract_text_from_docx(file)
    elif filetype == "txt":
        return str(file.read(), "utf-8", errors="ignore")
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="AI Resume Screener", layout="centered", page_icon="📄")

st.title("🤖 AI Resume Screener")
st.markdown("Upload your resume and get predicted job category instantly!")

uploaded_file = st.file_uploader("Upload Resume File", type=["pdf", "docx", "txt"], help="Supports PDF, DOCX, and TXT")

if uploaded_file:
    text = extract_text(uploaded_file)

    if not text:
        st.error("❌ Failed to extract text from file.")
    else:
        st.subheader("🧾 Resume Preview")
        st.text_area("Extracted Resume Text", text[:2000], height=250)

        # Clean, predict
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)
        label = encoder.inverse_transform(prediction)[0]

        st.success(f"✅ Predicted Job Category: **{label}**")

# TEMP: Placeholder job description until you upload real JD
        try:
            jd_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_jd", "data_analyst.txt")
            with open(jd_path, "r", encoding="utf-8") as f:
                sample_jd = f.read()
        except FileNotFoundError:
            sample_jd = ""
            st.warning("Sample job description file not found. Please add '../sample_jd/data_analyst.txt'.")

        if sample_jd:
            st.subheader("📋 Job Description (JD) for Reference")
            st.text(sample_jd[:1000] + "...") 
            st.caption(f"📂 Using JD from: `{jd_path}`")
 # limit long files

        keywords = extract_keywords_from_jd(sample_jd)


        # Run ATS/resume evaluation
        evaluation = evaluate_resume(text, job_keywords=keywords)

        # Show ATS/Rank/Structure Scores
        st.subheader("📊 Resume Evaluation Report")
        st.write(f"**ATS Score:** {evaluation['ats_score']}%")
        st.write(f"**Structure Score:** {evaluation['structure_score']}%")
        st.write(f"**Final Resume Rank:** {evaluation['final_rank']} / 100")

        # Show suggestions
        if evaluation["suggestions"]:
            st.subheader("🔧 Suggestions to Improve")
            for s in evaluation["suggestions"]:
                st.warning(s)

        # WordCloud
        st.subheader("🔍 Keyword Cloud")
        wc = WordCloud(width=600, height=300, background_color="white").generate(cleaned)
        st.image(wc.to_array())
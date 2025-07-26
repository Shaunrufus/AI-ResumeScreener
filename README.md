# AI-ResumeScreener

# 🤖 AI Resume Screener

An AI-powered web app built with Streamlit that screens resumes and predicts the most suitable job category using Natural Language Processing (NLP) and Machine Learning. It also evaluates resumes against a sample job description (JD) and provides ATS scores, structure analysis, suggestions, and keyword visualizations.

## 🔥 Live App

👉 [Click to Try the App](https://ai-resumescreener-5h7ifavnsxryjqlcipvd5h.streamlit.app/)  
*Upload your resume in PDF, DOCX, or TXT format and get instant AI analysis.*

---

## 📂 Project Structure

AI-Resume-Screener/
├── app/
│ └── streamlit_app.py # Main Streamlit app
├── model/
│ ├── resume_classifier_model.pkl # Trained ML model
│ ├── tfidf_vectorizer.pkl # Vectorizer for text data
│ └── label_encoder.pkl # Label encoder for categories
├── ResumeEvaluator/
│ └── init.py # Resume scoring and keyword matching logic
├── sample_jd/
│ └── data_analyst.txt # Sample job description for comparison
├── requirements.txt # All Python dependencies
└── README.md # Project documentation



---

## 🧠 Features

- ✅ **Job Prediction** – Predicts suitable job category from resume content.
- 📋 **JD Matching** – Compares resume with job description and extracts key terms.
- 📈 **ATS Evaluation** – Scores your resume based on ATS friendliness and structure.
- ☁️ **Word Cloud** – Visual representation of extracted keywords.
- 🧠 **ML/NLP Backend** – Built using scikit-learn, TF-IDF, PyMuPDF, and more.
- 🌐 **Web Interface** – Built with Streamlit and deployable via Streamlit Cloud.

---

## 🏗️ How It Works

1. **Resume Upload**: Upload your `.pdf`, `.docx`, or `.txt` resume.
2. **Text Extraction**: Extracts and cleans raw text from resume.
3. **Job Category Prediction**: ML model predicts your best-fit job category.
4. **JD Matching**: Loads a sample JD (e.g., Data Analyst) and compares keywords.
5. **Evaluation**: Returns ATS Score, Resume Structure Score, Final Ranking, Suggestions.
6. **WordCloud**: Shows important keywords detected from your resume.

---

## 🛠️ Setup Instructions (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Screener.git
cd AI-Resume-Screener


#Install Dependencies
pip install -r requirements.txt

#Run the App
streamlit run app/streamlit_app.py


sample_jd/
└── data_analyst.txt




Dependencies
streamlit

scikit-learn

joblib

matplotlib

wordcloud

python-docx

PyMuPDF (as fitz)

👨‍💻 Author
Shaun Rufus
ML Engineer | Python Developer | AI Enthusiast

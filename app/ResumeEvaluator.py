# app/resume_evaluator.py

import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer

def evaluate_resume(text, job_keywords=None):
    text = text.lower()
    ats_score = 0

    # 1. Count keyword matches
    if job_keywords:
        matches = sum(kw.lower() in text for kw in job_keywords)
        ats_score = int((matches / len(job_keywords)) * 100)

    # 2. Evaluate basic structure
    structure_score = 0
    if re.search(r"(experience|work history)", text): structure_score += 25
    if re.search(r"(education)", text): structure_score += 25
    if re.search(r"(skills?)", text): structure_score += 25
    if re.search(r"(email|phone|contact)", text): structure_score += 25

    # 3. Final rank score
    final_rank = int((ats_score * 0.5) + (structure_score * 0.5))

    # 4. Soft suggestion
    suggestions = []
    if "objective" not in text: suggestions.append("Consider adding a career objective.")
    if ats_score < 50: suggestions.append("Include more job-related keywords.")
    if structure_score < 100: suggestions.append("Improve resume formatting/sections.")

    return {
        "ats_score": ats_score,
        "structure_score": structure_score,
        "final_rank": final_rank,
        "suggestions": suggestions
    }

def extract_keywords_from_jd(jd_text):
    words = re.findall(r'\b[a-z]{4,}\b', jd_text.lower())
    return list(set(words))

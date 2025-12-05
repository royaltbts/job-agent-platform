
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import sys
import os
import streamlit as st

# -----------------------------
# FIX PYTHON IMPORT PATHS
# -----------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

# -----------------------------
# IMPORT YOUR AGENTS / UTILS
# -----------------------------
from agents.matcher import compute_similarity, explain_match
from agents.resume_optimizer import optimize_resume
from agents.cover_letter import generate_cover_letter
from agents.recruiter_message import create_recruiter_message
from utils.extractor import extract_text

# -----------------------------
# STREAMLIT PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Job Agent",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 AI Job Application Assistant")
st.write("Upload your resume, paste a job description, and generate everything automatically.")

# -----------------------------
# RESUME UPLOAD SECTION
# -----------------------------
st.header("📄 Upload Your Resume")

uploaded_file = st.file_uploader("Upload PDF or DOCX resume", type=["pdf", "docx"])

resume_text = ""
if uploaded_file:
    try:
        resume_text = extract_text(uploaded_file)
        st.success("Resume uploaded and extracted successfully!")
        st.text_area("Extracted Resume Text", resume_text, height=250)
    except Exception as e:
        st.error(f"Error extracting resume: {e}")

# -----------------------------
# JOB DESCRIPTION SECTION
# -----------------------------
st.header("📝 Enter Job Description")

job_description = st.text_area("Paste the job description here:", height=200)

# -----------------------------
# ACTION BUTTON
# -----------------------------
if st.button("⚡ Generate Results"):
    if not uploaded_file:
        st.error("Please upload your resume.")
    elif not job_description.strip():
        st.error("Please paste a job description.")
    else:
        # -----------------------------------
        # AI PROCESSING
        # -----------------------------------
        st.subheader("🔍 Match Score")
        score = compute_similarity(resume_text, job_description)
        st.metric("Similarity Score", f"{score}%")

        st.subheader("🤖 AI Match Explanation")
        explanation = explain_match(resume_text, job_description)
        st.write(explanation)

        st.subheader("📌 Optimized Resume")
        optimized_resume = optimize_resume(job_description)
        st.text_area("Optimized Resume", optimized_resume, height=300)

        st.subheader("✉️ Cover Letter")
        cover_letter = generate_cover_letter(optimized_resume, job_description)
        st.text_area("Generated Cover Letter", cover_letter, height=300)

        st.subheader("💬 Recruiter Message")
        message = create_recruiter_message(optimized_resume, job_description, "Company")
        st.text_area("Recruiter Message", message, height=200)

        st.success("Done! Your AI application pack is ready 🚀")

# -----------------------------
# FOOTER
# -----------------------------
st.write("---")
st.caption("Built with ❤️ by Arun’s AI Job Agent")


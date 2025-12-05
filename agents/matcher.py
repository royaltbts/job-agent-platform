
# agents/matcher.py

from core.llm import ask_llm
from sentence_transformers import SentenceTransformer, util
from agents.resume_optimizer import optimize_resume
from agents.cover_letter import generate_cover_letter
from agents.recruiter_message import create_recruiter_message

# Load embedding model once (fast)
model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_similarity(resume_text, job_text):
    """Return cosine similarity score (0–100)."""
    emb1 = model.encode(resume_text)
    emb2 = model.encode(job_text)
    score = util.cos_sim(emb1, emb2).item()
    return round(score * 100, 2)


def explain_match(resume_text, job_text):
    """Ask the LLM to explain the match."""
    prompt = f"""
Compare the following resume and job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_text}

Provide:
1. Key matching skills
2. Missing skills
3. Why this candidate fits / does not fit
4. A final suitability score (0–100)

Keep it short.
"""
    return ask_llm(prompt)


# MAIN PIPELINE
if __name__ == "__main__":

    # Real tests must be replaced with your resume & scraped JD
    resume = "Analytics manager with incentives, pharma SFE, dashboards, SQL, IC modeling."
    jd = "We need an incentive compensation analyst with pharma experience, SFE, KPI reporting, Power BI and SQL."

    # 1️⃣ Match Score
    score = compute_similarity(resume, jd)
    print("Match Score:", score)

    # 2️⃣ Optimized Resume
    optimized_resume = optimize_resume(jd)
    print("\nOptimized Resume:\n")
    print(optimized_resume)

    # 3️⃣ Cover Letter
    cover_letter = generate_cover_letter(optimized_resume, jd)
    print("\nCover Letter:\n")
    print(cover_letter)

    # 4️⃣ Recruiter Message
    msg = create_recruiter_message(optimized_resume, jd, "Company Name")
    print("\nRecruiter Message:\n")
    print(msg)

    # 5️⃣ Explanation
    explanation = explain_match(resume, jd)
    print("\nLLM Explanation:\n", explanation)

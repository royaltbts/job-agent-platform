import os
from core.llm import ask_llm

MASTER_RESUME_PATH = os.path.join(os.path.dirname(__file__), "..", "core", "master_resume.txt")

with open(MASTER_RESUME_PATH, "r") as f:
    BASE_RESUME = f.read()


def optimize_resume(job_description):
    prompt = f"""
You are an **ATS resume optimization engine**.

Your task:
- Rewrite the candidate’s resume so it **perfectly matches the job description**
- ONLY use real experience from the master resume — no fabrications
- Rewrite tone, bullet points, structure, and role focus
- Remove irrelevant domain experience
- Add keywords from job description naturally
- Produce a **clean, modern ATS resume**
- Output ONLY the resume — no explanations

MASTER RESUME:
{BASE_RESUME}

TARGET JOB DESCRIPTION:
{job_description}

Now generate the **optimized ATS resume**:
"""
    return ask_llm(prompt)


if __name__ == "__main__":
    # Example only — replace with any job description you test
    sample_jd = "We are hiring an Incentive Compensation Analyst with experience in SFE, KPI reporting, SQL, Power BI, Pharma analytics, and cross-functional coordination."
    print(optimize_resume(sample_jd))

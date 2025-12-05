from core.llm import ask_llm

def generate_cover_letter(resume, job_description, company="the company"):
    prompt = f"""
You are an expert cover letter generator.

Using the candidate's resume and the job description:
- Write a concise, high-impact cover letter.
- Make it role-specific.
- Highlight Arun's strengths in analytics, incentives, SFE, pharma ops, and digital operations.
- Keep it honest: do NOT add skills he doesn't have.
- Tone: professional, confident, not generic.

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}

Cover Letter:
"""
    return ask_llm(prompt)


if __name__ == "__main__":
    sample_resume = "Arun's resume sample text..."
    sample_jd = "Job description sample text..."
    print(generate_cover_letter(sample_resume, sample_jd, company="ABC Corp"))


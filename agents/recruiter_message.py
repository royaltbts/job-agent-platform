from core.llm import ask_llm

def create_recruiter_message(resume, job_description, company):
    prompt = f"""
Write a short LinkedIn message to a recruiter at {company}.
Tone: polite, confident, concise.

Resume:
{resume}

Job Description:
{job_description}

Message:
"""
    return ask_llm(prompt)


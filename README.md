⭐ Job Agent Platform — Multi-Agent Job Search Automation
AI-powered resume optimization, job matching, auto-apply bots, and recruiter messaging — all in one platform.

🚀 Overview

The Job Agent Platform is a fully automated AI system designed to help job seekers:

Optimize resumes for each job

Generate tailored cover letters & recruiter messages

Calculate job–resume similarity with embeddings

Auto-apply to jobs across portals

Run multi-API LLM pipelines (Groq, OpenAI, DeepSeek, Qwen)

Use a web-based UI (Streamlit) to control everything

This platform uses modular AI agents, allowing easy expansion into:

Customer Success

Analytics

Tech roles

Healthcare

Finance

Many more domains

🧠 Key Features
✅ 1. Resume Optimization Agent

Reads your master resume

Reads job description

Uses LLM to produce ATS-optimized resume

Adds missing keywords ethically

Maintains truthfulness

✅ 2. Job Matching Agent

Computes similarity using SentenceTransformer

Gives match score (0–100)

Generates a detailed explanation:

Matching skills

Missing skills

Final suitability score

✅ 3. Cover Letter Agent

AI-generated, short, personalized cover letters for each job.

✅ 4. Recruiter Outreach Agent

Creates highly professional LinkedIn messages tailored to:

Role

Company

Recruiter

✅ 5. Automated Job Apply Bot

Supports:

LinkedIn Easy Apply

Naukri (coming soon)

Indeed (coming soon)

Glassdoor (coming soon)

🌐 6. Web UI (Streamlit)

Users can:

Upload resume

Paste job descriptions

View optimized resume

Generate cover letters

Get recruiter messages

Export everything

🧩 Architecture
job_agent_platform/
│
├── agents/
│   ├── matcher.py               # Similarity & explanation agent
│   ├── resume_optimizer.py      # Resume optimization agent
│   ├── cover_letter.py          # Cover letter generator
│   ├── recruiter_message.py     # Recruiter message generator
│   ├── linkedin_apply.py        # Job auto-apply bot
│   └── job_scraper.py           # (future) Job portal scraper
│
├── core/
│   ├── llm.py                   # Multi-API LLM engine (Groq, OpenAI, HF, DeepSeek)
│   ├── keychain.py              # Secure credential loader (macOS Keychain)
│   └── master_resume.txt        # Base resume
│
├── utils/
│   └── extractor.py             # Text extractor for PDF/DOCX resumes
│
├── ui/
│   ├── app.py                   # Streamlit premium UI
│   └── test_app.py
│
├── .env                         # Secrets (ignored)
├── .gitignore
└── README.md

🔐 Security
✔️ .env never gets committed

Your .gitignore is properly configured.

✔️ macOS Keychain used for high-security API management

Your GROQ API key stays encrypted on device.

✔️ GitHub Push Protection verified

No secrets exist in commit history.

⚙️ Tech Stack
Layer	Technology
LLM Engines	Groq, OpenAI, DeepSeek, Qwen, HF models
Backend	Python
Agents	Modular AI agents
Embeddings	SentenceTransformers (MiniLM-L6-v2)
UI	Streamlit
Automation	Selenium (LinkedIn Easy Apply)
Security	macOS Keychain + .env + GitHub push protection
📦 Installation
1️⃣ Clone repository
git clone https://github.com/royaltbts/job-agent-platform.git
cd job-agent-platform

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set up Keychain API key
python3

from core.keychain import save_key
save_key("GROQ_API_KEY", "gsk_your_key_here")

4️⃣ Launch Streamlit UI
streamlit run ui/app.py

🖥️ UI Screenshots (placeholders)
⭐ Resume Optimization

⭐ Job Match Scoring

⭐ Cover Letter Generator

⭐ Recruiter Message Generator

🛠️ Usage Workflow
Step 1: Upload your resume
Step 2: Paste job description
Step 3: Platform generates:

Optimized resume

Cover letter

Recruiter message

Match score & explanation

Step 4: Auto-apply on LinkedIn

Chrome window opens → system handles application.

⏳ Roadmap (2025)
Feature	Status
Multi-API support	✅ Done
Streamlit UI	✅ Done
LinkedIn auto-apply	⚠️ Beta
Naukri auto-apply	🔄 In progress
Indeed auto-apply	🔄 Planned
Voice-based job search	⚙️ Planned
Mobile app (React Native)	🎯 Q2 2025
Cloud deployment	🔜 Coming soon
👤 Author

Arun Kumar Siripurapu
Analytics Leader • Incentive Strategy • Customer Success
🔗 LinkedIn: https://www.linkedin.com/in/arunkumarsiripurapu/

📧 Email: arunkumarsiripurapu@gmail.com

⭐ Contributions Welcome

If you want to contribute:

git checkout -b feature/my-enhancement
git commit -m "Added new feature"
git push


Then open a Pull Request 🚀

❤️ Support

If this project helped you land interviews or jobs, consider ⭐ starring the repo!

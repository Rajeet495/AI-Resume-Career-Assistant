\# 📄 AI Resume \& Career Assistant



An AI-powered resume analysis and career guidance application that uses \*\*Generative AI, RAG, embeddings, AI agents, tool execution, and LLMs\*\* to analyze a resume against a target job description.



The application provides an ATS-style compatibility estimate, identifies matching and missing skills, generates a skill-gap learning plan, suggests resume improvements, and provides interview preparation guidance.



\---



\## 🚀 Live Demo



\*\*Live Website:\*\*

\*Add your Streamlit deployment URL here\*



\---



\## 💻 GitHub Repository



\*\*Repository:\*\*

\*Add your GitHub repository URL here\*



\---



\# 🎯 Project Objective



The goal of this project is to build a practical Generative AI application that combines the concepts learned throughout the internship:



\* Generative AI fundamentals

\* Prompt Engineering

\* LLM APIs

\* Embeddings

\* Retrieval-Augmented Generation (RAG)

\* Vector similarity search

\* AI Agents

\* Tool execution

\* Structured AI workflows

\* Streamlit deployment



\---



\# ✨ Features



\## 📄 Resume Upload



Users can upload their resume in PDF format.



The application extracts the text automatically using `pypdf`.



\---



\## 🔎 RAG-Based Resume Retrieval



The extracted resume is:



```text

PDF

&#x20;↓

Text Extraction

&#x20;↓

Text Chunking

&#x20;↓

Embeddings

&#x20;↓

Vector Similarity

&#x20;↓

Relevant Resume Sections

```



The application retrieves the most relevant sections of the resume based on the provided job description.



\---



\## 🤖 AI Career Agent



The application uses an AI agent workflow to analyze the candidate's resume.



The agent performs:



```text

Understand Task

&#x20;     ↓

Analyze Resume

&#x20;     ↓

Identify Skills

&#x20;     ↓

Execute Tools

&#x20;     ↓

Process Results

&#x20;     ↓

Generate Career Report

```



\---



\# 🛠️ AI Tools



The project contains three custom tools.



\### 1. ATS Score Tool



Calculates an ATS-style compatibility score using matching and missing skills.



> Note: This is a custom compatibility estimate and is not an official ATS score.



\### 2. Skill Gap Analysis Tool



Identifies:



\* Matching skills

\* Missing skills

\* Matching skill count

\* Missing skill count



\### 3. Resume Summary Tool



Generates basic resume statistics including:



\* Word count

\* Character count

\* Projects availability

\* Skills section availability

\* Education availability

\* Experience/internship availability



\---



\# 🧠 Generative AI



The project uses the Groq API with:



```text

openai/gpt-oss-20b

```



The LLM is used for:



\* Resume analysis

\* Skill comparison

\* Career recommendations

\* Resume improvement

\* Interview preparation

\* Learning plans



\---



\# 📚 Career Analysis



The final report contains:



\### 📊 ATS-Style Compatibility



A custom compatibility estimate based on matching and missing skills.



\### ✅ Matching Skills



Skills present in the resume that are relevant to the job.



\### ❌ Missing Skills



Important job requirements that are not clearly present in the resume.



\### 📚 Skill Gap Learning Plan



Provides:



\* Skill importance

\* What to learn

\* Why the skill matters

\* Suggested practice/projects



\### 📝 Resume Improvement Suggestions



Suggestions for improving:



\* Skills

\* Projects

\* Experience

\* Keywords

\* Achievements

\* Resume clarity



\### 🎯 Interview Preparation



Technical and HR topics relevant to the target position.



\### 🚀 Project Recommendations



Project ideas designed to help demonstrate missing skills.



\### 📅 30-Day Improvement Plan



A structured learning roadmap for improving job readiness.



\---



\# 🏗️ Architecture



```text

&#x20;                   USER

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │ Streamlit UI    │

&#x20;            └────────┬────────┘

&#x20;                     │

&#x20;            Resume PDF + JD

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │ PDF Extraction  │

&#x20;            │    pypdf        │

&#x20;            └────────┬────────┘

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │ Text Chunking   │

&#x20;            └────────┬────────┘

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │  Embeddings     │

&#x20;            │ MiniLM-L6-v2    │

&#x20;            └────────┬────────┘

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │ Vector Search   │

&#x20;            │    NumPy        │

&#x20;            └────────┬────────┘

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │   AI Agent      │

&#x20;            └────────┬────────┘

&#x20;                     │

&#x20;            ┌────────┼────────┐

&#x20;            │        │        │

&#x20;            ▼        ▼        ▼

&#x20;         ATS Tool  Skill Gap  Summary

&#x20;            │        │        │

&#x20;            └────────┼────────┘

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │   Groq LLM      │

&#x20;            │ gpt-oss-20b     │

&#x20;            └────────┬────────┘

&#x20;                     │

&#x20;                     ▼

&#x20;            ┌─────────────────┐

&#x20;            │ Career Report   │

&#x20;            └─────────────────┘

```



\---



\# 🧰 Technology Stack



| Technology            | Purpose                   |

| --------------------- | ------------------------- |

| Python                | Core programming language |

| Streamlit             | Web application           |

| Groq                  | LLM API                   |

| GPT-OSS-20B           | Generative AI model       |

| PyPDF                 | PDF text extraction       |

| Sentence Transformers | Text embeddings           |

| all-MiniLM-L6-v2      | Embedding model           |

| NumPy                 | Vector similarity         |

| JSON                  | Structured data           |

| Git                   | Version control           |

| GitHub                | Code repository           |



\---



\# 📁 Project Structure



```text

AI-Resume-Career-Assistant/

│

├── app.py

├── agent.py

├── rag.py

├── tools.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── utils/

│   └── pdf\_processor.py

│

└── .streamlit/

&#x20;   └── secrets.toml

```



> `.streamlit/secrets.toml` is excluded from GitHub using `.gitignore`.



\---



\# ⚙️ Installation



\## 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\## 2. Enter the project directory



```bash

cd AI-Resume-Career-Assistant

```



\## 3. Create a virtual environment



```bash

python -m venv .venv

```



\## 4. Install dependencies



```bash

pip install -r requirements.txt

```



\---



\# 🔑 API Configuration



Create:



```text

.streamlit/secrets.toml

```



Add:



```toml

GROQ\_API\_KEY = "YOUR\_GROQ\_API\_KEY"

```



Never upload this file to GitHub.



\---



\# ▶️ Run the Application



```bash

python -m streamlit run app.py

```



The application will open in your browser.



\---



\# 🧪 Example Workflow



\### Step 1



Upload a resume PDF.



\### Step 2



Paste a target job description.



\### Step 3



Click:



```text

🚀 Analyze Resume

```



\### Step 4



The application:



```text

Extracts Resume

&#x20;     ↓

Creates Chunks

&#x20;     ↓

Creates Embeddings

&#x20;     ↓

Retrieves Relevant Information

&#x20;     ↓

Runs AI Agent

&#x20;     ↓

Executes Tools

&#x20;     ↓

Generates Career Analysis

```



\---



\# 🔐 Security



API keys are stored using Streamlit secrets.



The following files are excluded from Git:



```text

.streamlit/

.env

\_\_pycache\_\_/

\*.pyc

```



No API key should be committed to the repository.



\---



\# ⚠️ Limitations



This project is an educational AI application.



The ATS-style score is a custom compatibility estimate and does not represent the score generated by a commercial Applicant Tracking System.



AI-generated recommendations may contain errors, so users should verify important career information independently.



The quality of analysis depends on the quality of the uploaded resume and job description.



\---



\# 🔮 Future Improvements



Possible future enhancements include:



\* Multiple resume comparison

\* Multiple job comparison

\* Resume rewriting

\* Cover letter generation

\* LinkedIn profile analysis

\* Job recommendation system

\* Persistent user profiles

\* Better skill taxonomy

\* Industry-specific scoring

\* Resume section-level scoring

\* PDF report generation

\* Authentication

\* Database integration



\---



\# 🎓 Internship Concepts Demonstrated



This capstone combines the major concepts covered throughout the internship:



```text

Module 1

Generative AI Foundations

&#x20;       ↓

Module 2

Prompt Engineering

&#x20;       ↓

Module 3

LLM APIs \& Applications

&#x20;       ↓

Module 4

RAG \& Embeddings

&#x20;       ↓

Module 5

AI Agents \& Tools

&#x20;       ↓

Module 6

GENAI CAPSTONE

```



\---



\# 👨‍💻 Author



\*\*Rajeet Pratap Mall\*\*



B.Tech CSE – Artificial Intelligence \& Machine Learning



GitHub: `Rajeet495`



\---



\# ⭐ Acknowledgement



This project was developed as part of a Generative AI internship/capstone project to demonstrate practical implementation of modern GenAI application development concepts.



````



Save it.



\### Next command



Check your Git status:



```powershell

git status

````



\*\*Don't push yet.\*\* Send me the output of `git status`, and we'll clean the repository before the final push.




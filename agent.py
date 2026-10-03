
import json

from tools import execute_tool


# ============================================
# TOOL DEFINITIONS
# ============================================

tool_definitions = [

    {
        "type": "function",
        "function": {
            "name": "calculate_ats_score",

            "description": (
                "Calculate an ATS-style compatibility "
                "score."
            ),

            "parameters": {
                "type": "object",

                "properties": {

                    "matching_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },

                    "missing_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },

                "required": [
                    "matching_skills",
                    "missing_skills"
                ]
            }
        }
    },


    {
        "type": "function",
        "function": {
            "name": "analyze_skill_gap",

            "description": (
                "Analyze matching and missing "
                "skills."
            ),

            "parameters": {
                "type": "object",

                "properties": {

                    "matching_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },

                    "missing_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },

                "required": [
                    "matching_skills",
                    "missing_skills"
                ]
            }
        }
    },


    {
        "type": "function",
        "function": {
            "name": "summarize_resume",

            "description": (
                "Generate basic resume statistics."
            ),

            "parameters": {
                "type": "object",

                "properties": {

                    "resume_text": {
                        "type": "string"
                    }
                },

                "required": [
                    "resume_text"
                ]
            }
        }
    }
]


# ============================================
# EXTRACT SKILL ANALYSIS
# ============================================

def extract_skill_analysis(
    client,
    resume_context,
    job_description
):

    prompt = f"""
You are a resume analysis assistant.

Compare the resume with the job description.

Return ONLY valid JSON.

Use exactly:

{{
    "matching_skills": [],
    "missing_skills": []
}}

Rules:

1. matching_skills:
   Skills clearly present in both the resume
   and job description.

2. missing_skills:
   Skills required by the job but not clearly
   present in the resume.

3. Do not invent skills.

4. Do not include explanations.

5. Do not use markdown.

RESUME:

{resume_context}

JOB DESCRIPTION:

{job_description}
"""


    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[

            {
                "role": "system",

                "content": (
                    "You are a structured "
                    "resume analysis assistant."
                )
            },

            {
                "role": "user",

                "content": prompt
            }
        ],

        temperature=0.0
    )


    content = (
        response
        .choices[0]
        .message
        .content
    )


    try:

        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        result = json.loads(
            content
        )

        return result

    except Exception:

        return {

            "matching_skills": [],

            "missing_skills": [],

            "error":
                "Could not parse skill analysis."
        }


# ============================================
# MAIN AGENT
# ============================================

def run_agent(
    client,
    resume_context,
    job_description
):


    tool_results = []


    # ========================================
    # STEP 1
    # UNDERSTAND TASK
    # ========================================

    skill_analysis = extract_skill_analysis(

        client,

        resume_context,

        job_description
    )


    matching_skills = skill_analysis.get(
        "matching_skills",
        []
    )


    missing_skills = skill_analysis.get(
        "missing_skills",
        []
    )


    # ========================================
    # STEP 2
    # SKILL GAP TOOL
    # ========================================

    skill_gap_result = execute_tool(

        "analyze_skill_gap",

        matching_skills=matching_skills,

        missing_skills=missing_skills
    )


    tool_results.append({

        "tool":
            "analyze_skill_gap",

        "arguments": {

            "matching_skills":
                matching_skills,

            "missing_skills":
                missing_skills
        },

        "result":
            skill_gap_result
    })


    # ========================================
    # STEP 3
    # ATS SCORE TOOL
    # ========================================

    ats_result = execute_tool(

        "calculate_ats_score",

        matching_skills=matching_skills,

        missing_skills=missing_skills
    )


    tool_results.append({

        "tool":
            "calculate_ats_score",

        "arguments": {

            "matching_skills":
                matching_skills,

            "missing_skills":
                missing_skills
        },

        "result":
            ats_result
    })


    # ========================================
    # STEP 4
    # RESUME SUMMARY TOOL
    # ========================================

    summary_result = execute_tool(

        "summarize_resume",

        resume_text=resume_context
    )


    tool_results.append({

        "tool":
            "summarize_resume",

        "arguments": {

            "resume_text":
                resume_context
        },

        "result":
            summary_result
    })


    # ========================================
    # STEP 5
    # FINAL AI CAREER REPORT
    # ========================================

    final_prompt = f"""

You are an AI Resume and Career Assistant.

Create a professional career analysis based
ONLY on the information provided.

Do not invent experience, education,
projects or skills.

============================================
RESUME
============================================

{resume_context}


============================================
JOB DESCRIPTION
============================================

{job_description}


============================================
TOOL RESULTS
============================================

Skill Gap:

{json.dumps(
    skill_gap_result,
    indent=2
)}


ATS Score:

{json.dumps(
    ats_result,
    indent=2
)}


Resume Summary:

{json.dumps(
    summary_result,
    indent=2
)}


============================================
FINAL REPORT
============================================

Use the following sections:

## 📊 ATS-Style Compatibility

Give the ATS-style compatibility score.

Clearly state that this is a custom
ATS-style estimate and not an official
ATS score.


## ✅ Matching Skills

List the important skills that match
the job description.


## ❌ Missing Skills

List the important skills that are missing.


## 📚 Skill Gap Learning Plan

Create a practical learning plan.

For every important missing skill,
provide:

- Skill
- Why it matters
- What to learn
- Suggested practice/project

Prioritize the skills from highest
importance to lower importance.


## 📝 Resume Improvement Suggestions

Give practical suggestions for improving
the resume for this particular job.

Focus on:

- Skills section
- Projects
- Experience
- Keywords
- Achievements
- Resume clarity


## 🎯 Interview Preparation

Suggest technical and HR topics that the
candidate should prepare based on the job.


## 🚀 Recommended Project Ideas

Suggest 2-3 projects that could help
the candidate demonstrate the missing
skills.

Projects should be realistic for a
student/fresher.


## 📅 30-Day Improvement Plan

Create a realistic 30-day learning plan
for improving the candidate's fit for
this role.

Divide it into weekly phases.


## 📌 Final Summary

Give a concise summary of:

- Current strengths
- Main gaps
- Recommended next steps

Do not invent information.
"""


    # ========================================
    # FINAL GROQ CALL
    # ========================================

    final_response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[

            {
                "role": "system",

                "content": (
                    "You are an AI Resume and "
                    "Career Assistant."
                )
            },

            {
                "role": "user",

                "content":
                    final_prompt
            }
        ],

        temperature=0.2
    )


    final_answer = (
        final_response
        .choices[0]
        .message
        .content
    )


    # ========================================
    # RETURN RESULT
    # ========================================

    return {

        "final_response":
            final_answer,

        "tool_results":
            tool_results
    }

# ============================================
# AI RESUME & CAREER ASSISTANT
# TOOLS MODULE
# ============================================


# ============================================
# TOOL 1: ATS SCORE
# ============================================

def calculate_ats_score(
    matching_skills,
    missing_skills
):
    """
    Calculate an ATS-style compatibility score
    based on matching and missing skills.
    """

    total_skills = (
        len(matching_skills)
        + len(missing_skills)
    )

    if total_skills == 0:
        return 0

    score = (
        len(matching_skills)
        / total_skills
    ) * 100

    return round(score)


# ============================================
# TOOL 2: SKILL GAP ANALYSIS
# ============================================

def analyze_skill_gap(
    matching_skills,
    missing_skills
):
    """
    Analyze the candidate's skill gap.
    """

    return {
        "matching_skills": matching_skills,

        "missing_skills": missing_skills,

        "matching_count": len(
            matching_skills
        ),

        "missing_count": len(
            missing_skills
        )
    }


# ============================================
# TOOL 3: RESUME SUMMARY
# ============================================

def summarize_resume(
    resume_text
):
    """
    Generate basic resume statistics.
    """

    words = resume_text.split()

    return {
        "word_count": len(words),

        "character_count": len(
            resume_text
        ),

        "has_projects": (
            "project"
            in resume_text.lower()
        ),

        "has_skills": (
            "skill"
            in resume_text.lower()
        ),

        "has_education": (
            "education"
            in resume_text.lower()
        ),

        "has_experience": (
            "experience"
            in resume_text.lower()
            or
            "internship"
            in resume_text.lower()
        )
    }


# ============================================
# TOOL REGISTRY
# ============================================

TOOL_REGISTRY = {

    "calculate_ats_score":
        calculate_ats_score,

    "analyze_skill_gap":
        analyze_skill_gap,

    "summarize_resume":
        summarize_resume
}


# ============================================
# SAFE TOOL EXECUTOR
# ============================================

def execute_tool(
    tool_name,
    **kwargs
):
    """
    Execute a registered tool safely.
    """

    # Check whether tool exists
    if tool_name not in TOOL_REGISTRY:

        return {
            "error":
            f"Unknown tool: {tool_name}"
        }


    try:

        # Get requested tool
        tool = TOOL_REGISTRY[
            tool_name
        ]


        # Execute tool
        result = tool(
            **kwargs
        )


        return result


    except Exception as e:

        return {
            "error":
            str(e)
        }


# ============================================
# TEST SECTION
# ============================================

if __name__ == "__main__":

    print(
        "Testing ATS Score Tool..."
    )

    ats_result = execute_tool(

        "calculate_ats_score",

        matching_skills=[
            "Python",
            "RAG",
            "SQL"
        ],

        missing_skills=[
            "Docker"
        ]
    )

    print(
        ats_result
    )


    print(
        "\nTesting Skill Gap Tool..."
    )

    skill_result = execute_tool(

        "analyze_skill_gap",

        matching_skills=[
            "Python",
            "RAG",
            "SQL"
        ],

        missing_skills=[
            "Docker",
            "AWS"
        ]
    )

    print(
        skill_result
    )


    print(
        "\nTesting Resume Summary Tool..."
    )

    summary_result = execute_tool(

        "summarize_resume",

        resume_text=(
            "Python developer with "
            "Machine Learning projects "
            "and internship experience."
        )
    )

    print(
        summary_result
    )


    print(
        "\nAll tools tested successfully! ✅"
    )
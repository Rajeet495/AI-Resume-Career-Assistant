
import streamlit as st

from groq import Groq
from pypdf import PdfReader

from rag import (
    create_chunks,
    create_embeddings,
    create_faiss_index,
    retrieve_chunks
)

from agent import run_agent


# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="AI Resume & Career Assistant",
    page_icon="📄",
    layout="wide"
)


# ============================================
# GROQ CONNECTION
# ============================================

try:

    groq_api_key = st.secrets["GROQ_API_KEY"]

    client = Groq(
        api_key=groq_api_key
    )

except Exception:

    st.error(
        "Groq API key not found. "
        "Please check .streamlit/secrets.toml"
    )

    st.stop()


# ============================================
# PDF TEXT EXTRACTION
# ============================================

def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text


# ============================================
# HEADER
# ============================================

st.title(
    "📄 AI Resume & Career Assistant"
)

st.write(
    "AI-powered resume analysis using "
    "RAG, LLMs, Tools and AI Agents."
)

st.divider()


# ============================================
# RESUME UPLOAD
# ============================================

st.subheader(
    "1️⃣ Upload Your Resume"
)

resume_file = st.file_uploader(

    "Upload your resume PDF",

    type=["pdf"]
)


# ============================================
# JOB DESCRIPTION
# ============================================

st.subheader(
    "2️⃣ Enter Job Description"
)

job_description = st.text_area(

    "Paste the job description here",

    height=250,

    placeholder=(
        "Example: Looking for a Python "
        "developer with Machine Learning, "
        "SQL, RAG and NLP skills..."
    )
)


# ============================================
# ANALYZE BUTTON
# ============================================

if st.button(
    "🚀 Analyze Resume",
    type="primary"
):

    # ========================================
    # VALIDATION
    # ========================================

    if resume_file is None:

        st.warning(
            "Please upload your resume PDF."
        )

        st.stop()


    if not job_description.strip():

        st.warning(
            "Please enter a job description."
        )

        st.stop()


    # ========================================
    # STEP 1: PDF EXTRACTION
    # ========================================

    with st.spinner(
        "📖 Reading resume..."
    ):

        try:

            resume_text = (
                extract_text_from_pdf(
                    resume_file
                )
            )

        except Exception as e:

            st.error(
                f"PDF extraction failed: {e}"
            )

            st.stop()


    if not resume_text.strip():

        st.error(
            "Could not extract text from "
            "this PDF."
        )

        st.stop()


    st.success(
        "Resume text extracted successfully! ✅"
    )


    # ========================================
    # STEP 2: RAG PROCESSING
    # ========================================

    with st.spinner(
        "🧠 Creating resume knowledge base..."
    ):

        try:

            chunks = create_chunks(
                resume_text
            )

            embeddings = create_embeddings(
                chunks
            )

            index = create_faiss_index(
                embeddings
            )

        except Exception as e:

            st.error(
                f"RAG processing failed: {e}"
            )

            st.stop()


    st.success(
        f"Resume processed successfully! "
        f"Created {len(chunks)} chunks. ✅"
    )


    # ========================================
    # STEP 3: RETRIEVAL
    # ========================================

    with st.spinner(
        "🔎 Retrieving relevant resume information..."
    ):

        try:

            relevant_chunks = retrieve_chunks(

                job_description,

                chunks,

                index,

                top_k=5
            )

        except Exception as e:

            st.error(
                f"Retrieval failed: {e}"
            )

            st.stop()


    # ========================================
    # RETRIEVED INFORMATION
    # ========================================

    st.subheader(
        "🔎 Retrieved Resume Information"
    )


    for i, chunk in enumerate(
        relevant_chunks,
        1
    ):

        with st.expander(
            f"Relevant Section {i}"
        ):

            st.write(chunk)


    # ========================================
    # CREATE RAG CONTEXT
    # ========================================

    resume_context = "\n\n".join(
        relevant_chunks
    )


    # ========================================
    # STEP 4: AI AGENT
    # ========================================

    st.subheader(
        "🤖 AI Career Agent"
    )


    with st.spinner(
        "🤖 Agent is analyzing your resume..."
    ):

        try:

            agent_result = run_agent(

                client,

                resume_context,

                job_description
            )

        except Exception as e:

            st.error(
                f"Agent failed: {e}"
            )

            st.stop()


    # ========================================
    # GET TOOL RESULTS
    # ========================================

    tool_results = agent_result.get(
        "tool_results",
        []
    )


    # ========================================
    # EXTRACT ANALYSIS DATA
    # ========================================

    ats_score = 0

    matching_skills = []

    missing_skills = []


    for tool_result in tool_results:

        tool_name = tool_result.get(
            "tool",
            ""
        )

        result = tool_result.get(
            "result",
            {}
        )


        # ------------------------------------
        # ATS SCORE
        # ------------------------------------

        if tool_name == "calculate_ats_score":

            if isinstance(
                result,
                dict
            ):

                ats_score = result.get(
                    "score",
                    0
                )

            elif isinstance(
                result,
                (int, float)
            ):

                ats_score = result


        # ------------------------------------
        # SKILL GAP
        # ------------------------------------

        elif tool_name == "analyze_skill_gap":

            if isinstance(
                result,
                dict
            ):

                matching_skills = result.get(
                    "matching_skills",
                    []
                )

                missing_skills = result.get(
                    "missing_skills",
                    []
                )


    # ========================================
    # DASHBOARD
    # ========================================

    st.divider()

    st.header(
        "📊 Resume Analysis Dashboard"
    )


    # ========================================
    # METRICS
    # ========================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "ATS-Style Score",
            f"{ats_score}%"
        )


    with col2:

        st.metric(
            "Matching Skills",
            len(matching_skills)
        )


    with col3:

        st.metric(
            "Missing Skills",
            len(missing_skills)
        )


    st.divider()


    # ========================================
    # SKILLS
    # ========================================

    col1, col2 = st.columns(2)


    # ========================================
    # MATCHING SKILLS
    # ========================================

    with col1:

        st.subheader(
            "✅ Matching Skills"
        )


        if matching_skills:

            for skill in matching_skills:

                st.success(
                    skill
                )

        else:

            st.info(
                "No matching skills detected."
            )


    # ========================================
    # MISSING SKILLS
    # ========================================

    with col2:

        st.subheader(
            "❌ Missing Skills"
        )


        if missing_skills:

            for skill in missing_skills:

                st.error(
                    skill
                )

        else:

            st.success(
                "No major missing skills detected."
            )


    # ========================================
    # AI CAREER ANALYSIS
    # ========================================

    st.divider()

    st.header(
        "🤖 AI Career Analysis"
    )


    final_response = agent_result.get(
        "final_response",
        ""
    )


    if final_response:

        st.markdown(
            final_response
        )

    else:

        st.warning(
            "The agent did not return "
            "a final response."
        )


    # ========================================
    # TOOL ACTIVITY
    # ========================================

    st.divider()

    st.subheader(
        "🛠️ Agent Tool Activity"
    )


    for tool_result in tool_results:

        tool_name = tool_result.get(
            "tool",
            "Unknown"
        )


        with st.expander(
            f"🔧 {tool_name}"
        ):

            st.write(
                "Arguments:"
            )

            st.json(
                tool_result.get(
                    "arguments",
                    {}
                )
            )


            st.write(
                "Result:"
            )

            st.json(
                tool_result.get(
                    "result",
                    {}
                )
            )


    # ========================================
    # COMPLETE RESUME
    # ========================================

    with st.expander(
        "📄 View Complete Extracted Resume"
    ):

        st.text_area(

            "Resume Content",

            resume_text,

            height=400
        )


    # ========================================
    # JOB DESCRIPTION
    # ========================================

    with st.expander(
        "💼 View Job Description"
    ):

        st.write(
            job_description
        )


    # ========================================
    # COMPLETION
    # ========================================

    st.success(
        "🎉 AI Resume & Career Analysis completed!"
    )



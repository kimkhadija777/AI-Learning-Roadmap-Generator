# ============================================================
# AI LEARNING ROADMAP GENERATOR
# Streamlit + Groq
# Deployment Ready for Streamlit Community Cloud
# ============================================================


# ============================================================
# IMPORT LIBRARIES
# ============================================================

import streamlit as st
from groq import Groq


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# GET GROQ API KEY FROM STREAMLIT SECRETS
# ============================================================

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

except Exception:
    st.error(
        "❌ GROQ_API_KEY was not found in Streamlit Secrets."
    )

    st.info(
        """
Go to:

Streamlit Cloud → App Settings → Secrets

Then add:

GROQ_API_KEY = "your_groq_api_key"
        """
    )

    st.stop()


# ============================================================
# CREATE GROQ CLIENT
# ============================================================

client = Groq(
    api_key=GROQ_API_KEY
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 19px;
        color: gray;
        margin-bottom: 30px;
    }

    .feature-box {
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# APPLICATION TITLE
# ============================================================

st.markdown(
    """
    <div class="main-title">
        🎓 AI Learning Roadmap Generator
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="subtitle">
        Create a personalized learning roadmap for any skill or domain using AI 🚀
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Learning Preferences")


    # DOMAIN

    domain = st.text_input(
        "📚 What do you want to learn?",
        placeholder="Example: Cybersecurity, AI, Web Development"
    )


    # SKILL LEVEL

    skill_level = st.selectbox(
        "📊 Current Skill Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )


    # LEARNING TIME

    learning_time = st.selectbox(
        "⏳ Time Available to Learn",
        [
            "1 Month",
            "2 Months",
            "3 Months",
            "6 Months",
            "9 Months",
            "1 Year"
        ]
    )


    # HOURS PER WEEK

    hours_per_week = st.selectbox(
        "🕒 Study Hours Per Week",
        [
            "3 hours",
            "5 hours",
            "7 hours",
            "10 hours",
            "15 hours",
            "20 hours"
        ]
    )


    # AI MODEL

    model = st.selectbox(
        "🤖 Select AI Model",
        [
            "openai/gpt-oss-20b",
            "openai/gpt-oss-120b"
        ],
        index=0
    )


    st.divider()


    generate_button = st.button(
        "🚀 Generate My Roadmap",
        use_container_width=True
    )


# ============================================================
# MAIN PAGE
# ============================================================

st.subheader("🗺️ Your Personalized Learning Journey")


# ============================================================
# DEFAULT WELCOME SCREEN
# ============================================================

if not generate_button:

    st.info(
        """
👋 Welcome!

Your AI-powered learning roadmap will be personalized according to:

📚 **Domain** — What you want to learn

📊 **Skill Level** — Beginner, Intermediate, or Advanced

⏳ **Learning Time** — Your available duration

🕒 **Study Hours** — How much time you can study each week

🤖 **AI Model** — Choose the Groq model you want to use

Fill in the information from the sidebar and click:

🚀 **Generate My Roadmap**
        """
    )


# ============================================================
# GENERATE ROADMAP
# ============================================================

if generate_button:


    # --------------------------------------------------------
    # VALIDATE DOMAIN
    # --------------------------------------------------------

    if not domain or domain.strip() == "":

        st.error(
            "❌ Please enter the domain or skill you want to learn."
        )


    else:


        # ----------------------------------------------------
        # LOADING SPINNER
        # ----------------------------------------------------

        with st.spinner(
            "🤖 AI is analyzing your learning requirements and creating your roadmap..."
        ):


            # ------------------------------------------------
            # CREATE PROMPT
            # ------------------------------------------------

            prompt = f"""
You are an expert learning advisor, curriculum designer,
and career mentor.

Your task is to create a personalized, realistic,
structured, and practical learning roadmap.

==================================================
USER PROFILE
==================================================

Domain or Skill to Learn:
{domain}

Current Skill Level:
{skill_level}

Available Learning Time:
{learning_time}

Available Study Hours Per Week:
{hours_per_week}


==================================================
YOUR RESPONSIBILITIES
==================================================

Create a learning roadmap that is specifically
personalized for this user.

Follow these rules:

1. Start with a short explanation of the learning journey.

2. Divide the roadmap into clear learning phases.

3. For EVERY phase include:

- Phase name
- Main goal
- Topics to learn
- Important concepts
- Practical skills
- Practice activities
- Estimated duration

4. Create a realistic learning timeline based on:

{learning_time}

5. Adapt the roadmap to the user's skill level.

IF BEGINNER:

- Start from fundamentals.
- Assume little or no previous knowledge.
- Explain concepts in a simple progression.
- Avoid jumping into advanced topics too early.

IF INTERMEDIATE:

- Assume basic knowledge already exists.
- Focus on strengthening skills.
- Include practical projects.
- Introduce more advanced concepts gradually.

IF ADVANCED:

- Focus on specialization.
- Include advanced concepts.
- Include professional-level projects.
- Include industry-relevant skills.

6. Include practical projects.

Projects should gradually increase in difficulty.

7. Include one strong final portfolio project.

8. Recommend useful:

- Tools
- Technologies
- Platforms
- Libraries
- Frameworks

Only include technologies relevant to the domain.

9. Add progress milestones so the learner
can measure their improvement.

10. Add common mistakes to avoid.

11. Create a realistic weekly study routine based on:

{hours_per_week}

12. Include practical career guidance.

13. Keep the roadmap realistic.

Do not overload the learner.

Focus on learning by doing.


==================================================
OUTPUT FORMAT
==================================================

# 🎯 Personalized Learning Roadmap

## 👤 Your Learning Profile

Summarize:

- Domain
- Current level
- Learning duration
- Weekly study hours


## 🗺️ Roadmap Overview

Give a short overview of the complete journey.


## 📚 Phase 1

Include:

### 🎯 Goal

### 📖 Topics to Learn

### 💡 Important Concepts

### 🛠️ Practical Skills

### 💻 Practice Activities

### ⏳ Estimated Duration


## 📚 Phase 2

Use the same structure.


## 📚 Phase 3

Use the same structure.

Add additional phases if necessary.


## 📅 Learning Timeline

Create a clear week-by-week or month-by-month timeline.


## 🛠️ Practical Projects

Suggest multiple projects from easy to difficult.


## 🚀 Final Portfolio Project

Suggest one strong final project.

Explain:

- What to build
- Important features
- Technologies to use
- Skills demonstrated


## 🧰 Recommended Tools and Technologies


## 🎯 Progress Milestones


## ⚠️ Common Mistakes to Avoid


## 🗓️ Weekly Study Routine


## 💼 Career Guidance


## 🎉 Final Advice


IMPORTANT:

- Use Markdown headings.
- Use clear bullet points.
- Use tables only when they improve readability.
- Use emojis moderately.
- Be practical.
- Be realistic.
- Personalize everything.
- Focus on practical skills and projects.
"""


            try:


                # =============================================
                # CALL GROQ API
                # =============================================

                response = client.chat.completions.create(

                    model=model,

                    messages=[

                        {
                            "role": "system",

                            "content": """
You are an expert AI learning roadmap generator.

Your job is to create high-quality, personalized,
structured, realistic, and practical learning roadmaps.

Always adapt the roadmap according to:

- User skill level
- Available learning duration
- Weekly study hours
- Complexity of the selected domain

Focus strongly on:

- Learning fundamentals correctly
- Practical skills
- Projects
- Portfolio building
- Realistic progress

Do not create unrealistic learning schedules.
"""
                        },


                        {
                            "role": "user",
                            "content": prompt
                        }

                    ],

                    temperature=0.7,

                    max_completion_tokens=5000

                )


                # =============================================
                # EXTRACT ROADMAP
                # =============================================

                roadmap = response.choices[0].message.content


                # =============================================
                # DISPLAY RESULT
                # =============================================

                st.success(
                    "🎉 Your personalized learning roadmap is ready!"
                )


                st.markdown(roadmap)


                # =============================================
                # DOWNLOAD ROADMAP
                # =============================================

                st.divider()


                st.download_button(

                    label="📥 Download My Roadmap",

                    data=roadmap,

                    file_name="my_learning_roadmap.md",

                    mime="text/markdown",

                    use_container_width=True

                )


            # ================================================
            # ERROR HANDLING
            # ================================================

            except Exception as e:


                st.error(
                    "❌ Unable to generate the roadmap."
                )


                st.code(
                    str(e)
                )


                st.info(
                    """
Please check:

1. Your Groq API key in Streamlit Secrets

2. Your selected Groq model

3. Groq API availability

4. Your API usage limits
                    """
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(
    "🎓 AI Learning Roadmap Generator | Built with Streamlit + Groq + GPT-OSS"
  )

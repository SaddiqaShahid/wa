import streamlit as st
import time

# ---------------------------------------------
# CareerAdvisor Pro: A More Intelligent Expert System
# ---------------------------------------------

# Page Configuration
st.set_page_config(
    page_title="CareerAdvisor Pro",
    page_icon="🚀",
    layout="wide"
)

# --- STYLING FOR MULTICOLOR MOVING BACKGROUND ---
st.markdown("""
    <style>
    /* Animated black to grey gradient */
    .stApp {
        background: linear-gradient(-45deg, #000000, #1c1c1c, #2e2e2e, #3f3f3f, #1c1c1c, #000000);
        background-size: 400% 400%;
        animation: greyFade 30s ease infinite;
        padding: 2rem;
        border-radius: 15px;
        color: white;
    }

    @keyframes greyFade {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Headings and text */
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stRadio, .stSubheader {
        color: #ffffff !important;
    }

    /* Buttons */
    .stButton > button {
        border: 2px solid #888;
        border-radius: 10px;
        color: white;
        background-color: transparent;
        transition: all 0.3s ease-in-out;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        background-color: #999;
        color: black;
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background-color: #999;
    }
    </style>
""", unsafe_allow_html=True)


# --- KNOWLEDGE BASE (RULES) ---
rules = {
    "AI Engineer": ["strong_math_skills", "likes_programming", "interested_in_ai", "problem_solver", "data_structures_knowledge"],
    "Data Scientist": ["strong_math_skills", "likes_programming", "interested_in_data", "statistics_knowledge", "good_communication"],
    "Web Developer": ["likes_programming", "interested_in_web", "likes_design", "team_player", "detail_oriented"],
    "UI/UX Designer": ["likes_design", "creative", "interested_in_human_behavior", "empathy", "visual_thinker"],
    "Cybersecurity Analyst": ["problem_solver", "interested_in_security", "attention_to_detail", "ethical_mindset", "networking_knowledge"],
    "Product Manager": ["leadership_skills", "good_communication", "strategic_thinker", "interested_in_business", "user_focused"],
    "Cloud Engineer (DevOps)": ["likes_programming", "networking_knowledge", "interested_in_automation", "problem_solver", "system_administration"],
}

# --- UI & APP LOGIC ---
st.title("🚀 CareerAdvisor Pro")
st.subheader("Your Personal AI-Powered Career Guidance Expert")

# --- EXPLAINING BACKWARD CHAINING ---
with st.expander("🤔 How does this use Backward Chaining?"):
    st.markdown("""
    This system works by starting with a Conclusion (a career) and working backwards to see if the evidence supports it. Here's the process:

    1.  You Select a Goal: You choose a potential career like "AI Engineer". This is the hypothesis the system wants to prove or disprove.
    2.  System Identifies Conditions: The system looks up the rule for "AI Engineer" and finds the required skills (e.g., likes programming, strong math skills, etc.). These are the conditions needed to satisfy the goal.
    3.  It Asks You Specific Questions: It then asks you targeted questions only about those required skills. It's working backward from the goal to the facts.
    4.  It Evaluates the Goal: Based on your answers, it calculates a match score. Instead of a simple "yes" or "no", it determines the likelihood that the career is a good fit for you.
    """)

# --- MAIN APP ---
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3221/3221626.png", width=150)
    st.markdown("### 1. Select a Career to Evaluate")
    selected_career_key = st.selectbox(
        "Choose a career path:",
        options=list(rules.keys())
    )

with col2:
    if selected_career_key:
        st.markdown(f"### 2. Answer Questions for '{selected_career_key}'")
        st.write("Be honest! This will help give you the best recommendation.")

        with st.form(key='career_form'):
            user_facts = {}
            required_skills = rules[selected_career_key]

            for skill in required_skills:
                question = f"Do you have/are you interested in... {skill.replace('_', ' ').capitalize()}?"
                user_facts[skill] = st.radio(question, ("Yes", "No"), horizontal=True) == "Yes"

            submitted = st.form_submit_button("Analyze My Fit!")

        if submitted:
            matched_skills_count = sum(1 for skill in required_skills if user_facts.get(skill, False))
            total_required = len(required_skills)
            match_percentage = (matched_skills_count / total_required) * 100

            st.markdown("---")
            st.markdown("### 📊 Your Match Analysis")

            my_bar = st.progress(0)
            for percent_complete in range(int(match_percentage) + 1):
                time.sleep(0.01)
                my_bar.progress(percent_complete)

            if match_percentage >= 80:
                st.success(f"Excellent Match! ({match_percentage:.0f}%)")
                st.balloons()
                st.write(f"Based on your answers, {selected_career_key} is a highly suitable career path for you.")
            elif match_percentage >= 50:
                st.warning(f"Good Potential! ({match_percentage:.0f}%)")
                st.write(f"You have a solid foundation for a career as a {selected_career_key}. There are a few areas you could strengthen.")
            else:
                st.error(f"Needs Development. ({match_percentage:.0f}%)")
                st.write(f"A career as a {selected_career_key} might be a stretch right now, but it's achievable if you focus on developing the missing skills.")

            st.markdown("#### Skill Breakdown:")
            matched_skills = [skill.replace('_', ' ').capitalize() for skill in required_skills if user_facts.get(skill, False)]
            missing_skills = [skill.replace('_', ' ').capitalize() for skill in required_skills if not user_facts.get(skill, False)]

            if matched_skills:
                st.markdown("✅ Skills You Have:")
                for skill in matched_skills:
                    st.markdown(f"- {skill}")

            if missing_skills:
                st.markdown("🚧 Skills to Develop:")
                for skill in missing_skills:
                    st.markdown(f"- {skill}")
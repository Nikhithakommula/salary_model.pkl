import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt




st.set_page_config(
    page_title="CareerFit AI",
    page_icon="🎯",
    layout="wide"
)




model = joblib.load(
    "model/salary_model.pkl"
)




ROLE_SKILLS = {

    "Data Scientist": [
        "Python",
        "SQL",
        "Machine Learning",
        "Statistics",
        "Pandas",
        "Data Visualization"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics",
        "Data Visualization"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Scikit-learn",
        "SQL",
        "Deep Learning",
        "Docker"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "NLP",
        "Docker"
    ],

    "Software Engineer": [
        "Python",
        "DSA",
        "SQL",
        "Git",
        "OOP",
        "Problem Solving"
    ]
}




st.title(" CareerFit AI")

st.subheader(
    "AI-Powered Job Fit, Salary & Skill Gap Analyzer"
)

st.write(
    """
    Analyze your career profile, estimate your salary,
    measure job readiness and identify skills to improve.
    """
)

st.divider()




st.sidebar.header("👤 Candidate Profile")

education = st.sidebar.selectbox(
    "Education Level",
    [
        "High School",
        "Bachelor's",
        "Master's",
        "PhD"
    ]
)

experience = st.sidebar.number_input(
    "Experience (Years)",
    min_value=0.0,
    max_value=40.0,
    value=1.0,
    step=0.5
)

target_role = st.sidebar.selectbox(
    "Target Job Role",
    list(ROLE_SKILLS.keys())
)

skills_count = st.sidebar.number_input(
    "Number of Skills",
    min_value=0,
    max_value=30,
    value=5
)

certifications = st.sidebar.number_input(
    "Number of Certifications",
    min_value=0,
    max_value=20,
    value=1
)

industry = st.sidebar.selectbox(
    "Industry",
    [
        "Technology",
        "Finance",
        "Healthcare",
        "Education",
        "Retail",
        "Manufacturing"
    ]
)

company_size = st.sidebar.selectbox(
    "Company Size",
    [
        "Small",
        "Medium",
        "Large"
    ]
)

location = st.sidebar.selectbox(
    "Location",
    [
        "Hyderabad",
        "Bangalore",
        "Chennai",
        "Mumbai",
        "Delhi",
        "Pune"
    ]
)

remote_work = st.sidebar.selectbox(
    "Remote Work",
    [
        "Yes",
        "No"
    ]
)



st.subheader(" Your Skills")

user_skills = st.multiselect(
    "Select the skills you currently have",
    [
        "Python",
        "SQL",
        "Machine Learning",
        "Statistics",
        "Pandas",
        "Data Visualization",
        "Excel",
        "Power BI",
        "Scikit-learn",
        "Deep Learning",
        "TensorFlow",
        "NLP",
        "Docker",
        "Git",
        "DSA",
        "OOP",
        "Problem Solving"
    ]
)



analyze = st.button(
    "🚀 Analyze My Career Profile",
    use_container_width=True
)


if analyze:

    
    input_data = pd.DataFrame({

        "experience_years": [experience],

        "education_level": [education],

        "job_title": [target_role],

        "skills_count": [skills_count],

        "industry": [industry],

        "company_size": [company_size],

        "location": [location],

        "remote_work": [remote_work],

        "certifications": [certifications]
    })


    prediction = model.predict(
        input_data
    )[0]


    

    required_skills = set(
        ROLE_SKILLS[target_role]
    )

    candidate_skills = set(
        user_skills
    )

    matched_skills = (
        required_skills
        & candidate_skills
    )

    missing_skills = (
        required_skills
        - candidate_skills
    )


    if len(required_skills) > 0:

        skill_score = (
            len(matched_skills)
            / len(required_skills)
        ) * 100

    else:

        skill_score = 0


    

    experience_score = min(
        experience / 5 * 100,
        100
    )


    

    certification_score = min(
        certifications / 3 * 100,
        100
    )


    

    career_score = (
        skill_score * 0.60
        + experience_score * 0.25
        + certification_score * 0.15
    )


    

    st.divider()

    st.header("📊 Career Analysis")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "🎯 Job Fit Score",
            f"{career_score:.0f}%"
        )


    with col2:

        st.metric(
            "💰 Estimated Salary",
            f"${prediction:,.0f}"
        )


    with col3:

        st.metric(
            "🧠 Skills Matched",
            f"{len(matched_skills)} / {len(required_skills)}"
        )


    

    st.subheader("Career Readiness")

    st.progress(
        int(career_score)
    )


    

    st.subheader(" Strong Skills")

    if matched_skills:

        st.success(
            ", ".join(
                sorted(matched_skills)
            )
        )

    else:

        st.warning(
            "No matching skills found yet."
        )


    
    st.subheader(" Skill Gap")

    if missing_skills:

        for skill in sorted(missing_skills):

            st.write(
                f"🔸 {skill}"
            )

    else:

        st.success(
            "Excellent! You have all the core skills."
        )


    

    st.subheader(
        "🚀 Recommended Next Steps"
    )


    recommendations = []


    if missing_skills:

        recommendations.append(
            f"Learn: {', '.join(sorted(missing_skills))}"
        )


    if experience < 1:

        recommendations.append(
            "Build practical projects or gain internship experience."
        )


    if certifications == 0:

        recommendations.append(
            "Consider completing one relevant certification."
        )


    if skills_count < 5:

        recommendations.append(
            "Expand your technical skill set."
        )


    if not recommendations:

        recommendations.append(
            "Keep building projects and strengthen your interview preparation."
        )


    for i, recommendation in enumerate(
        recommendations,
        start=1
    ):

        st.write(
            f"**{i}.** {recommendation}"
        )


    

    st.subheader(
        "💡 AI Career Assessment"
    )


    if career_score >= 80:

        st.success(
            "Excellent match! Your profile is highly aligned with this role."
        )

    elif career_score >= 60:

        st.info(
            "Good match! A few improvements can make your profile stronger."
        )

    else:

        st.warning(
            "Your profile needs improvement for this role. Focus on the identified skill gaps."
        )



    st.subheader(
        "📈 Skill Match Visualization"
    )


    labels = [
        "Matched Skills",
        "Missing Skills"
    ]

    values = [
        len(matched_skills),
        len(missing_skills)
    ]


    fig, ax = plt.subplots()

    ax.bar(
        labels,
        values
    )

    ax.set_ylabel(
        "Number of Skills"
    )

    ax.set_title(
        f"{target_role} Skill Analysis"
    )

    st.pyplot(fig)


    

    with st.expander(
        "🔍 About the ML Model"
    ):

        st.write(
            """
            The salary prediction component uses a
            Random Forest Regression model.

            Categorical features are transformed using
            One-Hot Encoding through a Scikit-learn
            preprocessing pipeline.

            The model was trained using job-related
            features such as experience, education,
            job title, skills count, industry,
            company size, location, remote work and
            certifications.
            """
        )

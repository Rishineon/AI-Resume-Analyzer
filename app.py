import streamlit as st
import pdfplumber
import matplotlib.pyplot as plt

SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "SQL",
    "MySQL",
    "MongoDB",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Power BI",
    "Tableau",
    "Excel",
    "Git",
    "GitHub",
    "Streamlit",
    "VS Code"
]

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    st.success("Resume uploaded successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )
    found_skills = []

for skill in SKILLS:
    if skill.lower() in text.lower():
        found_skills.append(skill)
st.subheader("Resume Sections Check")

sections = {
    "Education": "education" in text.lower(),
    "Skills": "skills" in text.lower(),
    "Projects": "project" in text.lower(),
    "Experience": "experience" in text.lower(),
    "Certifications": "certification" in text.lower() or "certificate" in text.lower()
}

for section, present in sections.items():
    if present:
        st.success(f"✅ {section}")
    else:
        st.error(f"❌ {section}")
st.subheader("Detected Skills")

if found_skills:
    for skill in found_skills:
        st.success(skill)
else:
    st.warning("No skills detected")

st.subheader("ATS Score")

total_skills = len(SKILLS)
detected_skills = len(found_skills)

ats_score = int((detected_skills / total_skills) * 100)
missing_skills = []
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ATS Score", f"{ats_score}%")

with col2:
    st.metric("Skills Found", len(found_skills))

with col3:
    st.metric("Missing Skills", len(missing_skills))
st.success(f"ATS Score: {ats_score}/100")
st.subheader("📊 ATS Score Breakdown")

score_data = {
    "Skills": min(len(found_skills) * 5, 40),
    "Projects": 20 if sections["Projects"] else 0,
    "Experience": 20 if sections["Experience"] else 0,
    "Certifications": 10 if sections["Certifications"] else 0,
    "Education": 10 if sections["Education"] else 0
}

st.bar_chart(score_data)
st.subheader("Resume Strength")

if ats_score >= 80:
    st.success("🌟 Excellent Resume")
elif ats_score >= 60:
    st.info("👍 Good Resume")
elif ats_score >= 40:
    st.warning("⚠️ Average Resume")
else:
    st.error("❌ Poor Resume")
st.subheader("Target Job Role")

role = st.selectbox(
    "Choose a Role",
    [
        "AIML Engineer",
        "Data Analyst",
        "Data Scientist",
        "Business Analyst"
    ]
)
st.subheader("🏢 Company ATS Requirements")

company = st.selectbox(
    "Choose a Company",
    ["Google", "Amazon", "Microsoft", "IBM", "Capgemini", "Infosys", "TCS"]
)

company_scores = {
    "Google": 85,
    "Amazon": 80,
    "Microsoft": 85,
    "IBM": 75,
    "Capgemini": 70,
    "Infosys": 65,
    "TCS": 60
}

required_score = company_scores[company]

st.info(f"{company} Recommended ATS Score: {required_score}")

if ats_score >= required_score:
    st.success(f"✅ Your resume meets {company}'s ATS requirement")
else:
    st.warning(f"⚠️ Improve your resume to reach {company}'s ATS requirement")

role_skills = {
    "AIML Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Pandas",
        "NumPy"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Tableau",
        "Pandas"
    ],

    "Data Scientist": [
        "Python",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "SQL",
        "TensorFlow"
    ],

    "Business Analyst": [
        "SQL",
        "Excel",
        "Power BI",
        "Tableau"
    ]
}

required_skills = role_skills[role]

missing_skills = []

for skill in required_skills:
    if skill not in found_skills:
        missing_skills.append(skill)

st.subheader("Missing Skills")

if missing_skills:
    for skill in missing_skills:
        st.error(skill)
else:
    st.success("No missing skills found!")
st.subheader("Resume Match Percentage")

match_percentage = int(
    ((len(required_skills) - len(missing_skills))
     / len(required_skills)) * 100
)

st.progress(match_percentage)

st.success(f"Resume Match: {match_percentage}%")
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="ATS Score",
        value=f"{ats_score}/100"
    )

with col2:
    st.metric(
        label="Resume Match",
        value=f"{match_percentage}%"
    )
    st.subheader("Resume Summary")

st.subheader("Resume Strength")

if ats_score >= 80:
    st.success("Strong Resume 💪")
elif ats_score >= 60:
    st.warning("Average Resume ⚡")
else:
    st.error("Weak Resume 🚨")

st.info(f"""
Skills Found: {len(found_skills)}

ATS Score: {ats_score}/100

Target Role: {role}

Resume Match: {match_percentage}%
""")
st.subheader("Learning Recommendations")

recommendations = {
    "Machine Learning":
        "Learn Machine Learning by Andrew Ng (Coursera)",

    "Deep Learning":
        "Complete Deep Learning Specialization (Coursera)",

    "TensorFlow":
        "Learn TensorFlow from TensorFlow.org tutorials",

    "Power BI":
        "Complete Microsoft Power BI Learning Path",

    "Tableau":
        "Learn Tableau for Data Analytics",

    "SQL":
        "Practice SQL on HackerRank and LeetCode",

    "Python":
        "Practice Python on LeetCode and CodeChef"
}

for skill in missing_skills:
    if skill in recommendations:
        st.info(f"{skill} → {recommendations[skill]}")
         
st.subheader("Placement Readiness")

if match_percentage >= 80:
    st.success("Placement Ready ✅")

elif match_percentage >= 60:
    st.warning("Almost Ready ⚠️")

else:
    st.error("Needs Improvement ❌")
    st.subheader("Skill Gap Analysis")
found_count = len(required_skills) - len(missing_skills)
missing_count = len(missing_skills)

match_percentage = int((found_count / len(required_skills)) * 100)

st.write(f"✅ Skills Matched: {found_count}")
st.write(f"❌ Skills Missing: {missing_count}")
st.write(f"📊 Match Percentage: {match_percentage}%")
fig, ax = plt.subplots()

ax.pie(
    [found_count, missing_count],
    labels=["Skills Present", "Skills Missing"],
    autopct="%1.1f%%"
)

ax.set_title("Skill Gap Analysis")
import matplotlib.pyplot as plt

labels = ["Matched Skills", "Missing Skills"]
sizes = [len(found_skills), len(missing_skills)]

fig, ax = plt.subplots()
ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)
ax.axis("equal")

st.pyplot(fig)
report = f"""
AI Resume Analyzer Report

ATS Score: {ats_score}/100
Resume Match: {match_percentage}%

Skills Found:
{', '.join(found_skills)}

Missing Skills:
{', '.join(missing_skills)}

Placement Readiness:
{"Ready" if match_percentage >= 80 else "Needs Improvement"}
"""
st.subheader("Top Resume Improvement Suggestions")

suggestions = []

if ats_score < 80:
    suggestions.append("Increase ATS score by adding more relevant skills.")

if len(missing_skills) > 0:
    suggestions.append("Learn and add missing skills related to your target role.")

if "Projects" in sections and not sections["Projects"]:
    suggestions.append("Add at least 2-3 technical projects.")

if "Certifications" in sections and not sections["Certifications"]:
    suggestions.append("Include certifications from Coursera, Google, Microsoft or IBM.")

if match_percentage < 70:
    suggestions.append("Improve resume match percentage for your selected role.")

for suggestion in suggestions:
    st.warning(suggestion)

st.download_button(
    label="📄 Download Report",
    data=report,
    file_name="resume_analysis_report.txt",
    mime="text/plain"
)
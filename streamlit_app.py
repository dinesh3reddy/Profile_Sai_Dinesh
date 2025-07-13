import streamlit as st

# Page Config
st.set_page_config(page_title="Sai Palavalli Resume", layout="wide")

# Sidebar - Contact
st.sidebar.title("Contact Info")
st.sidebar.markdown("""
**Sai Palavalli**  
📍 Fort Worth, TX  
📧 sai3dinesh@gmail.com  
📞 +1 817-(264)-1590  
""")

st.title("Sai Palavalli")
st.subheader("Data Science & Airport Simulation Specialist")

# ---- PROFESSIONAL SUMMARY ----
st.markdown("## 🧾 Professional Summary")
st.text_area("Write your professional summary here:", height=150)

# ---- EXPERIENCE ----
st.markdown("## 💼 Professional Experience")

with st.expander("🔹 TransSolutions, LLC – Associate (Aug 2023 – Present)"):
    st.text_area("Your description of work at TransSolutions:", height=180)
    st.text_area("Explain your impact/results at TransSolutions:", height=120)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", format="video/mp4")

with st.expander("🔹 University of Texas at Arlington"):
    st.text_area("Describe your Research Assistant role:", height=100)
    st.text_area("Describe your Teaching Assistant role:", height=100)

# ---- PROJECTS ----
st.markdown("## 🧪 Projects")

with st.expander("✈️ Passenger Forecasting – RDU"):
    st.text_area("Write about the RDU Forecasting Project:", height=120)
    st.text_area("Explain the optimization method you used:", height=100)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with st.expander("📊 BTS Dashboard"):
    st.text_area("Describe the BTS Dashboard project:", height=100)
    st.text_area("What was the impact and user value?", height=100)

with st.expander("📈 DFW Flow Automation"):
    st.text_area("Describe how you automated reports for DFW:", height=100)
    st.text_area("Explain the tools used and results achieved:", height=100)

# ---- PERSONAL PROJECTS ----
st.markdown("## 🧠 Personal Projects")

with st.expander("💸 Airline Fare Prediction"):
    st.text_area("Explain the machine learning model:", height=100)
    st.text_area("What insights or accuracy did you achieve?", height=100)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with st.expander("👥 Customer Churn Prediction"):
    st.text_area("Describe your approach for churn prediction:", height=100)
    st.text_area("How was it used in marketing or retention?", height=100)

with st.expander("🔤 Sentiment Analysis on Amazon Reviews"):
    st.text_area("Describe your NLP pipeline:", height=100)
    st.text_area("Model used and deployment setup:", height=100)

# ---- EDUCATION ----
st.markdown("## 🎓 Education")
st.text_area("Your education summary:", "MS in Data Science – UT Arlington\nBE in ECE – VIT")

# ---- SKILLS ----
st.markdown("## 🛠️ Technical Skills")
st.text_area("List your technical skills (comma separated or bullet list):", height=120)

# ---- OPTIONAL: PROJECT VIDEOS OR PORTFOLIO ----
st.markdown("## 🎬 Project Video Demos (Optional)")
video_urls = st.text_area("Paste YouTube or video URLs here (one per line):", height=100)
for url in video_urls.splitlines():
    if url.strip():
        st.video(url.strip())

# ---- FOOTER ----
st.markdown("---")




import streamlit as st

st.set_page_config(
    page_title="ATTENDIQ",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0B0F12;
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

[data-testid="stMetric"] {
    background-color: #171F23;
    border: 1px solid #176B68;
    padding: 20px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("ATTENDIQ")
st.caption("STUDENT ATTENDANCE ANALYTICS DASHBOARD")

st.markdown("---")

st.subheader("Welcome to ATTENDIQ")

st.write(
    "Turning Attendance Data into Academic Insights."
)

st.info(
    "Your platform for understanding student attendance."
)

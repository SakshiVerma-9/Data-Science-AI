import streamlit as st

st.set_page_config(page_title="Student Profile", layout="centered")

st.title("Task 1: Student Profile Card")

st.divider()

st.subheader("🎓 STUDENT PROFILE")

st.image("https://via.placeholder.com/120", width=120)

col1, col2 = st.columns([1,2])

with col1:
    st.write("**Name**")
    st.write("**Course**")
    st.write("**College**")
    st.write("**Email**")
    st.write("**Phone**")

with col2:
    st.write("Sakshi Verma")
    st.write("Data Science")
    st.write("BBD University")
    st.write("sakshiverma.141111@gmail.com")
    st.write("8303966634")

st.write("### Skills")
st.write("✔ Python")
st.write("✔ Machine Learning")
st.write("✔ SQL")

st.button("Edit Profile")
import streamlit as st

st.set_page_config(page_title="Student Profile", layout="centered")

# CSS Styling
st.markdown("""
<style>
.profile-card{
    border:2px solid #888;
    border-radius:10px;
    padding:25px;
    width:500px;
    margin:auto;
    background-color:#fdfdfd;
}
.title{
    text-align:center;
    font-size:28px;
    font-weight:bold;
}
.subtitle{
    text-align:center;
    font-size:22px;
    margin-bottom:20px;
}
.photo{
    text-align:center;
    font-size:70px;
}
.info{
    font-size:18px;
    line-height:2;
}
.skills{
    font-size:18px;
}
.button{
    text-align:center;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

st.title("Student Profile Card")

st.markdown('<div class="profile-card">', unsafe_allow_html=True)

st.markdown('<div class="subtitle">🎓 STUDENT PROFILE</div>', unsafe_allow_html=True)

st.markdown('<div class="photo">👤</div>', unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Student Photo</h4>", unsafe_allow_html=True)

col1,col2=st.columns([1,2])

with col1:
    st.write("**Name**")
    st.write("**Course**")
    st.write("**College**")
    st.write("**Email**")
    st.write("**Phone**")

with col2:
    st.write(": Sakshi Verma")
    st.write(": Data Science")
    st.write(": BBD University")
    st.write(": sakshiverma.141111@gmail.com")
    st.write(": 8303966634")

st.markdown("### Skills")
st.write("✔ Python")
st.write("✔ Machine Learning")
st.write("✔ SQL")

st.markdown("<br>", unsafe_allow_html=True)

st.button("Edit Profile")

st.markdown("</div>", unsafe_allow_html=True)
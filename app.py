import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit page settings
st.set_page_config(page_title="Education Stream Recommender", layout="centered")

st.title("Education Stream Recommendation System")

# Input form
with st.form("student_form"):
    st.subheader("Enter Student Details")

    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.slider("Age", 10, 25, 18)
    tenth = st.number_input("10th Score (%)", min_value=0.0, max_value=100.0, step=0.1)
    twelfth = st.number_input("12th Score (%)", min_value=0.0, max_value=100.0, step=0.1)
    graduation = st.number_input("Graduation Grade (%)", min_value=0.0, max_value=100.0, step=0.1)
    
    # Add the missing inputs here:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    subject = st.selectbox("Preferred Subject", ["Math", "Science", "Commerce", "Arts"])
    interest = st.text_input("Interest Area (e.g., AI, Coding, Biology)")
    
    skill_strength = st.selectbox("Skill Strength", ["Problem Solving", "Creativity", "Teamwork", "Communication", "Leadership"])
    career_goal = st.selectbox("Career Goal", ["Engineer", "Scientist", "Artist", "Entrepreneur", "Doctor", "Researcher"])
    
    submit = st.form_submit_button("🔍 Recommend Stream")

if submit:
    # Build DataFrame including all required fields
    df = pd.DataFrame([{
        'Name': name,
        'Email': email,
        'Age': age,
        '10th Score (%)': tenth,
        '12th Score (%)': twelfth,
        'Graduation Grade (%)': graduation,
        'Gender': gender,
        'Preferred Subject': subject,
        'Interest Area': interest,
        'Skill Strength': skill_strength,
        'Career Goal': career_goal
    }])

    # Make prediction
    recommended_stream = model.predict(df)[0]
    st.success(f"Recommended Stream: **{recommended_stream}**")

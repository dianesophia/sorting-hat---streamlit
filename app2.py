import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('house_predictor_model.pkl')

# Page configuration
st.set_page_config(page_title="Hogwarts House Predictor", page_icon="🧙‍♂️", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h4 {
            font-family: 'Georgia', serif;
            color: #4b0082;
        }
        .stButton>button {
            background-color: #6A1B9A;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1.5em;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #4b0082;
        }
        footer {
            margin-top: 3rem;
            text-align: center;
            color: gray;
            font-size: 0.8rem;
        }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🧙‍♀️ Hogwarts House Predictor")
st.markdown("#### Answer the questions to discover your magical destiny!")

# Scoring system
bravery_q = st.radio("1. What would you do if you saw someone being bullied?",
    ("Walk away (2)", "Tell a teacher (5)", "Stand up to the bully (10)"))
intelligence_q = st.radio("2. What do you enjoy most?",
    ("Solving puzzles (10)", "Reading novels (7)", "Watching movies (3)"))
loyalty_q = st.radio("3. How do you handle secrets?",
    ("I never tell anyone (10)", "Depends on the secret (5)", "I might slip (2)"))
ambition_q = st.radio("4. What drives you the most?",
    ("Power and recognition (10)", "Doing what’s right (4)", "Helping others (6)"))

# Convert answers to scores
bravery_score = {"Walk away (2)": 2, "Tell a teacher (5)": 5, "Stand up to the bully (10)": 10}[bravery_q]
intelligence_score = {"Solving puzzles (10)": 10, "Reading novels (7)": 7, "Watching movies (3)": 3}[intelligence_q]
loyalty_score = {"I never tell anyone (10)": 10, "Depends on the secret (5)": 5, "I might slip (2)": 2}[loyalty_q]
ambition_score = {"Power and recognition (10)": 10, "Doing what’s right (4)": 4, "Helping others (6)": 6}[ambition_q]

# Prediction
if st.button("✨ Predict My House"):
    features = np.array([[bravery_score, intelligence_score, loyalty_score, ambition_score]])
    prediction = model.predict(features)[0]

    house_colors = {
        "Gryffindor": "#ae0001",
        "Ravenclaw": "#0e1a40",
        "Hufflepuff": "#ecb939",
        "Slytherin": "#2a623d"
    }

    st.markdown(f"""
        <div style="background-color: {house_colors[prediction]}; padding: 20px; border-radius: 10px;">
            <h2 style="color: white; text-align: center;">🏰 You belong to <strong>{prediction}</strong>! 🏆</h2>
        </div>
    """, unsafe_allow_html=True)

# End container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<footer>© 2025 All rights reserved by Diane Sophia. This app is inspired by the Harry Potter universe.</footer>", unsafe_allow_html=True)

import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('house_predictor_model.pkl')

# Page configuration
st.set_page_config(page_title="Hogwarts House Predictor", page_icon="🧙‍♂️", layout="centered")

# Custom CSS styling
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
st.markdown("#### Enter your traits and discover your magical destiny!")

# Sliders
bravery = st.slider("🦁 Bravery", 1, 10, 5)
intelligence = st.slider("🦅 Intelligence", 1, 10, 5)
loyalty = st.slider("🦡 Loyalty", 1, 10, 5)
ambition = st.slider("🐍 Ambition", 1, 10, 5)

# Prediction
if st.button("✨ Predict My House"):
    features = np.array([[bravery, intelligence, loyalty, ambition]])
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

# End main container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<footer>© 2025 All rights reserved by Diane Sophia. This app is inspired by the Harry Potter universe.</footer>", unsafe_allow_html=True)

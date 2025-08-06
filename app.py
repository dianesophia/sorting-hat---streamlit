import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('house_predictor_model.pkl')

# Page config
st.set_page_config(page_title="Hogwarts House Predictor", page_icon="🧙‍♂️", layout="centered")

# Apply custom style
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: #fff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        h1 {
            color: #6A1B9A;
            text-align: center;
            font-family: 'Georgia';
        }
        .stButton button {
            background-color: #6A1B9A;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1.5em;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🧙‍♀️ Hogwarts House Predictor")
st.markdown("#### Enter your traits and discover your magical destiny!")

# Input sliders
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

    # Optional: Show house banner
    # st.image(f"{prediction.lower()}.png", width=300)  # Make sure image file is present

st.markdown("</div>", unsafe_allow_html=True)

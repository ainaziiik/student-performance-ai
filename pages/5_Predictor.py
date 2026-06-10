import streamlit as st

st.title("🔮 Student Performance Predictor")

dataset = st.selectbox(
    "Выберите датасет",
    [
        "UCI School",
        "PIP University"
    ]
)

st.write("Выбран:", dataset)

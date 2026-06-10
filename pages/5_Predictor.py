import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.title("🔮 Student Performance Predictor")
print(df.columns.tolist())
dataset = st.selectbox(
    "Выберите датасет",
    [
        "UCI School",
        "PIP University"
    ]
)

st.write("Выбран:", dataset)

if dataset == "PIP University":

    st.subheader("🎓 Параметры студента")

    age = st.slider(
        "Возраст",
        17,
        70,
        20
    )

    admission_grade = st.slider(
        "Оценка поступления",
        0,
        200,
        120
    )

    scholarship = st.selectbox(
        "Стипендия",
        [0, 1]
    )

    debtor = st.selectbox(
        "Есть задолженность?",
        [0, 1]
    )

    tuition = st.selectbox(
        "Обучение оплачено?",
        [0, 1]
    )

    if st.button("🔮 Predict"):

        if score > 120:

            st.success(
                "✅ Student will Graduate"
            )

        else:

            st.error(
                "⚠️ Student Needs Support"
            )

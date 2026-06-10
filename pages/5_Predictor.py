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

import streamlit as st

st.title("🔮 Student Performance Predictor")

dataset = st.selectbox(
    "Выберите датасет",
    ["UCI School", "PIP University"]
)

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

        score = (
            admission_grade
            + scholarship * 20
            + tuition * 20
            - debtor * 30
        )

        if score > 120:

            st.success(
                "✅ Student will Graduate"
            )

        else:

            st.error(
                "⚠️ Student Needs Support"
            )

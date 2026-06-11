import streamlit as st

st.title("🔮 Student Performance Predictor")

dataset = st.selectbox(
    "Выберите датасет",
    [
        "UCI School",
        "PIP University"
    ]
)

# =====================
# PIP
# =====================

if dataset == "PIP University":

    st.subheader("🎓 Параметры студента")

    age = st.slider(
        "Age at enrollment",
        17,
        70,
        20
    )

    admission_grade = st.slider(
        "Admission grade",
        0,
        200,
        120
    )

    scholarship = st.selectbox(
        "Scholarship holder",
        ["No", "Yes"]
    )

    debtor = st.selectbox(
        "Debtor",
        ["No", "Yes"]
    )

    tuition = st.selectbox(
        "Tuition fees up to date",
        ["No", "Yes"]
    )

    if st.button("🔮 Predict PIP"):

        score = admission_grade

        if scholarship == "Yes":
            score += 20

        if tuition == "Yes":
            score += 20

        if debtor == "Yes":
            score -= 40

        if score >= 130:
            st.success("✅ Student is likely to Graduate")
        elif score >= 90:
            st.warning("📚 Student may remain Enrolled")
        else:
            st.error("⚠️ Student is at risk of Dropout")


# =====================
# UCI
# =====================

elif dataset == "UCI School":

    st.subheader("🏫 Параметры школьника")

    age = st.slider(
        "Возраст",
        15,
        22,
        17
    )

    studytime = st.slider(
        "Время обучения (часов)",
        1,
        10,
        4
    )

    absences = st.slider(
        "Количество пропусков",
        0,
        100,
        5
    )

    freetime = st.slider(
        "Свободное время",
        1,
        5,
        3
    )

    parent_education = st.slider(
        "Образование родителей",
        0,
        4,
        2
    )

    if st.button("🔮 Predict UCI"):

        score = (
            studytime * 15
            + parent_education * 10
            + freetime * 5
            - absences * 2
        )

        if score >= 50:
            st.success("✅ Student will Pass")
        else:
            st.error("⚠️ Student Needs Support")

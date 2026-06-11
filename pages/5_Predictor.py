import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.title("🔮 Student Performance Predictor")

dataset = st.selectbox(
    "Выберите датасет",
    [
        "UCI School",
        "PIP University"
    ]
)
if dataset == "PIP University":
    df = pd.read_csv(
        "Student performance (Polytechnic Institute of Portalegre).csv"
    )
    
    data_clean = df.copy()
    
    label_encoders = {}
    
    for col in data_clean.columns:
        if data_clean[col].dtype == "object":
            le = LabelEncoder()
            data_clean[col] = le.fit_transform(
                data_clean[col].astype(str)
            )
            label_encoders[col] = le
    
    X = data_clean.drop("Target", axis=1)
    y = data_clean["Target"]
    
    model = RandomForestClassifier(
        random_state=42
    )
    
    model.fit(X, y)
    
    
    
    st.subheader("🎓 Введите данные студента")
    
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
        [0, 1]
    )
    
    debtor = st.selectbox(
        "Debtor",
        [0, 1]
    )
    
    tuition = st.selectbox(
        "Tuition fees up to date",
        [0, 1]
    )
    
    gender = st.selectbox(
        "Gender",
        [0, 1]
    )
    
    if st.button("🔮 Predict"):
    
        student = pd.DataFrame({
            "Marital status":[1],
            "Application mode":[1],
            "Application order":[1],
            "Course":[1],
            "Daytime/evening attendance\t":[1],
            "Previous qualification":[1],
            "Previous qualification (grade)":[120],
            "Nacionality":[1],
            "Mother's qualification":[1],
            "Father's qualification":[1],
            "Mother's occupation":[1],
            "Father's occupation":[1],
            "Admission grade":[admission_grade],
            "Displaced":[0],
            "Educational special needs":[0],
            "Debtor":[debtor],
            "Tuition fees up to date":[tuition],
            "Gender":[gender],
            "Scholarship holder":[scholarship],
            "Age at enrollment":[age],
            "International":[0],
            "Curricular units 1st sem (credited)":[0],
            "Curricular units 1st sem (enrolled)":[6],
            "Curricular units 1st sem (evaluations)":[6],
            "Curricular units 1st sem (approved)":[5],
            "Curricular units 1st sem (grade)":[12],
            "Curricular units 1st sem (without evaluations)":[0],
            "Curricular units 2nd sem (credited)":[0],
            "Curricular units 2nd sem (enrolled)":[6],
            "Curricular units 2nd sem (evaluations)":[6],
            "Curricular units 2nd sem (approved)":[5],
            "Curricular units 2nd sem (grade)":[12],
            "Curricular units 2nd sem (without evaluations)":[0],
            "Unemployment rate":[10],
            "Inflation rate":[1],
            "GDP":[0]
        })
    
        prediction = model.predict(student)[0]
    
      st.write("Prediction:", prediction)
    
        if result == "Graduate":
            st.success(
                "✅ Student is likely to Graduate"
            )
    
        elif result == "Dropout":
            st.error(
                "⚠️ Student is at risk of Dropout"
            )
    
        else:
            st.warning(
                "📚 Student may remain Enrolled"
            )

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

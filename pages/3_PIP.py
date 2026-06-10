import streamlit as st
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

st.title("🎓 PIP — Университетский датасет")

uploaded_file = st.file_uploader(
    "Загрузите PIP CSV",
    type="csv"
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Файл загружен")

    st.dataframe(df.head())

    # 👇 ВСЁ ДАЛЬШЕ ТОЛЬКО ВНУТРИ БЛОКА

    data = df.copy()

    for col in data.columns:
        if data[col].dtype == "object":
            data[col] = LabelEncoder().fit_transform(data[col].astype(str))

    data = data.fillna(0)

    target_col = st.selectbox("Выбери target колонку", data.columns)

    X = data.drop(columns=[target_col])
    y = data[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(),
        "Decision Tree": DecisionTreeClassifier(),
        "KNN": KNeighborsClassifier(),
        "Naive Bayes": GaussianNB()
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        results[name] = accuracy_score(y_test, preds)

    st.subheader("📊 Результаты моделей")

    st.dataframe(
        pd.DataFrame({
            "Model": results.keys(),
            "Accuracy": [f"{v:.2%}" for v in results.values()]
        })
    )

    best_model = max(results, key=results.get)

    st.success(f"🏆 Лучшая модель: {best_model}")

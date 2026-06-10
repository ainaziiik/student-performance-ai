import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

st.title("🎓 PIP Student Performance Dataset")

uploaded_file = st.file_uploader(
    "Загрузите PIP CSV файл",
    type="csv"
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Файл успешно загружен")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Количество записей",
        len(df)
    )

    col2.metric(
        "Количество признаков",
        len(df.columns)
    )

    col3.metric(
        "Средний возраст",
        round(df["Age at enrollment"].mean(), 1)
    )

    st.subheader("Предпросмотр данных")
    st.dataframe(df.head(10))

    # =====================
    # Heatmap
    # =====================

    st.subheader("📊 Корреляционная тепловая карта")

    numeric_df = df.select_dtypes(include=[np.number])

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.heatmap(
        numeric_df.corr(),
        cmap="magma",
        ax=ax
    )

    st.pyplot(fig)

    # =====================
    # Подготовка данных
    # =====================

    st.subheader("🤖 Сравнение моделей машинного обучения")

    data_clean = df.copy()

    for col in data_clean.columns:

        if data_clean[col].dtype == "object":

            le = LabelEncoder()

            data_clean[col] = le.fit_transform(
                data_clean[col].astype(str)
            )

    data_clean = data_clean.fillna(0)

    # Target

    X = data_clean.drop(
        "Target",
        axis=1
    )

    y = data_clean["Target"]

    X = X.apply(
        pd.to_numeric,
        errors="coerce"
    )

    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    models = {
        "Logistic Regression":
            LogisticRegression(max_iter=2000),

        "Random Forest":
            RandomForestClassifier(random_state=42),

        "Decision Tree":
            DecisionTreeClassifier(random_state=42),

        "KNN":
            KNeighborsClassifier(),

        "Naive Bayes":
            GaussianNB()
    }

    results = {}

    for name, model in models.items():

        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            preds
        )

        results[name] = accuracy

    best_model_name = max(
        results,
        key=results.get
    )

    best_model = models[
        best_model_name
    ]

    best_model.fit(
        X_train,
        y_train
    )

    best_preds = best_model.predict(
        X_test
    )

    results_df = pd.DataFrame({

        "Модель":
            results.keys(),

        "Точность": [
            f"{acc:.2%}"
            for acc in results.values()
        ]
    })

    st.dataframe(results_df)

    st.success(
        f"🏆 Лучшая модель: "
        f"{best_model_name} "
        f"({results[best_model_name]:.2%})"
    )

    # =====================
    # Confusion Matrix
    # =====================

    st.subheader(
        "📉 Confusion Matrix (лучшая модель)"
    )

    cm = confusion_matrix(
        y_test,
        best_preds
    )

    fig, ax = plt.subplots()

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Purples",
        ax=ax
    )

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

    st.pyplot(fig)

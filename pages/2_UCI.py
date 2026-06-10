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

st.title("🏫 UCI Student Performance Dataset")
uploaded_file = st.file_uploader(
    "Загрузите UCI CSV файл",
    type="csv"
)
if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        sep=";"
    )
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
        "Средний балл G3",
        round(df["G3"].mean(), 2)
    )
    st.subheader("Предпросмотр данных")
    st.dataframe(df.head(10))
st.subheader("📊 Корреляционная тепловая карта")

numeric_df = df.select_dtypes(include=[np.number])
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(
    numeric_df.corr(),
    cmap="magma",
    ax=ax
)
st.pyplot(fig)
st.subheader("🤖 Сравнение моделей машинного обучения")

data_clean = df.copy()
for col in data_clean.columns:
    if data_clean[col].dtype == "object":
        le = LabelEncoder()
        data_clean[col] = le.fit_transform(
            data_clean[col].astype(str)
        )
data_clean = data_clean.fillna(0)

data_clean["target"] = data_clean["G3"].apply(
    lambda x: 1 if x >= 10 else 0
)

X = data_clean.drop(
    ["G1", "G2", "G3", "target"],
    axis=1,
    errors="ignore"
)
y = data_clean["target"]

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
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Naive Bayes": GaussianNB()
}

results = {}

for name, model in models.items():
    st.write(X.dtypes)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    accuracy = accuracy_score(
        y_test,
        preds
    )
    results[name] = accuracy

results_df = pd.DataFrame({
    "Модель": results.keys(),
    "Точность": [
        f"{acc:.2%}"
        for acc in results.values()
    ]
})

st.dataframe(results_df)

best_model = max(
    results,
    key=results.get
)

st.success(
    f"🏆 Лучшая модель: {best_model} "
    f"({results[best_model]:.2%})"
)

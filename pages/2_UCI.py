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

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("UCI мектеп окуучуларынын жетишкендиктери жөнүндө маалымат топтому")
st.markdown("""
<div class="page-banner">
Машиналык үйрөнүү анализинин панели
</div>
""", unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "UCI CSV файлды жүктөңүз",
    type="csv"
)
if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        sep=";"
    )
    st.success("Файл ийгиликтүү жүктөлдү!")
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Окуучулардын саны",
        len(df)
    )
    col2.metric(
        "Белгилердин саны",
        len(df.columns)
    )
    col3.metric(
        "Орточо балл G3",
        round(df["G3"].mean(), 2)
    )
    st.subheader("Маалыматтарды алдын ала көрүү")
    st.dataframe(df.head(10))
    
    st.markdown("""
    <div class="section-title">
    Корреляциялык жылуулук картасы
    </div>
    """, unsafe_allow_html=True)
    
    numeric_df = df.select_dtypes(include=[np.number])
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(
        numeric_df.corr(),
        cmap="magma",
        ax=ax
    )
    st.pyplot(fig)
    
    st.markdown("""
    <div class="section-title">
    Моделдерди салыштыруу
    </div>
    """, unsafe_allow_html=True)
    
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
     
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        accuracy = accuracy_score(
            y_test,
            preds
        )
        results[name] = accuracy
    
    best_model_name = max(results, key=results.get)
    best_model = models[best_model_name]
    
    best_model.fit(X_train, y_train)
    best_preds = best_model.predict(X_test)
    
    results_df = pd.DataFrame({
        "Модель": results.keys(),
        "Тактыгы": [
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
    
    st.markdown(
        f"""
        ### Эң мыкты модель
    
        **{best_model}**
    
        Моделдин тактыгы: **{results[best_model]:.2%}**
    
        Бул модель UCI маалымат топтомунда 
        эң жакшы натыйжаларды көрсөттү жана эң эффективдүү 
        болжолдоо алгоритми катары тандалды.
        """
    )
    
    st.markdown("""
    <div class="section-title">
    Дал келүүлөр матрицасы
    </div>
    """, unsafe_allow_html=True)
    
    cm = confusion_matrix(y_test, best_preds)
    
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

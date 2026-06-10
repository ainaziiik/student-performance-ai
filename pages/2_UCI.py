import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

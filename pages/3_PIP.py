import streamlit as st
import pandas as pd

st.title("🎓 PIP — Университетский датасет")

uploaded_file = st.file_uploader(
    "Загрузите PIP CSV",
    type="csv"
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Файл загружен")

    st.dataframe(df.head())

st.subheader("Первые строки датасета")
st.dataframe(df.head())

st.subheader("Размер датасета")
st.write(df.shape)

st.subheader("Названия столбцов")
st.write(df.columns.tolist())

st.subheader("Типы данных")
st.write(df.dtypes)

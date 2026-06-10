import streamlit as st
import pandas as pd

st.title("🎓 PIP Dataset Analysis")

df = pd.read_csv(
    "Student performance (Polytechnic Institute of Portalegre).csv"
)

st.subheader("Первые строки датасета")
st.dataframe(df.head())

st.subheader("Размер датасета")
st.write(df.shape)

st.subheader("Названия столбцов")
st.write(df.columns.tolist())

st.subheader("Типы данных")
st.write(df.dtypes)

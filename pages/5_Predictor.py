import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.title("🔮 Student Performance Predictor")

df = pd.read_csv(
    "Student performance (Polytechnic Institute of Portalegre).csv"
)

data_clean = df.copy()

for col in data_clean.columns:
    if data_clean[col].dtype == "object":
        le = LabelEncoder()
        data_clean[col] = le.fit_transform(
            data_clean[col].astype(str)
        )

X = data_clean.drop(
    "Target",
    axis=1
)

y = data_clean["Target"]

model = RandomForestClassifier(
    random_state=42
)

model.fit(X, y)


print(df.columns.tolist())

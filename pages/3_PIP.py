import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

st.title("🎓 PIP Student Performance")

df = pd.read_csv(
    "Student performance (Polytechnic Institute of Portalegre).csv"
)

st.dataframe(df.head())

df = df.copy()

df["Target"] = df["Target"].replace({
    "Graduate": 1,
    "Dropout": 0,
    "Enrolled": 0
})

X = df.drop("Target", axis=1)
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


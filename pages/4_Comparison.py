import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("⚖️ Сравнение UCI и PIP")

comparison_df = pd.DataFrame({
    "Модель": [
        "Logistic Regression",
        "Random Forest",
        "Decision Tree",
        "KNN",
        "Naive Bayes"
    ],
    "UCI": [
        74.68,
        72.15,
        59.49,
        65.82,
        72.15
    ],
    "PIP": [
        73.22,
        76.05,
        67.68,
        60.90,
        69.94
    ]
})

st.dataframe(comparison_df)

best_uci = comparison_df.loc[
    comparison_df["UCI"].idxmax()
]

best_pip = comparison_df.loc[
    comparison_df["PIP"].idxmax()
]

st.success(
    f"🏫 Лучшая модель для UCI: "
    f"{best_uci['Модель']} "
    f"({best_uci['UCI']}%)"
)

st.success(
    f"🎓 Лучшая модель для PIP: "
    f"{best_pip['Модель']} "
    f"({best_pip['PIP']}%)"
)

fig, ax = plt.subplots(figsize=(10,5))

x = range(len(comparison_df))

ax.bar(
    [i-0.2 for i in x],
    comparison_df["UCI"],
    width=0.4,
    label="UCI"
)

ax.bar(
    [i+0.2 for i in x],
    comparison_df["PIP"],
    width=0.4,
    label="PIP"
)

ax.set_xticks(x)
ax.set_xticklabels(
    comparison_df["Модель"],
    rotation=20
)

ax.set_ylabel("Accuracy (%)")
ax.legend()

st.pyplot(fig)

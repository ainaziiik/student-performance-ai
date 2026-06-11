import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("⚖️ Сравнение UCI и PIP")

st.markdown("""
<div class="page-banner">
⚖️ Comparative Analysis of School and University Datasets
</div>
""", unsafe_allow_html=True)

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

st.markdown(f"""
<div class="winner-card">
<div class="winner-title">
🏫 Best Model for UCI
</div>

<div class="winner-model">
{best_uci['Модель']}
</div>

Accuracy: {best_uci['UCI']}%
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="winner-card">
<div class="winner-title">
🎓 Best Model for PIP
</div>

<div class="winner-model">
{best_pip['Модель']}
</div>

Accuracy: {best_pip['PIP']}%
</div>
""", unsafe_allow_html=True)
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

st.markdown(f"""
<div class="research-card">

<h3>📖 Research Conclusion</h3>

<ul>

<li>
For the school dataset (UCI), the highest accuracy was achieved by
<b>{best_uci['Модель']}</b>
with a result of
<b>{best_uci['UCI']}%</b>.
</li>

<li>
For the university dataset (PIP), the highest accuracy was achieved by
<b>{best_pip['Модель']}</b>
with a result of
<b>{best_pip['PIP']}%</b>.
</li>

<li>
The comparison demonstrates that different educational environments
require different machine learning approaches.
</li>

<li>
The developed system can be used to identify students at academic risk
and support decision-making in educational institutions.
</li>

</ul>

</div>
""", unsafe_allow_html=True)

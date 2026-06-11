import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("UCI жана PIP датасеттерди салыштыруу")

st.markdown("""
<div class="page-banner">
Мектеп жана университеттин маалымат топтомун салыштырмалуу талдоо
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
UCI үчүн мыкты модель
</div>

<div class="winner-model">
{best_uci['Модель']}
</div>

Тактыгы: {best_uci['UCI']}%
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="winner-card">
<div class="winner-title">
PI үчүн мыкты модель
</div>

<div class="winner-model">
{best_pip['Модель']}
</div>

Тактыгы: {best_pip['PIP']}%
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

ax.set_ylabel("Тактыгы (%)")
ax.legend()

st.pyplot(fig)

st.markdown(f"""
<div class="research-card">

<h3>Изилдөө корутундусу</h3>

<ul>

<li>
Мектеп маалыматтар топтому  (UCI) үчүн эң жогорку тактыкка
<b>{best_uci['Модель']}</b> 
<b>{best_uci['UCI']}%</b> натыйжасы менен ээ болду.
</li>

<li>
Университеттин маалымат топтому үчүн (PIP) үчүн эң жогорку тактыкка
<b>{best_pip['Модель']}</b>
<b>{best_pip['PIP']}%</b> натыйжасы менен ээ болду.
</li>

<p>
Салыштыруу көрсөткөндөй, ар кандай билим берүү чөйрөлөрү машинаны үйрөнүүнүн 
ар кандай ыкмаларын талап кылат. 
Иштелип чыккан система тобокелдик тобундагы студенттерди аныктоо 
жана билим берүү мекемелеринде чечим кабыл алууну жеңилдетүү үчүн колдонулушу мүмкүн.
</p>

</ul>

</div>
""", unsafe_allow_html=True)

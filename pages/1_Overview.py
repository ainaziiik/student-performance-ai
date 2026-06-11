import streamlit as st

st.set_page_config(
    page_title="Student Performance AI",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("📊 Student Performance AI System")

st.markdown(
    """
    <div class="glow-line"></div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div class="glass-card">

<h2>🧠 Искусственный интеллект для анализа успеваемости студентов</h2>

<p>
Данный проект исследует эффективность алгоритмов машинного обучения
для прогнозирования академической успеваемости учащихся школы и университета.
</p>

<br>

<h3>Возможности системы</h3>

<ul>
<li>🏫 Анализ школьного датасета UCI</li>
<li>🎓 Анализ университетского датасета PIP</li>
<li>🤖 Сравнение 5 моделей машинного обучения</li>
<li>📊 Heatmap корреляций</li>
<li>📉 Confusion Matrix</li>
<li>⚖️ Сравнение результатов UCI и PIP</li>
<li>🔮 Прогнозирование успеваемости студентов</li>
</ul>

</div>
""", unsafe_allow_html=True)

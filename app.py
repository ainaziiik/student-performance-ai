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
st.markdown("""
### Искусственный интеллект для анализа успеваемости студентов

Проект содержит:

- 🏫 Анализ школьного датасета UCI
- 🎓 Анализ университетского датасета PIP
- ⚖️ Сравнение моделей
- 🔮 Прогнозирование успеваемости
""")

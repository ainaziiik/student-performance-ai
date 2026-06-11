import streamlit as st

with open(
    "assets/style.css"
) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
    
st.set_page_config(
    page_title="Башкы бет",
    layout="wide"
)
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
st.title("ЖИ технологияларынын жардамы менен студенттердин жетишүүсүн болжолдуу аныктоо")
st.markdown("""
### Жетишкендиктерди анализдөө жана болжолдоо

Долбоор төмөнкүлөрдүкамтыйт:

- Мектептин UCI датасетине талдоо жүргүзүү,
- Университеттин PIP датасетине  талдоо жүргүзүү,
- Моделдерди салыштыруу
- Жетишүүлөрүн болжолдоо
""")

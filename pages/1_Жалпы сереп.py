import streamlit as st

st.set_page_config(
    page_title="Жетишкендиктерди анализдөө жана болжолдоо",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.markdown("""
<div class="bg-blur blur1"></div>
<div class="bg-blur blur2"></div>
<div class="bg-blur blur3"></div>
""", unsafe_allow_html=True)

st.title("Жетишкендиктерди анализдөө жана болжолдоо")

st.markdown(
    """
    <div class="glow-line"></div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div class="glass-card">

<h2>Билим алуучулардын жетишкендиктерин талдоо үчүн жасалма интеллектти колдонуу</h2>

<p>
Бул долбоор мектеп жана жогорку окуу жайларынын студенттеринин академиялык жетишкендиктерин 
болжолдоо үчүн машиналык окутуу алгоритмдердин натыйжалуулугун изилдейт.
</p>

<br>

<h3>Системанын өзгөчөлүктөрү</h3>

<ul>
<li>Мектеп датасетин UCI талдоо</li>
<li>Университет датасетин PIP талдоо</li>
<li>Машиналык үйрөнүүнүн 5 моделин салыштыруу</li>
<li>Heatmap корреляциясы</li>
<li>Дал келүүлөр матрицасы</li>
<li>UCI жана PIP натыйжаларын салыштыруу</li>
<li>Студенттердин жетишкендиктерин болжолдоо</li>
</ul>

</div>
""", unsafe_allow_html=True)

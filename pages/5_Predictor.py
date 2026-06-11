import streamlit as st

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
st.title("Окуучулардын жетишкендиктерин болжолдуу аныктоо")

st.markdown("""
<div class="page-banner">
ЖИ алдын ала айтуу системасы 
</div>
""", unsafe_allow_html=True)

dataset = st.selectbox(
    "Датасет тандаңыз",
    [
        "UCI Мектеп окуучулары",
        "PIP ЖОЖ студенттери"
    ]
)


if dataset == "PIP ЖОЖ студенттери":

    st.markdown("""
    <div class="section-title">
    ЖОЖдун студенттеринин параметрлери
    </div>
    """, unsafe_allow_html=True)

    age = st.slider(
        "Окууга кирүүдөгү курагы",
        17,
        70,
        20
    )

    admission_grade = st.slider(
        "Өтүү балы",
        0,
        200,
        120
    )

    scholarship = st.selectbox(
        "Стипендиат",
        ["Жок", "Ооба"]
    )

    debtor = st.selectbox(
        "Кредит",
        ["Жок", "Бар"]
    )

    tuition = st.selectbox(
        "Учурдагы окуу төлөмүндүк карызы",
        ["Жок", "Бар"]
    )

    if st.button("Болжолдоо!"):

        score = admission_grade

        if scholarship == "Ооба":
            score += 20

        if tuition == "Бар":
            score += 20

        if debtor == "Бар":
            score -= 40

        if score >= 130:
            st.success("✅ Студент окуусун ийгиликтүү бүтүшү ыктымал!")
        elif score >= 90:
            st.warning("Студент катталган бойдон кала алат")
        else:
            st.error("⚠️ Студент окуудан чыгаруу коркунучунда!")


elif dataset == "UCI Мектеп окуучулары":

    st.markdown("""
    <div class="section-title">
    UCI Мектеп окуучуларынын параметрлери
    </div>
    """, unsafe_allow_html=True)

    age = st.slider(
        "Жашы",
        15,
        22,
        17
    )

    studytime = st.slider(
        "Окуу убактысы (саат)",
        1,
        10,
        4
    )

    absences = st.slider(
        "Сабак калтырууларынын саны",
        0,
        100,
        5
    )

    freetime = st.slider(
        "Бош убактысы",
        1,
        5,
        3
    )

    parent_education = st.slider(
        "Ата-энесинин билими",
        0,
        4,
        2
    )

    if st.button("Болжолдоо!"):

        score = (
            studytime * 15
            + parent_education * 10
            + freetime * 5
            - absences * 2
        )

        if score >= 50:
            st.success("✅ Окуучу ийгиликтүү өтүшү мүмкүн!")
        else:
            st.error("⚠️ Окуучуга кошумча даярдык керек болушу мүмкүн!")

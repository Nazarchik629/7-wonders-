import streamlit as st

st.set_page_config(page_title="7 чудес Казахстана", layout="wide")

st.markdown("<h1 style='text-align: center; color: #003366;'>KZ Семь природных чудес Казахстана</h1>", unsafe_allow_html=True)
st.info("МЕНІҢ ОТАНЫМА- МЕНІҢ БАСТАМАМ")
st.info("Ученика Солодовникова Назара КГУ ОШ №125")
st.write("---")

wonders = {
    "Урочище Босжира":       "client/public/images/boszhira.png",
    "Чарынский каньон":      "client/public/images/charyn.png",
    "Озеро Балхаш":          "client/public/images/balkhash.png",
    "Поющий бархан":         "client/public/images/dune.png",
    "Карабилуха (г. Белуха)":"client/public/images/belukha.png",
    "Пик Хан-Тенгри":        "client/public/images/khan_tengri.png",
    "Озеро Каинды":          "client/public/images/kaindy.png",
}

choice = st.selectbox("Выберите чудо природы:", list(wonders.keys()))

st.subheader(f"📍 {choice}")
st.image(wonders[choice], caption=f"Вид на {choice}", width=800)

st.write("### Описание")
if choice == "Урочище Босжира":
    st.info("Фантастический ландшафт на плато Устюрт. Это дно древнего океана Тетис.")
elif choice == "Чарынский каньон":
    st.info("Один из красивейших каньонов мира, длиной 154 км и глубиной до 300 м.")
elif choice == "Озеро Балхаш":
    st.info("Уникальное озеро: западная часть пресноводная, восточная — солёная. Площадь 16 400 км².")
elif choice == "Поющий бархан":
    st.info("Гигантский песчаный бархан, при ветре издающий звук, похожий на органный гул.")
elif choice == "Карабилуха (г. Белуха)":
    st.info("Священная гора Алтая, высочайшая вершина Сибири и Алтайских гор.")
elif choice == "Пик Хан-Тенгри":
    st.info("Высшая точка Казахстана, «Повелитель неба». Высота 7 010 метров.")
elif choice == "Озеро Каинды":
    st.info("Горное озеро, образовавшееся после землетрясения 1911 года. Из воды торчат верхушки затопленных елей.")

st.balloons()

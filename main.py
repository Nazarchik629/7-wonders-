import streamlit as st

# 1. Настройка и Оранжевый стиль
st.set_page_config(page_title="7 чудес 🇰🇿", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #F5F5DC; }
        h1, h2, h3 { color: #FF8C00 !important; }
        .stAlert { border: 2px solid #FF8C00; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🧡 Семь Чудес Казахстана 🧡</h1>", unsafe_allow_html=True)
st.write("🌟 **Назар Солодовников, ОШ №125** 🎓")

# 2. База данных (Короткие строки, чтобы не ломались)
data = {
    "Босжира 🏔️": ["1.jpg", "Белые скалы Устюрта 👽", "15к чел/год", "Цвет меняется на солнце ☀️"],
    "Чарын 🏜️": ["2.jpg", "Долина замков 🏰", "100к чел/год", "Там растет древний ясень 🌳"],
    "Балхаш 🌊": ["3.jpg", "Пресное и соленое озеро 🧂", "200к чел/год", "Зависит от ледников 🧊"],
    "Бархан ⏳": ["4.jpg", "Песчаная гора поет 🎵", "20к чел/год", "Гул слышен далеко 📢"],
    "Белуха 🏔️": ["5.jpg", "Высшая точка Алтая ❄️", "5к чел/год", "Центр Евразии 🌍"],
    "Хан-Тенгри 💎": ["6.jpg", "Пик из розового мрамора ✨", "2к чел/год", "Светится розовым на закате 🔥"],
    "Каинды 🌲": ["7.jpg", "Лес в бирюзовой воде 🛶", "40к чел/год", "Ели не гниют в холоде 🌡️"]
}

# 3. Интерфейс
choice = st.sidebar.selectbox("Выбери чудо: ✨", list(data.keys()))
item = data[choice]

col1, col2 = st.columns([2, 1])

with col1:
    try:
        st.image(item[0], use_container_width=True)
    except:
        st.error("❌ Файл картинки не найден!")
    st.success(f"📢 Идея: Продвижение через соцсети и VR! 📱")

with col2:
    st.info(f"✨ **Что это:** {item[1]}")
    st.warning(f"📊 **Туристы:** {item[2]}")
    st.info(f"💡 **Факт:** {item[3]}")

st.balloons()

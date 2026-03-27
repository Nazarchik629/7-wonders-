import streamlit as st

# 1. Настройка и Глубокий кремовый стиль
st.set_page_config(page_title="7 чудес 🇰🇿", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #D2B48C !important; } /* Темно-кремовый фон */
        h1, h2, h3 { color: #8B4513 !important; text-align: center; } /* Коричневые заголовки */
        
        /* Стиль текста в блоках: Темно-коричневый (кофейный) */
        .stAlert div, .stAlert p {
            color: #3E2723 !important; 
            font-weight: bold;
        }
        
        .stAlert {
            background-color: #FFF8DC !important; /* Светло-кремовый внутри блоков */
            border: 2px solid #8B4513 !important;
            border-radius: 12px;
        }

        [data-testid="stHeaderActionElements"], #MainMenu, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🤎 Семь Чудес Казахстана 🤎</h1>", unsafe_allow_html=True)
st.info("Ученика Солодовникова Назар КГУ ОШ №125")

# 2. База данных (Максимально короткие строки!)
data = {
    "Урочище Бозжыра 🏔️": ["1.jpg", "Белые скалы Устюрта 👽", "15к чел/год", "Цвет меняется на солнце ☀️"],
    "Чарынский Каньон🏜️": ["2.jpg", "Долина замков 🏰", "100к чел/год", "Там растет древний ясень 🌳"],
    "Озеро Балхаш 🌊": ["3.jpg", "Пресное и соленое озеро 🧂", "200к чел/год", "Зависит от ледников 🧊"],
    "Поющий Бархан 🎶": ["4.jpg", "Песчаная гора поет 🎵", "20к чел/год", "Гул слышен далеко 📢"],
    "Гора Белуха 🏔️": ["5.jpg", "Высшая точка Алтая ❄️", "5к чел/год", "Центр Евразии 🌍"],
    " Пик Хан-Тенгри 🗻": ["6.jpg", "Пик из розового мрамора ✨", "2к чел/год", "Светится розовым 🔥"],
    "Озеро Каинды 🌲": ["7.jpg", "Лес в бирюзовой воде 🛶", "40к чел/год", "Ели не гниют в холоде 🌡️"]
}

# 3. Интерфейс
choice = st.sidebar.selectbox("Выбери чудо: ✨", list(data.keys()))
item = data[choice]

col1, col2 = st.columns([2, 1.2])

with col1:
    try:
        st.image(item[0], use_container_width=True)
    except:
        st.error("❌ Картинка не найдена!")
    st.success("📢 Идея: VR-туры и реклама в TikTok! 📱")

with col2:
    st.info(f"✨ Что это: {item[1]}")
    st.info(f"📊 Туристы: {item[2]}")
    st.info(f"💡 Факт: {item[3]}")

st.balloons()

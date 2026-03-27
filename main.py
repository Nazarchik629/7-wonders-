import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="7 чудес Казахстана 🇰🇿", layout="wide")

# 2. МЕГА-СТИЛЬ: Бежевый фон и Оранжевые элементы
st.markdown("""
    <style>
        /* Главный фон всего приложения (Бежевый) */
        .stApp {
            background-color: #F5F5DC;
        }

        /* Стиль для заголовков (Оранжевый) */
        h1, h2, h3 {
            color: #FF8C00 !important;
            font-family: 'Trebuchet MS', sans-serif;
        }

        /* Оранжевые блоки st.info */
        .stAlert {
            background-color: #FFFAF0;
            border: 2px solid #FF8C00;
            border-radius: 15px;
        }

        /* Стиль выпадающего списка */
        .stSelectbox div[data-baseweb="select"] {
            border: 2px solid #FF8C00;
            border-radius: 10px;
        }

        /* Скрытие лишних кнопок Streamlit */
        [data-testid="stHeaderActionElements"] { display: none; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Мобильное меню */
        @media (max-width: 768px) {
            header[data-testid="stHeader"] { visibility: visible !important; background-color: rgba(0,0,0,0); }
        }
        @media (min-width: 769px) {
            header[data-testid="stHeader"] { visibility: hidden; }
        }
    </style>
""", unsafe_allow_html=True)

# Шапка сайта со смайликами
st.markdown("<h1 style='text-align: center;'>🧡 Семь Чудес Казахстана 🧡</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>✨ Менің Отаныма - менің бастамам ✨</h3>", unsafe_allow_html=True)
st.info("🌟 Ученик: Солодовников Назар, КГУ ОШ №125 🎓🏫")
st.write("---")

# 3. База данных со смайликами 📝
data = {
    "Урочище Босжира 🏔️": {
        "img": "1.jpg",
        "info": "⚪ Белоснежные скалы и космические пейзажи плато Устюрт! 👽",
        "stats": "📈 Около 15,000 туристов в год 🎒",
        "fact": "🎨 Скалы меняют цвет: от белого до розового под солнцем! ☀️",
        "ads": "📱 VR-туры и QR-коды для мгновенной истории! 🤖"
    },
    "Чарынский каньон 🏜️": {
        "img": "2.jpg",
        "info": "🧱 Древний каньон, который называют 'Долиной замков'! 🏰",
        "stats": "📈 Более 100,000 посетителей в год 📸",
        "fact": "🌳 Здесь растет уникальный ясень, выживший в ледниковый период! ❄️",
        "ads": "🎧 Аудиогиды на 3-х языках и крутые эко-фестивали! 🎸"
    },
    "Озеро Балхаш 🌊": {
        "img": "3.jpg",
        "info": "🌓 Уникальное озеро: одна сторона пресная, другая — соленая! 🧂",
        "stats": "📈 200,000 отдыхающих за сезон 🏖️",
        "fact": "🧊

import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="7 чудес Казахстана 🇰🇿", layout="wide")

# 2. МЕГА-СТИЛЬ: Бежевый фон и Оранжевые элементы
st.markdown("""
    <style>
        .stApp { background-color: #F5F5DC; }
        h1, h2, h3 { color: #FF8C00 !important; font-family: 'Arial', sans-serif; }
        .stAlert { background-color: #FFFAF0; border: 2px solid #FF8C00; border-radius: 15px; }
        .stSelectbox div[data-baseweb="select"] { border: 2px solid #FF8C00; border-radius: 10px; }
        [data-testid="stHeaderActionElements"] { display: none; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        @media (max-width: 768px) {
            header[data-testid="stHeader"] { visibility: visible !important; background-color: rgba(0,0,0,0); }
        }
        @media (min-width: 769px) {
            header[data-testid="stHeader"] { visibility: hidden; }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🧡 Семь Чудес Казахстана 🧡</h1>", unsafe_allow_html=True)
st.info("🌟 Ученик: Солодовников Назар, КГУ ОШ №125 🎓🏫")

# 3. База данных (Всё проверено на кавычки!)
data = {
    "Урочище Босжира 🏔️": {
        "img": "1.jpg",
        "info": "⚪ Белоснежные скалы плато Устюрт! 👽",
        "stats": "📈 15,000 туристов в год 🎒",
        "fact": "🎨 Скалы меняют цвет на солнце! ☀️",
        "ads": "📱 VR-туры и QR-коды! 🤖"
    },
    "Чарынский каньон 🏜️": {
        "img": "2.jpg",
        "info": "🧱 Древний каньон 'Долина замков'! 🏰",
        "stats": "📈 100,000 посетителей в год 📸",
        "fact": "🌳 Здесь растет реликтовый ясень! ❄️",
        "ads": "🎧 Аудиогиды и эко-фестивали! 🎸"
    },
    "Озеро Балхаш 🌊": {
        "img": "3.jpg",
        "info": "🌓 Половина пресная, половина соленая! 🧂",
        "stats": "📈 200,000 отдыхающих за сезон 🏖️",
        "fact": "🧊 Зависит от ледников Тянь-Шаня! 🏔️",
        "ads": "🤳 Реклама у блогеров и эко-туры! 🛶"
    },
    "Поющий Бархан ⏳": {
        "img": "4.jpg",
        "info": "🎵 Песчаная гора, которая поет! 🎶",
        "stats": "📈 20,000 человек в год 🐪",
        "fact": "📢 Его гул слышен за километры! ✈

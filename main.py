import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="7 чудес Казахстана", layout="wide")

# CSS: скрываем лишнее, оставляем меню для мобилок
st.markdown("""
    <style>
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

# Заголовки
st.markdown("<h1 style='text-align: center;'>Семь Чудес Казахстана 💫</h1>", unsafe_allow_html=True)
st.info("Ученик: Солодовников Назар, КГУ ОШ №125 🧑‍🎓")

# 2. База данных (тексты сокращены для надежности)
w_data = {
    "Урочище Босжира": {
        "img": "1.jpg",
        "desc": "Белоснежные скалы плато Устюрт.",
        "stats": "15,000 чел/год",
        "res": "Исследования 1990-х годов.",
        "fact": "Скалы меняют цвет на закате.",
        "ads": "VR-туры и QR-коды на месте."
    },
    "Чарынский каньон": {
        "img": "2.jpg",
        "desc": "Древний каньон, Долина замков.",
        "stats": "100,000 чел/год",
        "res": "Изучен в XIX веке (Мушкетов).",
        "fact": "Есть роща реликтового ясеня.",
        "ads": "Эко-фестивали и аудиогиды."
    },
    "Озеро Балхаш": {
        "img": "3.jpg",
        "desc": "Половина озера пресная, половина соленая.",
        "stats": "200,000 чел/год",
        "res": "Изучается с 1920-х годов.",
        "fact": "Зависит от ледников Тянь-Шаня.",
        "ads": "Реклама у блогеров и эко-туры."
    },
    "Поющий Бархан": {
        "img": "4.jpg",
        "desc": "Песчаная гора, которая издает гул.",
        "stats": "20,000 чел/год",
        "res": "Описан Чоканом Валихановым.",
        "fact": "Звук слышен за километры.",
        "ads": "TikTok-ролики и медитации."
    },
    "Карабилуха (г. Белуха)": {
        "img": "5.jpg",
        "desc": "Высшая точка Алтая в ледниках.",
        "stats": "5,000 чел/год",
        "res":

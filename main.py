import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="7 чудес Казахстана", layout="wide")

# Умный CSS для скрытия кнопок и работы меню на мобилках
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
        .block-container { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

# Заголовки
st.markdown("<h1 style='text-align: center;'>Семь Чудес Казахстана 💫</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Менің Отаныма менің бастамам</h2>", unsafe_allow_html=True)
st.info("Ученика Солодовникова Назар КГУ ОШ №125 🧑‍🎓")
st.write("---")

# 2. Полная база данных (Все кавычки проверены!)
wonders_data = {
    "Урочище Босжира": {
        "img": "1.jpg",
        "desc": "Босжира — ослепительно белое безмолвие плато Устюрт.",
        "stats": "Около 15,000 туристов в год.",
        "research": "Исследования начаты в 1990-х годах геологами Мангистау.",
        "facts": "Скалы меняют цвет от белого до розового в зависимости от солнца.",
        "promo": "Использование VR-туров и QR-кодов на смотровых площадках."
    },
    "Чарынский каньон": {
        "img": "2.jpg",
        "desc": "Каменная летопись планеты, высеченная ветрами и водой.",
        "stats": "Более 100,000 посетителей в год.",
        "research": "Первые описания появились в конце XIX века (И.В. Мушкетов).",
        "facts": "Здесь растет реликтовый ясень, переживший ледниковый период.",
        "promo": "Аудиогиды на трех языках и эко-фестивали."
    },
    "Озеро Балхаш": {
        "img": "3.jpg",
        "desc": "Уникальное озеро: половина пресная, половина соленая.",
        "stats": "Более 200,000 отдыхающих в сезон.",
        "research": "Масштабные исследования начались в 1920-х годах.",
        "facts": "Уровень воды зависит от состояния ледников Тянь-Шаня.",
        "promo": "Развитие эко-туризма и реклама через тревел-блогеров."
    },
    "Поющий Бархан": {
        "img": "4.jpg",
        "desc": "Песчаная гора, издающая глубокий гул в сухую погоду.",
        "stats": "Около 20,000 человек в год.",
        "research": "Описан в XIX веке, включая труды Чокана Валиханова.",
        "facts": "Звук бархана напоминает рев само

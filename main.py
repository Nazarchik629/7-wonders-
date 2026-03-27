import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="7 чудес Казахстана", layout="wide")

# Умный CSS: скрывает лишние кнопки, но оставляет навигацию на мобильных
st.markdown("""
    <style>
        /* Скрываем кнопки Share, Deploy и лишние иконки */
        [data-testid="stHeaderActionElements"] { display: none; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* На мобильных устройствах показываем кнопку меню */
        @media (max-width: 768px) {
            header[data-testid="stHeader"] {
                visibility: visible !important;
                background-color: rgba(0,0,0,0);
            }
        }
        /* На ПК скрываем хедер полностью */
        @media (min-width: 769px) {
            header[data-testid="stHeader"] {
                visibility: hidden;
            }
        }
        .block-container { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

# Заголовки
st.markdown("<h1 style='text-align: center;'>Семь Чудес Казахстана 💫</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Менің Отаныма менің бастамам</h2>", unsafe_allow_html=True)
st.info("Ученика Солодовникова Назар КГУ ОШ №125 🧑‍🎓")
st.write("---")

# 2. Расширенная база данных
wonders_data = {
    "Урочище Босжира": {
        "img": "1.jpg",
        "desc": "Босжира — это ослепительно белое безмолвие плато Устюрт. Когда-то здесь бушевал океан Тетис.",
        "stats": "Около 15,000 туристов в год.",
        "research": "Активные исследования начаты в 1990-х годах геологами Мангистау.",
        "facts": "Скалы Босжиры меняют цвет в зависимости от освещения — от белого до розового.",
        "promo": "Создание VR-туров и установка QR-кодов с историей места на смотровых площадках."
    },
    "Чарынский каньон": {
        "img": "2.jpg",
        "desc": "Каменная летопись планеты, высеченная ветрами. Его «Долина замков» поражает формами скал.",
        "stats": "Более 100,000 посетителей в год.",
        "research": "Первые научные описания появились в конце XIX века

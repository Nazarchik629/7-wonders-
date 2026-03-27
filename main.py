import streamlit as st

# 1. Настройка страницы
st.set_page_config(
    page_title="7 Чудес Казахстана 💫", 
    layout="wide",
    initial_sidebar_state="collapsed" # Скрываем боковую панель совсем
)

# Умный CSS: убираем лишнее, но оставляем кнопку навигации (на всякий случай)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
        }
        /* Полностью убираем боковую панель из интерфейса */
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Заголовки
st.markdown("<h1 style='text-align: center;'>KZ Семь Чудес Казахстана</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Менің Отаныма - менің бастамам</h2>", unsafe_allow_html=True)
st.info("Ученика Солодовникова Назара КГУ ОШ №125 🧑‍🎓")

# Данные
wonders = {
    "Урочище Босжира": "1.jpg",
    "Чарынский каньон": "2.jpg",
    "Озеро Балхаш": "3.jpg",
    "Поющий Бархан": "4.jpg",
    "Карабилуха (г. Белуха)": "5.jpg",

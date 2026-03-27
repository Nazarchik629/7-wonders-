import streamlit as st

# 1. Настройка страницы
st.set_page_config(
    page_title="7 Чудес Казахстана 💫", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# Умный CSS: скрываем лишнее, но оставляем кнопку навигации
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
        }
        /* Кнопка открытия меню для мобилок */
        button[data-testid="baseButton-headerNoPadding"] {
            background-color: #ff4b4b !important;
            border-radius: 8px !important;
            color: white !important;
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
    "Пик Хан-Тенгри": "6.jpg",
    "Озеро Каинды": "7.jpg"
}

descriptions = {
    "Урочище Босжира": "Босжира — это ослепительно белое безмолвие плато Устюрт, где время словно замерло миллионы лет назад.",
    "Чарынский каньон": "Чарынский каньон — это каменная летопись планеты, высеченная ветрами и водой. Его «Долина замков» поражает воображение.",
    "Озеро Балхаш": "Балхаш — это природный феномен. Это единственное в мире озеро, западная часть которого пресная, а восточная — соленая.",
    "Поющий Бархан": "Поющий бархан — это легенда пустыни Алтын-Эмель. В сухую погоду эта гигантская песчаная гора издает глубокий гул.",
    "Карабилуха (г. Белуха)": "Гора Белуха — это корона Алтая, священная двуглавая вершина, вечно укрытая сияющими ледниками.",
    "Пик Хан-Тенгри": "Хан-Тенгри — «Повелитель неба», один из самых красивых семитысячников планеты. Его пирамида на закате вспыхивает розовым светом.",
    "Озеро Каинды": "Каинды — мистическая сказка в лесах Тянь-Шаня. Из бирюзовой глади озера поднимаются сухие стволы вековых елей."
}

# 2. Навигация
# Основной выбор в центре (для мобильных)
choice = st.selectbox("Выберите чудо природы:", list(wonders.keys()))

# Дубликат в боковую панель (исправлено!)
st.sidebar.title("Навигация")
st.sidebar.radio(
    "Перейти к:", 
    list(wonders.keys()), 
    index=list(wonders.keys()).index(choice)
)

st.write("---")

# 3. Контент
st.write(f"### 📍 {choice}")
col_img, col_txt = st.columns([2, 1])

with col_img:
    try:
        st.image(wonders[choice], use_container_width=True)
    except:
        st.error(f"Файл {wonders[choice]} не найден.")

with col_txt:
    st.markdown("#### ✨ Описание")
    st.success(descriptions[choice])

st.balloons()

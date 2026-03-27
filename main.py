import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="7 чудес Казахстана 🇰🇿", layout="wide")

# 2. Оранжево-бежевый стиль
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

# 3. База данных (тексты без лишних переносов, чтобы не было ошибок)
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
        "fact": "📢 Его гул слышен за километры! ✈️",
        "ads": "🎬 Трендовые TikTok-челленджи! 🧘"
    },
    "Карабилуха (г. Белуха) 🏔️": {
        "img": "5.jpg",
        "info": "👑 Высшая точка Алтая в ледниках! ❄️",
        "stats": "📈 5,000 человек в год 🧗",
        "fact": "🌍 Центр материка Евразия! 🧭",
        "ads": "🖼️ Фотовыставки и кино! 🎥"
    },
    "Пик Хан-Тенгри 🏔️💖": {
        "img": "6.jpg",
        "info": "💎 Повелитель неба из розового мрамора! ✨",
        "stats": "📈 2,000 профи-альпинистов 🥇",
        "fact": "🌅 На закате горит розовым цветом! 🔥",
        "ads": "📡 Онлайн-трансляции экспедиций! 💻"
    },
    "Озеро Каинды 🌲💧": {
        "img": "7.jpg",
        "info": "🛶 Затонувший лес в бирюзовой воде! 🧚",
        "stats": "📈 40,000 ценителей в год 🌲",
        "fact": "🌡️ Ели не гниют в ледяной воде! ❄️",
        "ads": "📷 Подводные фото-выставки! 🤿"
    }
}

# 4. Навигация и вывод
choice = st.sidebar.selectbox("Куда отправимся? ✨", list(data.keys()))

st.markdown(f"## 📍 Место: {choice}")

c1, c2 = st.columns([2, 1.2])

with c1:
    try:
        st.image(data[choice]["img"], use_container_width=True)
    except:
        st.error("⚠️ Картинка не найдена! Проверь файлы 1.jpg, 2.jpg

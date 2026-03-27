import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="7 чудес Казахстана 🇰🇿", layout="wide")

# 2. НОВЫЙ "КРЕМОВЫЙ" СТИЛЬ: Насыщенный фон и читабельный текст
st.markdown("""
    <style>
        /* Главный фон всего приложения (Насыщенный темный крем/беж) */
        .stApp {
            background-color: #E6D9C3 !important; /* Более темный, насыщенный кремовый фон */
        }

        /* Стиль для заголовков (Темно-оранжевый, глубокий) */
        h1, h2, h3, h4 {
            color: #C16A00 !important;
            font-family: 'Trebuchet MS', sans-serif;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }

        /* СТИЛИЗАЦИЯ ТЕКСТА В БЛОКАХ INFO И SUCCESS */
        /* Принудительно ставим мягкий, глубокий темно-коричневый цвет текста в alert блоках */
        .stAlert div, .stAlert p {
            color: #4B3621 !important; /* Мягкий темно-коричневый цвет 'кофе/шоколад' */
            font-weight: 500; /* Немного жирнее для лучшей читаемости */
        }

        /* Сами блоки st.info: Светлые внутри, с оранжевой рамкой */
        .stAlert {
            background-color: #FFFDF5 !important; /* Очень светлый, почти белый фон внутри блока */
            border: 2px solid #FF8C00 !important; /* Оранжевая рамка сохраняется */
            border-radius: 15px !important;
        }

        /* Оранжевый текст в выпадающем списке и других элементах по умолчанию */
        .stSelectbox div[data-baseweb="select"] {
            border: 2px solid #FF8C00 !important;
            border-radius: 10px !important;
        }
        
        /* Скрытие лишних кнопок Streamlit */
        [data-testid="stHeaderActionElements"] { display: none; }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Убираем хедер на ПК полностью */
        @media (min-width: 769px) {
            header[data-testid="stHeader"] { visibility: hidden; }
        }
        
        /* Отступ сверху */
        .block-container {
            padding-top: 1.5rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Шапка сайта
st.markdown("<h1 style='text-align: center;'>💛 Семь Чудес Казахстана 💛</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>✨ Менің Отаныма - менің бастамам ✨</h3>", unsafe_allow_html=True)
# Текст в info блоках теперь будет темно-коричневым
st.info("🌟 Ученик: Солодовников Назар, КГУ ОШ №125 🎓🏫")
st.write("---")

# 3. База данных со смайликами (Короткая версия для надежности)
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
        "stats": "📈 10

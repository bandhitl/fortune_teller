# streamlit_app.py
# This file creates a production-ready web application with a new UI
# to display an "Astrology Board" instead of an AI image.

import streamlit as st
import datetime
import os
from fortune import get_thai_fortune_details, get_chinese_fortune_details, generate_ai_fortune

# --- Page Configuration ---
st.set_page_config(
    page_title="AI โหราศาสตร์ไทย-จีน",
    page_icon="📜",
    layout="wide"
)

# --- Function to Display the Astrology Board ---
def display_astrology_board(day_name, thai_color, thai_animal, english_animal, birth_time):
    """Creates a visually appealing summary board of the user's astrological data."""
    zodiac_emojis = {
        "Rat": "🐭", "Ox": "🐮", "Tiger": "🐯", "Rabbit": "🐰", "Dragon": "🐲", 
        "Snake": "🐍", "Horse": "🐴", "Goat": "🐐", "Monkey": "🐵", 
        "Rooster": "🐔", "Dog": "🐶", "Pig": "🐷"
    }
    animal_emoji = zodiac_emojis.get(english_animal, "✨")

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap');
    .board {{
        background-color: #fdf6e3; /* A warm, parchment-like color */
        border: 3px solid #b58900; /* A golden-brown border */
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        font-family: 'Sarabun', sans-serif;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }}
    .board h3 {{
        color: #654f00;
        margin-bottom: 20px;
        border-bottom: 2px solid #b58900;
        padding-bottom: 10px;
    }}
    .info-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        align-items: center;
    }}
    .info-item {{
        background-color: #fffbf0;
        padding: 15px;
        border-radius: 10px;
    }}
    .info-item p.label {{
        font-size: 1.1em;
        margin-bottom: 5px;
        color: #837031;
    }}
    .info-item p.value {{
        font-size: 1.6em;
        font-weight: bold;
        color: #584900;
        margin: 0;
    }}
    .emoji {{
        font-size: 6em;
        line-height: 1;
    }}
    .color-circle {{
        width: 50px;
        height: 50px;
        background-color: {thai_color.lower()};
        border-radius: 50%;
        margin: auto;
        border: 3px solid #fff;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }}
    </style>
    <div class="board">
        <h3>กระดานชันษาจร</h3>
        <div class="info-grid">
            <div class="info-item">
                <p class="label">ดาวพระเคราะห์ประจำวันเกิด</p>
                <p class="value">วัน{day_name}</p>
            </div>
            <div class="info-item">
                <p class="label">ปีนักษัตร</p>
                <p class="value">{thai_animal}</p>
            </div>
            <div class="info-item">
                <p class="label">เวลาตกฟาก</p>
                <p class="value">{birth_time.strftime('%H:%M')} น.</p>
            </div>
             <div class="info-item">
                <p class="label">สีมงคล</p>
                <div class="color-circle"></div>
            </div>
        </div>
        <p class="emoji">{animal_emoji}</p>
    </div>
    """, unsafe_allow_html=True)


# --- Securely Get API Key ---
api_key = os.environ.get("OPENAI_API_KEY")

# --- Application UI ---
st.title("📜 AI โหราจารย์")
st.markdown("ไขความลับแห่งดวงดาว ผูกดวงชะตาตามหลักโหราศาสตร์ไทย-จีนโบราณ เพื่อค้นหาคำตอบและแนวทางแห่งชีวิต")

# --- Sidebar for Inputs ---
st.sidebar.header("ข้อมูลสำหรับผูกดวง")

default_date = datetime.date.today() - datetime.timedelta(days=365*25)
birth_date = st.sidebar.date_input("วัน/เดือน/ปีเกิด:", default_date, min_value=datetime.date(1920, 1, 1), max_value=datetime.date.today())
birth_time = st.sidebar.time_input("เวลาเกิด (ถ้าทราบ):", datetime.time(12, 00))

if st.sidebar.button("📜 เปิดดวงชะตา"):
    if not api_key:
        st.error("เกิดข้อผิดพลาด: ไม่พบ OpenAI API key บนเซิร์ฟเวอร์")
    elif not birth_date:
        st.error("กรุณากรอกวันเกิด")
    else:
        st.balloons()
        with st.spinner("กำลังผูกดวงและอ่านคำพยากรณ์..."):
            day_name, thai_color = get_thai_fortune_details(birth_date)
            thai_animal, english_animal = get_chinese_fortune_details(birth_date.year)
            
            # Display the new Astrology Board UI
            display_astrology_board(day_name, thai_color, thai_animal, english_animal, birth_time)
            
            # Generate and display the text fortune
            text_fortune = generate_ai_fortune(api_key, day_name, thai_color, thai_animal, birth_time)
            
            st.subheader("คำพยากรณ์ดวงชะตา")
            st.markdown("---")
            
            if "Error:" in text_fortune:
                st.error(text_fortune)
            else:
                st.markdown(text_fortune)


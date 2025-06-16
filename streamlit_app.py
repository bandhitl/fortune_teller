# streamlit_app.py
# This file creates a production-ready web application that securely uses
# an API key from the server's environment variables (e.g., on Render).

import streamlit as st
import datetime
import os # Import the 'os' module to access environment variables
from fortune import get_thai_fortune_details, get_chinese_fortune_details, generate_ai_fortune_and_image

# --- Page Configuration ---
st.set_page_config(
    page_title="AI โหราศาสตร์ไทย-จีน",
    page_icon="✨",
    layout="wide"
)

# --- Securely Get API Key ---
api_key = os.environ.get("OPENAI_API_KEY")

# --- Application UI ---
st.title("✨ AI โหราศาสตร์ไทย-จีน")
st.markdown("ปลดล็อกความลับแห่งโชคชะตาของคุณ ด้วยการผสมผสานศาสตร์โบราณเข้ากับ AI สมัยใหม่ เพียงกรอกวันและเวลาเกิดของคุณเพื่อรับคำทำนายเฉพาะบุคคล")

# --- Sidebar for Inputs ---
st.sidebar.header("ข้อมูลของคุณ")

# Date of Birth Input
default_date = datetime.date.today() - datetime.timedelta(days=365*25)
birth_date = st.sidebar.date_input(
    "กรอกวันเกิดของคุณ:",
    default_date,
    min_value=datetime.date(1920, 1, 1),
    max_value=datetime.date.today()
)

# Time of Birth Input
birth_time = st.sidebar.time_input(
    "กรอกเวลาเกิด (ถ้าทราบ):",
    datetime.time(12, 00)
)

# --- Fortune Button and Logic ---
if st.sidebar.button("🔮 เปิดคำทำนาย"):
    if not api_key:
        st.error("เกิดข้อผิดพลาดในการตั้งค่า: ไม่พบ OpenAI API key บนเซิร์ฟเวอร์ ผู้ดูแลระบบต้องทำการตั้งค่า OPENAI_API_KEY ก่อน")
    elif not birth_date:
        st.error("กรุณากรอกวันเกิดของคุณ")
    else:
        st.balloons()
        with st.spinner("กำลังปรึกษาเทพพยากรณ์ AI... อาจใช้เวลาสักครู่ในการสร้างภาพและคำทำนาย"):
            # 1. Get the basic astrological details
            day_name, thai_color = get_thai_fortune_details(birth_date)
            thai_animal, english_animal = get_chinese_fortune_details(birth_date.year)
            
            # 2. Generate the AI fortune text and image URL
            text_fortune, image_url = generate_ai_fortune_and_image(api_key, day_name, thai_color, thai_animal, english_animal, birth_time)
            
            # 3. Display the results
            st.subheader("📜 คำทำนายดวงชะตาเฉพาะบุคคลของคุณ")
            
            if image_url:
                st.image(image_url, caption="ภาพอินโฟกราฟิกดวงชะตาของคุณ", use_column_width=True)
            
            st.info(f"คำทำนายนี้อ้างอิงจากการเกิด **วัน{day_name}** เวลา **{birth_time.strftime('%H:%M')} น.** และปีนักษัตร **{thai_animal}**")
            st.markdown("---")
            
            if text_fortune:
                st.markdown(text_fortune)
            else:
                st.error("ไม่สามารถสร้างคำทำนายได้ในขณะนี้")


st.markdown("---")
st.markdown("### เกี่ยวกับแอปพลิเคชันนี้")
st.markdown("แอปพลิเคชันนี้ผสมผสานหลักโหราศาสตร์ไทยและจีนเข้ากับพลังของปัญญาประดิษฐ์ (AI) เพื่อสร้างคำทำนายที่ลึกซึ้งและเป็นเอกลักษณ์สำหรับคุณโดยเฉพาะ")

# streamlit_app.py
# Simple working version

import streamlit as st
import datetime
import os

# Page config
st.set_page_config(
    page_title="AI โหราศาสตร์ไทย-จีน",
    page_icon="🔮",
    layout="wide"
)

# Simple CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
}
.main {
    background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
}
.stApp {
    background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="
    text-align: center;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    padding: 25px 15px;
    margin-bottom: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
">
    <h1 style="color: white; font-size: 3em; margin-bottom: 10px;">🔮 AI โหราจารย์ 🔮</h1>
    <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.2em;">
        ✨ ไขความลับแห่งดวงดาว ผูกดวงชะตาไทย-จีนโบราณ ✨
    </p>
</div>
""", unsafe_allow_html=True)

# Input section
st.markdown("### 📋 ข้อมูลสำหรับผูกดวง")

col1, col2 = st.columns(2)

with col1:
    birth_date = st.date_input(
        "📅 วัน/เดือน/ปีเกิด:", 
        datetime.date(1980, 7, 8),
        min_value=datetime.date(1950, 1, 1), 
        max_value=datetime.date.today()
    )

with col2:
    birth_time = st.time_input(
        "🕐 เวลาเกิด:", 
        datetime.time(7, 30)
    )

# Button
if st.button("🔮 เปิดดวงชะตา", use_container_width=True, type="primary"):
    st.success(f"วันเกิด: {birth_date}, เวลา: {birth_time}")
    st.write("ระบบกำลังทำงาน...")

# Test display
st.write("หากคุณเห็นข้อความนี้ แสดงว่าระบบทำงานได้")

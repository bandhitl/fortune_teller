# --- Enhanced Loading Component ---
def show_mystical_loading():
    """Display a beautiful full-screen loading animation with steps."""
    return st.markdown("""
    <div class="mystical-loading-overlay">
        <div class="mystical-loading-content">
            <div class="loading-title">
                🔮 กำลังเปิดดวงชะตา 🔮
            </div>
            <div class="loading-subtitle">
                กรุณารอคำทำนายจากเทพ AI สักครู่...<br>
                ขณะนี้กำลังวิเคราะห์ดวงดาวของคุณ
            </div>
            
            <div class="mystical-spinner-container">
                <div class="mystical-spinner"></div>
            </div>
            
            <div class="loading-progress-bar">
                <div class="loading-progress-fill"></div>
            </div>
            
            <div class="loading-steps">
                <div class="loading-step active">✨ เริ่มต้นการผูกดวงชะตาของคุณ</div>
                <div class="loading-step">🔍 วิเคราะห์ข้อมูลวันเวลาเกิด</div>
                <div class="loading-step">🤖 ปรึกษาเทพ AI ผู้รอบรู้</div>
                <div class="loading-step">📝 เขียนคำพยากรณ์สำหรับคุณ</div>
            </div>
            
            <div style="margin-top: 20px; font-size: 0.9em; color: rgba(255,255,255,0.7);">
                💫 กระบวนการนี้อาจใช้เวลา 30-60 วินาที<br>
                ขึ้นอยู่กับความซับซ้อนของดวงชะตา
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)# streamlit_app.py
# Mobile-optimized Enhanced UI version with responsive design

import streamlit as st
import datetime
import os
from fortune import get_thai_fortune_details, get_chinese_fortune_details, generate_ai_fortune

# --- Page Configuration ---
st.set_page_config(
    page_title="AI โหราศาสตร์ไทย-จีน",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Enhanced Mobile-Responsive CSS ---
def load_mobile_responsive_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700&family=Kanit:wght@300;400;600;700&display=swap');
    
    /* Global Reset and Mobile Optimization */
    * {
        box-sizing: border-box;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 10px;
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide sidebar toggle on mobile for cleaner look */
    @media (max-width: 768px) {
        .css-1dp5vir {
            background: transparent;
        }
        .main {
            padding: 5px;
        }
    }
    
    /* Enhanced Header - Mobile Responsive */
    .main-header {
        text-align: center;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 25px 15px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        color: #ffffff;
        font-family: 'Kanit', sans-serif;
        font-size: clamp(1.8em, 5vw, 3.5em);
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        line-height: 1.2;
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-family: 'Sarabun', sans-serif;
        font-size: clamp(0.9em, 3vw, 1.2em);
        line-height: 1.5;
        margin: 0;
    }
    
    /* Mobile-First Board Design */
    .board {
        background: linear-gradient(145deg, #fdf6e3, #f7e98e);
        border: none;
        border-radius: 20px;
        padding: 20px 15px;
        text-align: center;
        font-family: 'Sarabun', sans-serif;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.6);
        margin: 15px 0;
        position: relative;
        overflow: hidden;
        width: 100%;
    }
    
    .board::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #d4af37, #ffd700, #d4af37);
    }
    
    .board h3 {
        color: #8b4513;
        margin-bottom: 20px;
        font-family: 'Kanit', sans-serif;
        font-size: clamp(1.3em, 4vw, 2.2em);
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        line-height: 1.2;
    }
    
    /* Mobile-Optimized Grid System */
    .mobile-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 15px;
        width: 100%;
    }
    
    @media (min-width: 768px) {
        .mobile-grid {
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
    }
    
    @media (min-width: 1024px) {
        .mobile-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 25px;
        }
    }
    
    /* Info Items - Touch Friendly */
    .info-item {
        background: rgba(255, 255, 255, 0.8);
        padding: 18px 12px;
        border-radius: 15px;
        transition: all 0.3s ease;
        border: 1px solid rgba(212, 175, 55, 0.3);
        min-height: 100px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        cursor: pointer;
    }
    
    .info-item:hover, .info-item:active {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        background: rgba(255, 255, 255, 0.95);
    }
    
    .info-item .label {
        font-size: clamp(0.8em, 2.5vw, 1em);
        margin-bottom: 8px;
        color: #8b4513;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .info-item .value {
        font-size: clamp(1.1em, 3.5vw, 1.4em);
        font-weight: 700;
        color: #654321;
        margin: 0;
        font-family: 'Kanit', sans-serif;
        line-height: 1.2;
    }
    
    /* Animal Display - Mobile Optimized */
    .animal-display {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        border-radius: 50%;
        width: clamp(80px, 20vw, 120px);
        height: clamp(80px, 20vw, 120px);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: gentle-pulse 3s ease-in-out infinite;
    }
    
    @keyframes gentle-pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .animal-emoji {
        font-size: clamp(2.5em, 8vw, 4em);
        line-height: 1;
    }
    
    /* Color Circle - Touch Friendly */
    .color-circle {
        width: clamp(40px, 12vw, 60px);
        height: clamp(40px, 12vw, 60px);
        border-radius: 50%;
        margin: 10px auto;
        border: 3px solid #fff;
        box-shadow: 
            0 5px 15px rgba(0,0,0,0.3),
            inset 0 2px 5px rgba(255,255,255,0.5);
        transition: transform 0.3s ease;
    }
    
    .color-circle:hover, .color-circle:active {
        transform: scale(1.1);
    }
    
    /* BaZi Pillars - Mobile Stack */
    .bazi-pillars {
        margin: 20px 0;
    }
    
    .pillar-row {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 10px;
    }
    
    @media (max-width: 480px) {
        .pillar-row {
            grid-template-columns: 1fr;
            gap: 8px;
        }
    }
    
    .pillar-item {
        background: rgba(139, 69, 19, 0.1);
        border: 2px solid #8b4513;
        border-radius: 12px;
        padding: 12px 8px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .pillar-item:hover, .pillar-item:active {
        transform: scale(1.02);
        background: rgba(139, 69, 19, 0.2);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .pillar-label {
        font-size: clamp(0.7em, 2vw, 0.8em);
        color: #8b4513;
        margin: 0 0 3px 0;
        font-weight: 600;
    }
    
    .pillar-value {
        font-size: clamp(1.1em, 3vw, 1.4em);
        font-weight: 700;
        color: #654321;
        margin: 0 0 2px 0;
        font-family: 'Kanit', sans-serif;
    }
    
    .pillar-thai {
        font-size: clamp(0.6em, 1.8vw, 0.8em);
        color: #8b4513;
        margin: 0 0 2px 0;
        font-style: italic;
    }
    
    .pillar-detail {
        font-size: clamp(0.6em, 1.6vw, 0.7em);
        color: #a0522d;
        margin: 0;
    }
    
    /* Element Display - Mobile Responsive */
    .element-display {
        margin-top: 20px;
    }
    
    .element-label {
        font-size: clamp(0.9em, 2.5vw, 1.1em);
        color: #8b4513;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .element-circle {
        width: clamp(60px, 15vw, 80px);
        height: clamp(60px, 15vw, 80px);
        border-radius: 50%;
        margin: 10px auto;
        border: 3px solid #fff;
        box-shadow: 
            0 8px 20px rgba(0,0,0,0.3),
            inset 0 2px 5px rgba(255,255,255,0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.3s ease;
    }
    
    .element-circle:hover, .element-circle:active {
        transform: scale(1.05) rotate(5deg);
    }
    
    .element-emoji {
        font-size: clamp(1.8em, 6vw, 2.5em);
    }
    
    .element-name {
        font-size: clamp(1em, 3vw, 1.3em);
        font-weight: 700;
        color: #654321;
        margin: 8px 0 5px 0;
        font-family: 'Kanit', sans-serif;
    }
    
    .element-characteristic {
        font-size: clamp(0.8em, 2.2vw, 0.9em);
        color: #8b4513;
        margin: 5px 0;
        line-height: 1.4;
        font-style: italic;
    }
    
    /* Fortune Container - Mobile Optimized */
    .fortune-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 20px 15px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #d4af37;
    }
    
    .fortune-container h3 {
        color: #8b4513;
        font-family: 'Kanit', sans-serif;
        font-size: clamp(1.2em, 4vw, 1.8em);
        margin-bottom: 15px;
        text-align: center;
        line-height: 1.2;
    }
    
    /* Sidebar Styling - Mobile Friendly */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Button Styling - Touch Optimized */
    .stButton > button {
        background: linear-gradient(45deg, #d4af37, #ffd700);
        color: #8b4513;
        border: none;
        border-radius: 25px;
        padding: 18px 30px;
        font-weight: 600;
        font-size: clamp(1em, 3vw, 1.1em);
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        width: 100%;
        min-height: 50px;
    }
    
    .stButton > button:hover, .stButton > button:active {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #ffd700, #d4af37);
    }
    
    /* Date and Time Input Styling */
    .stDateInput > div, .stTimeInput > div {
        border-radius: 10px;
    }
    
    /* Content Cards - Mobile Responsive */
    .content-card {
        background: rgba(255,255,255,0.9);
        padding: 20px 15px;
        border-radius: 15px;
        line-height: 1.7;
        font-family: 'Sarabun', sans-serif;
        font-size: clamp(0.9em, 2.5vw, 1.1em);
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    
    /* Grid for Analysis Cards */
    .analysis-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 12px;
        margin-top: 15px;
    }
    
    @media (min-width: 600px) {
        .analysis-grid {
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
    }
    
    .analysis-card {
        background: rgba(139,69,19,0.1);
        padding: 15px 12px;
        border-radius: 12px;
        border: 1px solid rgba(212,175,55,0.3);
        transition: all 0.3s ease;
    }
    
    .analysis-card:hover, .analysis-card:active {
        background: rgba(139,69,19,0.2);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Welcome Message - Mobile Centered */
    .welcome-message {
        text-align: center;
        padding: 40px 20px;
        color: rgba(255,255,255,0.9);
    }
    
    .welcome-message h2 {
        font-family: 'Kanit', sans-serif;
        font-size: clamp(1.5em, 5vw, 2.5em);
        margin-bottom: 15px;
        line-height: 1.3;
    }
    
    .welcome-message p {
        font-size: clamp(1em, 3vw, 1.2em);
        font-family: 'Sarabun', sans-serif;
        line-height: 1.6;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Enhanced Loading Screen */
    .mystical-loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.95), rgba(118, 75, 162, 0.95));
        backdrop-filter: blur(10px);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .mystical-loading-content {
        text-align: center;
        color: white;
        padding: 40px 20px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(15px);
        max-width: 90%;
        width: 400px;
    }
    
    .loading-title {
        font-family: 'Kanit', sans-serif;
        font-size: clamp(1.5em, 5vw, 2.5em);
        font-weight: 700;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        background: linear-gradient(45deg, #ffd700, #ffed4e, #d4af37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: titleGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes titleGlow {
        from { 
            filter: drop-shadow(0 0 10px rgba(255, 215, 0, 0.5));
            transform: scale(1);
        }
        to { 
            filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.8));
            transform: scale(1.02);
        }
    }
    
    .loading-subtitle {
        font-family: 'Sarabun', sans-serif;
        font-size: clamp(1em, 3vw, 1.3em);
        margin-bottom: 30px;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.5;
        font-weight: 500;
    }
    
    .mystical-spinner-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 30px 0;
        position: relative;
    }
    
    .mystical-spinner {
        width: clamp(80px, 20vw, 120px);
        height: clamp(80px, 20vw, 120px);
        border: 4px solid rgba(255, 215, 0, 0.2);
        border-top: 4px solid #ffd700;
        border-radius: 50%;
        animation: mysticalSpin 1.5s linear infinite;
        position: relative;
    }
    
    .mystical-spinner::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 60%;
        height: 60%;
        border: 3px solid rgba(255, 255, 255, 0.3);
        border-top: 3px solid #ffffff;
        border-radius: 50%;
        transform: translate(-50%, -50%);
        animation: mysticalSpin 1s linear infinite reverse;
    }
    
    .mystical-spinner::after {
        content: '🔮';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: clamp(1.5em, 5vw, 2.5em);
        animation: float 2s ease-in-out infinite;
    }
    
    @keyframes mysticalSpin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes float {
        0%, 100% { transform: translate(-50%, -50%) translateY(0px); }
        50% { transform: translate(-50%, -50%) translateY(-10px); }
    }
    
    .loading-steps {
        font-family: 'Sarabun', sans-serif;
        font-size: clamp(0.9em, 2.5vw, 1.1em);
        color: rgba(255, 255, 255, 0.8);
        margin-top: 20px;
        line-height: 1.6;
    }
    
    .loading-step {
        margin: 8px 0;
        padding: 5px 0;
        opacity: 0.6;
        transition: all 0.5s ease;
    }
    
    .loading-step.active {
        opacity: 1;
        color: #ffd700;
        font-weight: 600;
        transform: scale(1.05);
    }
    
    .loading-step::before {
        content: '✨ ';
        margin-right: 5px;
    }
    
    .loading-progress-bar {
        width: 100%;
        height: 6px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        margin: 20px 0 10px 0;
        overflow: hidden;
    }
    
    .loading-progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #ffd700, #ffed4e, #d4af37);
        border-radius: 10px;
        animation: progressFlow 3s ease-in-out infinite;
        width: 0%;
    }
    
    @keyframes progressFlow {
        0% { width: 0%; }
        50% { width: 70%; }
        100% { width: 100%; }
    }
    
    /* Hide default streamlit spinner */
    .stSpinner {
        display: none !important;
    }
    
    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(212,175,55,0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(212,175,55,0.7);
    }
    
    /* Accessibility - Focus States */
    .info-item:focus, .pillar-item:focus, .analysis-card:focus {
        outline: 2px solid #d4af37;
        outline-offset: 2px;
    }
    
    /* Print Styles */
    @media print {
        .main {
            background: white !important;
        }
        .board {
            background: white !important;
            border: 1px solid #ccc !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- Chinese BaZi Functions ---
def get_bazi_elements(birth_date, birth_time):
    """Get BaZi (Eight Characters) elements for the given birth date and time."""
    # Heavenly Stems (天干) with Thai translations
    heavenly_stems = [
        {"chinese": "甲", "thai": "กิ๊บ", "element": "木陽", "meaning": "ไม้ชาย"},
        {"chinese": "乙", "thai": "ยี๋", "element": "木陰", "meaning": "ไม้หญิง"},
        {"chinese": "丙", "thai": "บิ๋ง", "element": "火陽", "meaning": "ไฟชาย"},
        {"chinese": "丁", "thai": "ติ๋ง", "element": "火陰", "meaning": "ไฟหญิง"},
        {"chinese": "戊", "thai": "หวู่", "element": "土陽", "meaning": "ดินชาย"},
        {"chinese": "己", "thai": "จี๋", "element": "土陰", "meaning": "ดินหญิง"},
        {"chinese": "庚", "thai": "เกิ่ง", "element": "金陽", "meaning": "โลหะชาย"},
        {"chinese": "辛", "thai": "ซิน", "element": "金陰", "meaning": "โลหะหญิง"},
        {"chinese": "壬", "thai": "เหริน", "element": "水陽", "meaning": "น้ำชาย"},
        {"chinese": "癸", "thai": "กุย", "element": "水陰", "meaning": "น้ำหญิง"}
    ]
    
    # Earthly Branches (地支) with Thai translations
    earthly_branches = [
        {"chinese": "子", "thai": "จื่อ", "animal": "鼠", "thai_animal": "หนู", "time": "23-01น."},
        {"chinese": "丑", "thai": "โฉว", "animal": "牛", "thai_animal": "วัว", "time": "01-03น."},
        {"chinese": "寅", "thai": "อิน", "animal": "虎", "thai_animal": "เสือ", "time": "03-05น."},
        {"chinese": "卯", "thai": "เหมา", "animal": "兔", "thai_animal": "กระต่าย", "time": "05-07น."},
        {"chinese": "辰", "thai": "เฉิน", "animal": "龍", "thai_animal": "มังกร", "time": "07-09น."},
        {"chinese": "巳", "thai": "ซื่อ", "animal": "蛇", "thai_animal": "งู", "time": "09-11น."},
        {"chinese": "午", "thai": "วู่", "animal": "馬", "thai_animal": "ม้า", "time": "11-13น."},
        {"chinese": "未", "thai": "เหวย", "animal": "羊", "thai_animal": "แพะ", "time": "13-15น."},
        {"chinese": "申", "thai": "เสิน", "animal": "猴", "thai_animal": "ลิง", "time": "15-17น."},
        {"chinese": "酉", "thai": "โย่ว", "animal": "雞", "thai_animal": "ไก่", "time": "17-19น."},
        {"chinese": "戌", "thai": "ซู่", "animal": "狗", "thai_animal": "หมา", "time": "19-21น."},
        {"chinese": "亥", "thai": "ไห", "animal": "豬", "thai_animal": "หมู", "time": "21-23น."}
    ]
    
    # Five Elements (五行) with detailed Thai explanations
    elements = {
        "木": {
            "chinese": "木", "thai": "ไม้", "emoji": "🌳", "color": "#22c55e",
            "characteristics": "เจริญเติบโต, ความยืดหยุ่น, ความคิดสร้างสรรค์",
            "personality": "รักอิสระ, มีจิตใจดี, ชอบธรรมชาติ"
        },
        "火": {
            "chinese": "火", "thai": "ไฟ", "emoji": "🔥", "color": "#ef4444",
            "characteristics": "ความร้อนแรง, พลังงานสูง, ความกระตือรือร้น",
            "personality": "ร่าเริง, กระฉับกระเฉง, เป็นผู้นำ"
        },
        "土": {
            "chinese": "土", "thai": "ดิน", "emoji": "🏔️", "color": "#a3a3a3",
            "characteristics": "ความมั่นคง, ความอดทน, ความไว้วางใจได้",
            "personality": "มั่นคง, น่าเชื่อถือ, รักครอบครัว"
        },
        "金": {
            "chinese": "金", "thai": "โลหะ", "emoji": "⚡", "color": "#fbbf24",
            "characteristics": "ความแข็งแกร่ง, ความคมคาย, ความยุติธรรม",
            "personality": "เด็ดขาด, มีหลักการ, รักความยุติธรรม"
        },
        "水": {
            "chinese": "水", "thai": "น้ำ", "emoji": "💧", "color": "#3b82f6",
            "characteristics": "ความยืดหยุ่น, ความลึกซึ้ง, ปัญญา",
            "personality": "ฉลาด, ปรับตัวได้ดี, มีสัญชาตญาณ"
        }
    }
    
    # Simplified calculation
    year = birth_date.year
    month = birth_date.month
    day = birth_date.day
    hour = birth_time.hour
    
    # Calculate pillars
    year_stem_idx = (year - 4) % 10
    year_branch_idx = (year - 4) % 12
    month_stem_idx = (month - 1) % 10
    month_branch_idx = (month - 1) % 12
    day_stem_idx = (day - 1) % 10
    day_branch_idx = (day - 1) % 12
    hour_stem_idx = (hour // 2) % 10
    hour_branch_idx = (hour // 2) % 12
    
    # Dominant element
    dominant_element_key = list(elements.keys())[year % 5]
    dominant_element = elements[dominant_element_key]
    
    return {
        "year_stem": heavenly_stems[year_stem_idx],
        "year_branch": earthly_branches[year_branch_idx],
        "month_stem": heavenly_stems[month_stem_idx],
        "month_branch": earthly_branches[month_branch_idx],
        "day_stem": heavenly_stems[day_stem_idx],
        "day_branch": earthly_branches[day_branch_idx],
        "hour_stem": heavenly_stems[hour_stem_idx],
        "hour_branch": earthly_branches[hour_branch_idx],
        "dominant_element": dominant_element
    }

# --- Enhanced Mobile-Responsive Astrology Board ---
def display_mobile_optimized_boards(day_name, thai_color, thai_animal, english_animal, birth_time, birth_date):
    """Creates mobile-optimized astrology boards."""
    zodiac_emojis = {
        "Rat": "🐭", "Ox": "🐮", "Tiger": "🐯", "Rabbit": "🐰", "Dragon": "🐲", 
        "Snake": "🐍", "Horse": "🐴", "Goat": "🐐", "Monkey": "🐵", 
        "Rooster": "🐔", "Dog": "🐶", "Pig": "🐷"
    }
    animal_emoji = zodiac_emojis.get(english_animal, "✨")
    
    # Color mapping
    color_map = {
        'แดง': '#dc2626', 'เขียว': '#16a34a', 'น้ำเงิน': '#2563eb',
        'เหลือง': '#eab308', 'ม่วง': '#9333ea', 'ชมพู': '#ec4899',
        'ส้ม': '#ea580c', 'ขาว': '#f8fafc', 'ดำ': '#1f2937'
    }
    display_color = color_map.get(thai_color, thai_color.lower())
    
    # Get BaZi elements
    bazi = get_bazi_elements(birth_date, birth_time)
    
    # Thai Board
    st.markdown(f"""
    <div class="board">
        <h3>🔮 กระดานชันษาจร</h3>
        <div class="mobile-grid">
            <div class="info-item">
                <p class="label">🌟 ดาวประจำวัน</p>
                <p class="value">วัน{day_name}</p>
            </div>
            <div class="info-item">
                <p class="label">🐉 ปีนักษัตร</p>
                <p class="value">{thai_animal}</p>
            </div>
            <div class="info-item">
                <p class="label">⏰ เวลาเกิด</p>
                <p class="value">{birth_time.strftime('%H:%M')} น.</p>
            </div>
            <div class="info-item">
                <p class="label">🎨 สีมงคล</p>
                <div class="color-circle" style="background-color: {display_color};"></div>
                <p class="value">{thai_color}</p>
            </div>
        </div>
        <div class="animal-display">
            <span class="animal-emoji">{animal_emoji}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Chinese BaZi Board
    st.markdown(f"""
    <div class="board">
        <h3>🏮 八字命盤 (Bā Zì)</h3>
        <p style="font-size: 0.9em; color: #8b4513; margin-bottom: 15px;">
            โหราศาสตร์จีนโบราณ
        </p>
        <div class="bazi-pillars">
            <div class="pillar-row">
                <div class="pillar-item">
                    <p class="pillar-label">年柱 (ปี)</p>
                    <p class="pillar-value">{bazi['year_stem']['chinese']}{bazi['year_branch']['chinese']}</p>
                    <p class="pillar-thai">({bazi['year_stem']['thai']}{bazi['year_branch']['thai']})</p>
                    <p class="pillar-detail">{bazi['year_branch']['thai_animal']}</p>
                </div>
                <div class="pillar-item">
                    <p class="pillar-label">月柱 (เดือน)</p>
                    <p class="pillar-value">{bazi['month_stem']['chinese']}{bazi['month_branch']['chinese']}</p>
                    <p class="pillar-thai">({bazi['month_stem']['thai']}{bazi['month_branch']['thai']})</p>
                    <p class="pillar-detail">{bazi['month_branch']['thai_animal']}</p>
                </div>
            </div>
            <div class="pillar-row">
                <div class="pillar-item">
                    <p class="pillar-label">日柱 (วัน)</p>
                    <p class="pillar-value">{bazi['day_stem']['chinese']}{bazi['day_branch']['chinese']}</p>
                    <p class="pillar-thai">({bazi['day_stem']['thai']}{bazi['day_branch']['thai']})</p>
                    <p class="pillar-detail">{bazi['day_branch']['thai_animal']}</p>
                </div>
                <div class="pillar-item">
                    <p class="pillar-label">時柱 (เวลา)</p>
                    <p class="pillar-value">{bazi['hour_stem']['chinese']}{bazi['hour_branch']['chinese']}</p>
                    <p class="pillar-thai">({bazi['hour_stem']['thai']}{bazi['hour_branch']['thai']})</p>
                    <p class="pillar-detail">{bazi['hour_branch']['time']}</p>
                </div>
            </div>
        </div>
        <div class="element-display">
            <p class="element-label">主導五行 (ธาตุหลัก)</p>
            <div class="element-circle" style="background-color: {bazi['dominant_element']['color']};">
                <span class="element-emoji">{bazi['dominant_element']['emoji']}</span>
            </div>
            <p class="element-name">{bazi['dominant_element']['chinese']} ({bazi['dominant_element']['thai']})</p>
            <p class="element-characteristic">{bazi['dominant_element']['characteristics']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Main Application ---
def main():
    # Load mobile-responsive CSS
    load_mobile_responsive_css()
    
    # Enhanced Header
    st.markdown("""
    <div class="main-header">
        <h1>🔮 AI โหราจารย์ 🔮</h1>
        <p>✨ ไขความลับแห่งดวงดาว<br>ผูกดวงชะตาไทย-จีนโบราณ ✨</p>
    </div>
    """, unsafe_allow_html=True)

    # Mobile-optimized Sidebar
    with st.sidebar:
        st.markdown("### 📋 ข้อมูลสำหรับผูกดวง")
        st.markdown("---")
        
        default_date = datetime.date.today() - datetime.timedelta(days=365*25)
        birth_date = st.date_input(
            "📅 วัน/เดือน/ปีเกิด:", 
            default_date, 
            min_value=datetime.date(1920, 1, 1), 
            max_value=datetime.date.today()
        )
        
        birth_time = st.time_input(
            "🕐 เวลาเกิด (ถ้าทราบ):", 
            datetime.time(12, 00)
        )
        
        st.markdown("---")
        fortune_button = st.button("🔮 เปิดดวงชะตา", use_container_width=True)

    # Get API key
    api_key = os.environ.get("OPENAI_API_KEY")

    # Main content area
    if fortune_button:
        if not api_key:
            st.error("⚠️ เกิดข้อผิดพลาด: ไม่พบ OpenAI API key บนเซิร์ฟเวอร์")
        elif not birth_date:
            st.error("⚠️ กรุณากรอกวันเกิด")
        else:
            # Success effects
            st.balloons()
            
            # Show enhanced loading screen
            loading_placeholder = st.empty()
            with loading_placeholder.container():
                show_mystical_loading()
            
            # Actual processing with progress simulation
            import time
            time.sleep(1)  # Show loading screen briefly
            
            try:
                # Get fortune details
                day_name, thai_color = get_thai_fortune_details(birth_date)
                thai_animal, english_animal = get_chinese_fortune_details(birth_date.year)
                
                # Clear loading screen and show results
                loading_placeholder.empty()
                
                # Display mobile-optimized boards
                display_mobile_optimized_boards(day_name, thai_color, thai_animal, english_animal, birth_time, birth_date)
                
                # Generate AI fortune with another loading indicator
                with st.spinner("🤖 เทพ AI กำลังเขียนคำพยากรณ์สำหรับคุณ..."):
                    text_fortune = generate_ai_fortune(api_key, day_name, thai_color, thai_animal, birth_time)
                
                # Display fortune in mobile-friendly container
                st.markdown("""
                <div class="fortune-container">
                    <h3>📜 คำพยากรณ์ดวงชะตา</h3>
                </div>
                """, unsafe_allow_html=True)
                
                if "Error:" in text_fortune:
                    st.error(f"❌ {text_fortune}")
                else:
                    # Main fortune text
                    st.markdown(f"""
                    <div class="content-card">
                        {text_fortune}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # BaZi Analysis Section
                    bazi_info = get_bazi_elements(birth_date, birth_time)
                    
                    st.markdown("""
                    <div class="fortune-container">
                        <h3>🏮 การวิเคราะห์บุคลิกตาม八字</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Element analysis
                    st.markdown(f"""
                    <div class="content-card">
                        <h4 style="color: #8b4513; margin-bottom: 15px; text-align: center;">
                            🌟 ธาตุหลัก: {bazi_info['dominant_element']['chinese']} ({bazi_info['dominant_element']['thai']}) {bazi_info['dominant_element']['emoji']}
                        </h4>
                        
                        <p><strong>🎭 ลักษณะเด่น:</strong> {bazi_info['dominant_element']['characteristics']}</p>
                        <p><strong>💫 บุคลิกภาพ:</strong> {bazi_info['dominant_element']['personality']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Pillars explanation
                    st.markdown("<h5 style='color: white; text-align: center; margin: 20px 0;'>📝 ความหมายของเสาทั้ง 4</h5>", unsafe_allow_html=True)
                    
                    # Mobile-friendly grid for pillar meanings
                    st.markdown(f"""
                    <div class="analysis-grid">
                        <div class="analysis-card">
                            <strong>年柱 (ปี):</strong> {bazi_info['year_stem']['chinese']}{bazi_info['year_branch']['chinese']} 
                            ({bazi_info['year_stem']['thai']}{bazi_info['year_branch']['thai']})<br>
                            <small style="color: #8b4513;">บรรพบุรุษ, รากเหง้า, วัยเด็ก</small>
                        </div>
                        <div class="analysis-card">
                            <strong>月柱 (เดือน):</strong> {bazi_info['month_stem']['chinese']}{bazi_info['month_branch']['chinese']} 
                            ({bazi_info['month_stem']['thai']}{bazi_info['month_branch']['thai']})<br>
                            <small style="color: #8b4513;">พ่อแม่, วัยรุ่น, การศึกษา</small>
                        </div>
                        <div class="analysis-card">
                            <strong>日柱 (วัน):</strong> {bazi_info['day_stem']['chinese']}{bazi_info['day_branch']['chinese']} 
                            ({bazi_info['day_stem']['thai']}{bazi_info['day_branch']['thai']})<br>
                            <small style="color: #8b4513;">ตัวเอง, คู่ชีวิต, วัยผู้ใหญ่</small>
                        </div>
                        <div class="analysis-card">
                            <strong>時柱 (เวลา):</strong> {bazi_info['hour_stem']['chinese']}{bazi_info['hour_branch']['chinese']} 
                            ({bazi_info['hour_stem']['thai']}{bazi_info['hour_branch']['thai']})<br>
                            <small style="color: #8b4513;">ลูกหลาน, วัยชรา, อนาคต</small>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
            except Exception as e:
                loading_placeholder.empty()  # Clear loading on error
                st.error(f"❌ เกิดข้อผิดพลาด: {str(e)}")
    
    else:
        # Mobile-optimized welcome message
        st.markdown("""
        <div class="welcome-message">
            <h2>🌟 ยินดีต้อนรับสู่โลกแห่งโหราศาสตร์</h2>
            <p>
                กรอกข้อมูลวันเกิดของคุณในแถบด้านข้าง<br>
                แล้วคลิก "เปิดดวงชะตา" เพื่อเริ่มต้นการเดินทาง<br>
                สู่ความลับแห่งดวงดาว ✨
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

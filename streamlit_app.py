# streamlit_app.py
# Enhanced UI version with modern design and better visual elements

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

# --- Custom CSS for Enhanced UI ---
def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700&family=Kanit:wght@300;400;600;700&display=swap');
    
    /* Global Styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        color: #ffffff;
        font-family: 'Kanit', sans-serif;
        font-size: 3.5em;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-family: 'Sarabun', sans-serif;
        font-size: 1.2em;
        line-height: 1.6;
    }
    
    /* Astrology Board Enhanced */
    .board {
        background: linear-gradient(145deg, #fdf6e3, #f7e98e);
        border: none;
        border-radius: 25px;
        padding: 35px;
        text-align: center;
        font-family: 'Sarabun', sans-serif;
        box-shadow: 
            0 20px 40px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.6);
        margin: 30px 0;
        position: relative;
        overflow: hidden;
    }
    
    /* BaZi Specific Styling */
    .bazi-pillars {
        margin: 20px 0;
    }
    
    .pillar-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 15px;
    }
    
    .pillar-item {
        background: rgba(139, 69, 19, 0.1);
        border: 2px solid #8b4513;
        border-radius: 15px;
        padding: 15px 20px;
        min-width: 80px;
        transition: transform 0.3s ease;
    }
    
    .pillar-item:hover {
        transform: scale(1.05);
        background: rgba(139, 69, 19, 0.2);
    }
    
    .pillar-label {
        font-size: 0.8em;
        color: #8b4513;
        margin: 0 0 5px 0;
        font-weight: 600;
    }
    
    .pillar-value {
        font-size: 1.4em;
        font-weight: 700;
        color: #654321;
        margin: 0 0 3px 0;
        font-family: 'Kanit', sans-serif;
    }
    
    .pillar-thai {
        font-size: 0.8em;
        color: #8b4513;
        margin: 0 0 3px 0;
        font-style: italic;
    }
    
    .pillar-detail {
        font-size: 0.7em;
        color: #a0522d;
        margin: 0;
    }
    
    .element-display {
        margin-top: 25px;
    }
    
    .element-label {
        font-size: 1.1em;
        color: #8b4513;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .element-circle {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin: 10px auto;
        border: 4px solid #fff;
        box-shadow: 
            0 8px 20px rgba(0,0,0,0.3),
            inset 0 2px 5px rgba(255,255,255,0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.3s ease;
    }
    
    .element-circle:hover {
        transform: scale(1.1) rotate(5deg);
    }
    
    .element-emoji {
        font-size: 2.5em;
    }
    
    .element-name {
        font-size: 1.3em;
        font-weight: 700;
        color: #654321;
        margin: 10px 0 5px 0;
        font-family: 'Kanit', sans-serif;
    }
    
    .element-characteristic {
        font-size: 0.9em;
        color: #8b4513;
        margin: 5px 0;
        line-height: 1.4;
        font-style: italic;
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
        margin-bottom: 25px;
        font-family: 'Kanit', sans-serif;
        font-size: 2.2em;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 25px;
        margin-bottom: 25px;
    }
    
    .info-item {
        background: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(212, 175, 55, 0.3);
    }
    
    .info-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .info-item .label {
        font-size: 1em;
        margin-bottom: 8px;
        color: #8b4513;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .info-item .value {
        font-size: 1.4em;
        font-weight: 700;
        color: #654321;
        margin: 0;
        font-family: 'Kanit', sans-serif;
    }
    
    .animal-display {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        border-radius: 50%;
        width: 120px;
        height: 120px;
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
        font-size: 4em;
        line-height: 1;
    }
    
    .color-circle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        margin: 10px auto;
        border: 4px solid #fff;
        box-shadow: 
            0 5px 15px rgba(0,0,0,0.3),
            inset 0 2px 5px rgba(255,255,255,0.5);
        transition: transform 0.3s ease;
    }
    
    .color-circle:hover {
        transform: scale(1.1);
    }
    
    /* Fortune Text Styling */
    .fortune-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-left: 5px solid #d4af37;
    }
    
    .fortune-container h3 {
        color: #8b4513;
        font-family: 'Kanit', sans-serif;
        font-size: 1.8em;
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(45deg, #d4af37, #ffd700);
        color: #8b4513;
        border: none;
        border-radius: 25px;
        padding: 15px 30px;
        font-weight: 600;
        font-size: 1.1em;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #ffd700, #d4af37);
    }
    
    /* Loading Animation */
    .loading-container {
        text-align: center;
        padding: 40px;
    }
    
    .mystical-loader {
        display: inline-block;
        width: 60px;
        height: 60px;
        border: 3px solid rgba(212, 175, 55, 0.3);
        border-radius: 50%;
        border-top-color: #d4af37;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
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
        {"chinese": "子", "thai": "จื่อ", "animal": "鼠", "thai_animal": "หนู", "time": "23:00-01:00"},
        {"chinese": "丑", "thai": "โฉว", "animal": "牛", "thai_animal": "วัว", "time": "01:00-03:00"},
        {"chinese": "寅", "thai": "อิน", "animal": "虎", "thai_animal": "เสือ", "time": "03:00-05:00"},
        {"chinese": "卯", "thai": "เหมา", "animal": "兔", "thai_animal": "กระต่าย", "time": "05:00-07:00"},
        {"chinese": "辰", "thai": "เฉิน", "animal": "龍", "thai_animal": "มังกร", "time": "07:00-09:00"},
        {"chinese": "巳", "thai": "ซื่อ", "animal": "蛇", "thai_animal": "งู", "time": "09:00-11:00"},
        {"chinese": "午", "thai": "วู่", "animal": "馬", "thai_animal": "ม้า", "time": "11:00-13:00"},
        {"chinese": "未", "thai": "เหวย", "animal": "羊", "thai_animal": "แพะ", "time": "13:00-15:00"},
        {"chinese": "申", "thai": "เสิน", "animal": "猴", "thai_animal": "ลิง", "time": "15:00-17:00"},
        {"chinese": "酉", "thai": "โย่ว", "animal": "雞", "thai_animal": "ไก่", "time": "17:00-19:00"},
        {"chinese": "戌", "thai": "ซู่", "animal": "狗", "thai_animal": "หมา", "time": "19:00-21:00"},
        {"chinese": "亥", "thai": "ไห", "animal": "豬", "thai_animal": "หมู", "time": "21:00-23:00"}
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
    
    # Simplified calculation (in real app, you'd use proper Chinese calendar conversion)
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
    
    # Dominant element (simplified)
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

# --- Enhanced Astrology Board Function ---
def display_enhanced_astrology_board(day_name, thai_color, thai_animal, english_animal, birth_time, birth_date):
    """Creates an enhanced visually appealing astrology board with both Thai and Chinese systems."""
    zodiac_emojis = {
        "Rat": "🐭", "Ox": "🐮", "Tiger": "🐯", "Rabbit": "🐰", "Dragon": "🐲", 
        "Snake": "🐍", "Horse": "🐴", "Goat": "🐐", "Monkey": "🐵", 
        "Rooster": "🐔", "Dog": "🐶", "Pig": "🐷"
    }
    animal_emoji = zodiac_emojis.get(english_animal, "✨")
    
    # Color mapping for better display
    color_map = {
        'แดง': '#dc2626', 'เขียว': '#16a34a', 'น้ำเงิน': '#2563eb',
        'เหลือง': '#eab308', 'ม่วง': '#9333ea', 'ชมพู': '#ec4899',
        'ส้ม': '#ea580c', 'ขาว': '#f8fafc', 'ดำ': '#1f2937'
    }
    display_color = color_map.get(thai_color, thai_color.lower())
    
    # Get BaZi elements
    bazi = get_bazi_elements(birth_date, birth_time)

    # Create two columns for Thai and Chinese boards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="board">
            <h3>🔮 กระดานชันษาจร 🔮</h3>
            <div class="info-grid">
                <div class="info-item">
                    <p class="label">🌟 ดาวพระเคราะห์ประจำวัน</p>
                    <p class="value">วัน{day_name}</p>
                </div>
                <div class="info-item">
                    <p class="label">🐉 ปีนักษัตร</p>
                    <p class="value">{thai_animal}</p>
                </div>
                <div class="info-item">
                    <p class="label">⏰ เวลาตกฟาก</p>
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
    
    with col2:
        st.markdown(f"""
        <div class="board">
            <h3>🏮 八字命盤 (Bā Zì) 🏮</h3>
            <p style="font-size: 0.9em; color: #8b4513; margin-bottom: 20px;">
                ระบบโหราศาสตร์จีนโบราณ คำนวณจากวันเวลาเกิด
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
    # Load custom CSS
    load_custom_css()
    
    # Enhanced Header
    st.markdown("""
    <div class="main-header">
        <h1>🔮 AI โหราจารย์ 🔮</h1>
        <p>✨ ไขความลับแห่งดวงดาว ผูกดวงชะตาตามหลักโหราศาสตร์ไทย-จีนโบราณ ✨<br>
        🌟 เพื่อค้นหาคำตอบและแนวทางแห่งชีวิต 🌟</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar for Inputs
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
            
            # Loading spinner with custom message
            with st.spinner("🔮 กำลังผูกดวงและอ่านคำพยากรณ์... ✨"):
                try:
                    # Get fortune details
                    day_name, thai_color = get_thai_fortune_details(birth_date)
                    thai_animal, english_animal = get_chinese_fortune_details(birth_date.year)
                    
                    # Display enhanced astrology board
                    display_enhanced_astrology_board(day_name, thai_color, thai_animal, english_animal, birth_time, birth_date)
                    
                    # Generate AI fortune
                    text_fortune = generate_ai_fortune(api_key, day_name, thai_color, thai_animal, birth_time)
                    
                    # Display fortune in styled container
                    st.markdown("""
                    <div class="fortune-container">
                        <h3>📜 คำพยากรณ์ดวงชะตา 📜</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if "Error:" in text_fortune:
                        st.error(f"❌ {text_fortune}")
                    else:
                        st.markdown(f"""
                        <div style="background: rgba(255,255,255,0.9); padding: 25px; border-radius: 15px; 
                                    line-height: 1.8; font-family: 'Sarabun', sans-serif; font-size: 1.1em;
                                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                            {text_fortune}
                        </div>
                        """, unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"❌ เกิดข้อผิดพลาด: {str(e)}")
    
    else:
        # Welcome message when no fortune is generated
        st.markdown("""
        <div style="text-align: center; padding: 50px; color: rgba(255,255,255,0.8);">
            <h2 style="font-family: 'Kanit', sans-serif;">🌟 ยินดีต้อนรับสู่โลกแห่งโหราศาสตร์ 🌟</h2>
            <p style="font-size: 1.2em; font-family: 'Sarabun', sans-serif; line-height: 1.6;">
                กรอกข้อมูลวันเกิดของคุณในแถบด้านข้าง<br>
                แล้วคลิก "เปิดดวงชะตา" เพื่อเริ่มต้นการเดินทางสู่ความลับแห่งดวงดาว ✨
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

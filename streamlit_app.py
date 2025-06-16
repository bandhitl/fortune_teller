# streamlit_app.py
# Complete AI Astrology App with Real AI Integration

import streamlit as st
import datetime
import os
import openai
import calendar

# Page config
st.set_page_config(
    page_title="AI โหราศาสตร์ไทย-จีน",
    page_icon="🔮",
    layout="wide"
)

# Thai Fortune Functions
def get_thai_fortune_details(birth_date):
    """Get Thai astrology details based on birth date."""
    days = ['จันทร์', 'อังคาร', 'พุธ', 'พฤหัสบดี', 'ศุกร์', 'เสาร์', 'อาทิตย์']
    colors = ['เหลือง', 'ชมพู', 'เขียว', 'ส้ม', 'น้ำเงิน', 'ม่วง', 'แดง']
    
    day_of_week = birth_date.weekday()
    day_name = days[day_of_week]
    color = colors[day_of_week]
    
    return day_name, color

def get_chinese_fortune_details(birth_year):
    """Get Chinese zodiac details."""
    animals = [
        ('หนู', 'Rat'), ('วัว', 'Ox'), ('เสือ', 'Tiger'), ('กระต่าย', 'Rabbit'),
        ('มังกร', 'Dragon'), ('งู', 'Snake'), ('ม้า', 'Horse'), ('แพะ', 'Goat'),
        ('ลิง', 'Monkey'), ('ไก่', 'Rooster'), ('หมา', 'Dog'), ('หมู', 'Pig')
    ]
    
    index = (birth_year - 1900) % 12
    thai_animal, english_animal = animals[index]
    
    return thai_animal, english_animal

def get_bazi_elements(birth_date, birth_time):
    """Get simplified BaZi elements."""
    heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    elements = {
        "木": {"chinese": "木", "thai": "ไม้", "emoji": "🌳", "color": "#22c55e"},
        "火": {"chinese": "火", "thai": "ไฟ", "emoji": "🔥", "color": "#ef4444"},
        "土": {"chinese": "土", "thai": "ดิน", "emoji": "🏔️", "color": "#a3a3a3"},
        "金": {"chinese": "金", "thai": "โลหะ", "emoji": "⚡", "color": "#fbbf24"},
        "水": {"chinese": "水", "thai": "น้ำ", "emoji": "💧", "color": "#3b82f6"}
    }
    
    year = birth_date.year
    month = birth_date.month
    day = birth_date.day
    hour = birth_time.hour
    
    year_stem = heavenly_stems[(year - 4) % 10]
    year_branch = earthly_branches[(year - 4) % 12]
    month_stem = heavenly_stems[(month - 1) % 10]
    month_branch = earthly_branches[(month - 1) % 12]
    day_stem = heavenly_stems[(day - 1) % 10]
    day_branch = earthly_branches[(day - 1) % 12]
    hour_stem = heavenly_stems[(hour // 2) % 10]
    hour_branch = earthly_branches[(hour // 2) % 12]
    
    dominant_element_key = list(elements.keys())[year % 5]
    dominant_element = elements[dominant_element_key]
    
    return {
        "year_pillar": f"{year_stem}{year_branch}",
        "month_pillar": f"{month_stem}{month_branch}",
        "day_pillar": f"{day_stem}{day_branch}",
        "hour_pillar": f"{hour_stem}{hour_branch}",
        "dominant_element": dominant_element
    }

def generate_ai_fortune(birth_date, birth_time, day_name, thai_color, thai_animal):
    """Generate AI fortune using OpenAI."""
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "❌ ไม่พบ OpenAI API Key ในระบบ กรุณาตั้งค่า Environment Variable"
    
    try:
        # Use older openai syntax that works
        openai.api_key = api_key
        
        # Calculate age
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        prompt = f"""
        คุณเป็นหมอดูผู้เชี่ยวชาญด้านโหราศาสตร์ไทยและจีน กรุณาทำนายดวงชะตาให้กับบุคคลที่มีข้อมูลดังนี้:

        ข้อมูลพื้นฐาน:
        - วันเกิด: {birth_date.strftime('%d %B %Y')}
        - เวลาเกิด: {birth_time.strftime('%H:%M')} น.
        - อายุ: {age} ปี
        
        ข้อมูลโหราศาสตร์ไทย:
        - ดาวประจำวัน: วัน{day_name}
        - สีมงคล: {thai_color}
        - ปีนักษัตร: {thai_animal}
        
        กรุณาเขียนคำทำนายที่ครอบคลุม:
        1. ลักษณะนิสัยและบุคลิกภาพ
        2. โชคลาภและการเงิน
        3. ความรักและครอบครัว  
        4. การงานและอาชีพ
        5. สุขภาพ
        6. คำแนะนำสำหรับปีนี้
        
        ใช้ภาษาไทยที่สวยงาม เป็นกันเอง และให้กำลังใจ ยาวประมาณ 300-400 คำ
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Use GPT-4o as requested
            messages=[
                {"role": "system", "content": "คุณเป็นหมอดูผู้เชี่ยวชาญด้านโหราศาสตร์ไทยและจีน มีประสบการณ์กว่า 30 ปี ให้คำทำนายที่แม่นยำและให้กำลังใจ"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {str(e)}"

# CSS Styling
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

.board {
    background: linear-gradient(145deg, #fef3c7, #fbbf24);
    border: none;
    border-radius: 20px;
    padding: 20px 15px;
    text-align: center;
    box-shadow: 0 15px 35px rgba(220, 38, 38, 0.2);
    margin: 15px 0;
    border-top: 4px solid #dc2626;
}

.board h3 {
    color: #991b1b;
    margin-bottom: 20px;
    font-size: 1.5em;
    font-weight: 600;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 15px;
    margin-bottom: 20px;
}

.info-item {
    background: rgba(255, 255, 255, 0.9);
    padding: 15px 10px;
    border-radius: 12px;
    border: 1px solid rgba(220, 38, 38, 0.3);
}

.info-item .label {
    font-size: 0.9em;
    color: #991b1b;
    font-weight: 600;
    margin-bottom: 5px;
}

.info-item .value {
    font-size: 1.2em;
    font-weight: 700;
    color: #7f1d1d;
    margin: 0;
}

.animal-display {
    background: linear-gradient(45deg, #fbbf24, #f59e0b);
    border-radius: 50%;
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 15px auto;
    border: 3px solid #dc2626;
}

.animal-emoji {
    font-size: 2.5em;
}

.color-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin: 8px auto;
    border: 3px solid #dc2626;
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
        datetime.date(1990, 1, 1),
        min_value=datetime.date(1950, 1, 1), 
        max_value=datetime.date.today()
    )

with col2:
    birth_time = st.time_input(
        "🕐 เวลาเกิด:", 
        datetime.time(12, 0)
    )950, 1, 1), 
        max_value=datetime.date.today()
    )

with col2:
    birth_time = st.time_input(
        "🕐 เวลาเกิด:", 
        datetime.time(12, 0)
    )

# Main fortune telling button
if st.button("🔮 เปิดดวงชะตา", use_container_width=True, type="primary"):
    st.balloons()
    
    # Calculate astrology data
    day_name, thai_color = get_thai_fortune_details(birth_date)
    thai_animal, english_animal = get_chinese_fortune_details(birth_date.year)
    bazi = get_bazi_elements(birth_date, birth_time)
    
    # Display astrology boards
    col_left, col_right = st.columns(2)
    
    # Thai astrology board
    with col_left:
        zodiac_emojis = {
            "Rat": "🐭", "Ox": "🐮", "Tiger": "🐯", "Rabbit": "🐰", "Dragon": "🐲", 
            "Snake": "🐍", "Horse": "🐴", "Goat": "🐐", "Monkey": "🐵", 
            "Rooster": "🐔", "Dog": "🐶", "Pig": "🐷"
        }
        animal_emoji = zodiac_emojis.get(english_animal, "✨")
        
        color_map = {
            'แดง': '#dc2626', 'เขียว': '#16a34a', 'น้ำเงิน': '#2563eb',
            'เหลือง': '#eab308', 'ม่วง': '#9333ea', 'ชมพู': '#ec4899',
            'ส้ม': '#ea580c', 'ขาว': '#f8fafc', 'ดำ': '#1f2937'
        }
        display_color = color_map.get(thai_color, thai_color.lower())
        
        st.markdown(f"""
        <div class="board">
            <h3>🔮 กระดานชันษาจร</h3>
            <div class="info-grid">
                <div class="info-item">
                    <div class="label">🌟 ดาวประจำวัน</div>
                    <div class="value">วัน{day_name}</div>
                </div>
                <div class="info-item">
                    <div class="label">🐉 ปีนักษัตร</div>
                    <div class="value">{thai_animal}</div>
                </div>
                <div class="info-item">
                    <div class="label">⏰ เวลาเกิด</div>
                    <div class="value">{birth_time.strftime('%H:%M')} น.</div>
                </div>
                <div class="info-item">
                    <div class="label">🎨 สีมงคล</div>
                    <div class="color-circle" style="background-color: {display_color};"></div>
                    <div class="value">{thai_color}</div>
                </div>
            </div>
            <div class="animal-display">
                <span class="animal-emoji">{animal_emoji}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Chinese BaZi board
    with col_right:
        st.markdown(f"""
        <div class="board">
            <h3>🏮 八字命盤</h3>
            <div class="info-grid">
                <div class="info-item">
                    <div class="label">年柱 (ปี)</div>
                    <div class="value">{bazi['year_pillar']}</div>
                </div>
                <div class="info-item">
                    <div class="label">月柱 (เดือน)</div>
                    <div class="value">{bazi['month_pillar']}</div>
                </div>
                <div class="info-item">
                    <div class="label">日柱 (วัน)</div>
                    <div class="value">{bazi['day_pillar']}</div>
                </div>
                <div class="info-item">
                    <div class="label">時柱 (เวลา)</div>
                    <div class="value">{bazi['hour_pillar']}</div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 15px;">
                <div style="font-size: 1em; color: #991b1b; font-weight: 600;">ธาตุหลัก</div>
                <div style="
                    width: 60px; height: 60px; border-radius: 50%; 
                    background-color: {bazi['dominant_element']['color']};
                    margin: 10px auto; display: flex; align-items: center; justify-content: center;
                    border: 3px solid #dc2626;
                ">
                    <span style="font-size: 2em;">{bazi['dominant_element']['emoji']}</span>
                </div>
                <div style="font-weight: 700; color: #7f1d1d;">
                    {bazi['dominant_element']['chinese']} ({bazi['dominant_element']['thai']})
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Generate AI fortune with proper loading
    st.markdown("### 📜 คำพยากรณ์ดวงชะตา")
    
    # Show comprehensive loading that waits for actual AI response
    with st.spinner("🤖 AI กำลังวิเคราะห์ดวงชะตาของคุณ กรุณารอสักครู่... (อาจใช้เวลา 30-60 วินาที)"):
        # Generate AI fortune - spinner will stay until this actually completes
        fortune_text = generate_ai_fortune(birth_date, birth_time, day_name, thai_color, thai_animal)
    
    # Only show result after AI is completely done
    if fortune_text:
    
    # Only show result after AI is completely done
    if fortune_text:
        # Display fortune
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.95);
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
            line-height: 1.8;
            color: #333;
            border-left: 5px solid #dc2626;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        ">
            {fortune_text}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ ไม่สามารถสร้างคำทำนายได้ กรุณาลองใหม่")

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: rgba(255,255,255,0.7);">'
    'พัฒนาโดย AI โหราจารย์ | ใช้ OpenAI GPT-4</p>', 
    unsafe_allow_html=True
)

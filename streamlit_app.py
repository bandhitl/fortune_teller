# streamlit_app.py
# Complete working AI Astrology App with Enhanced Fortune Telling

import streamlit as st
import datetime
import os
import openai

# Page config
st.set_page_config(
    page_title="AI โหราศาสตร์ไทย-จีน",
    page_icon="🔮",
    layout="wide"
)

# Functions
def get_thai_fortune_details(birth_date):
    days = ['จันทร์', 'อังคาร', 'พุธ', 'พฤหัสบดี', 'ศุกร์', 'เสาร์', 'อาทิตย์']
    colors = ['เหลือง', 'ชมพู', 'เขียว', 'ส้ม', 'น้ำเงิน', 'ม่วง', 'แดง']
    day_of_week = birth_date.weekday()
    return days[day_of_week], colors[day_of_week]

def get_chinese_fortune_details(birth_year):
    animals = [
        ('หนู', 'Rat'), ('วัว', 'Ox'), ('เสือ', 'Tiger'), ('กระต่าย', 'Rabbit'),
        ('มังกร', 'Dragon'), ('งู', 'Snake'), ('ม้า', 'Horse'), ('แพะ', 'Goat'),
        ('ลิง', 'Monkey'), ('ไก่', 'Rooster'), ('หมา', 'Dog'), ('หมู', 'Pig')
    ]
    index = (birth_year - 1900) % 12
    return animals[index]

def get_bazi_elements(birth_date, birth_time):
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

def generate_enhanced_ai_fortune(birth_date, birth_time, day_name, thai_color, thai_animal):
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "❌ ไม่พบ OpenAI API Key ในระบบ กรุณาตั้งค่า Environment Variable"
    
    try:
        openai.api_key = api_key
        
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Enhanced detailed prompt
        text_prompt = (
            f"จงสวมบทบาทเป็น 'ซินแสผู้เชี่ยวชาญศาสตร์จีนระดับปรมาจารย์' ทำการวิเคราะห์ดวงชะตา (ปาจื่อ - 八字) ของบุคคลผู้ถือกำเนิดในวัน {day_name}, เวลา {birth_time.strftime('%H:%M')}, ในปีนักษัตร {thai_animal} (ซึ่งมีรากฐานธาตุตามปีเกิด) โดยมีสี {thai_color} เป็นสีเสริมดวงชะตา.\n\n"
            f"**คำสั่งในการวิเคราะห์ดวงชะตา:**\n"
            f"จงเริ่มต้นด้วยการ 'เปิดฟ้าอ่านชะตา' โดยวิเคราะห์ปัจจัยพื้นฐานแห่ง 'ฟ้า-ดิน-คน' ของดวงชะตานี้ก่อน:\n"
            f" - **ฟ้า (天):** อธิบายว่าพลังแห่งปีนักษัตร {thai_animal} กำหนด 'ธาตุประจำตัว' และภาพรวมแห่งชีวิตไว้อย่างไร\n"
            f" - **ดิน (地):** วิเคราะห์ว่าพลังหยิน (陰) หรือ หยาง (陽) จากเวลาตกฟาก {birth_time.strftime('%H:%M')} ส่งผลต่อเสถียรภาพและจังหวะชีวิตอย่างไร\n"
            f" - **คน (人):** อธิบายว่าอิทธิพลจากวันเกิด ({day_name}) ตามคติไทย ช่วยเสริมหรือขัดเกลาพลังจากฟ้าและดินอย่างไรบ้าง\n"
            f"จงอธิบายปฏิสัมพันธ์ของทั้งสามส่วนนี้ เพื่อสรุปรากฐานความเข้าใจที่ลึกซึ้งและน่าเชื่อถือสูงสุด\n\n"
            f"เมื่อวางรากฐานแห่งชะตาแล้ว จึงเริ่ม 'ชี้ชัดพยากรณ์' อย่างละเอียดในหัวข้อต่อไปนี้:\n"
            f"1. **วิเคราะห์แก่นแท้และพลังธาตุ:** เจาะลึกถึงบุคลิกภาพ อุปนิสัย จุดแข็งที่ควรส่งเสริม และจุดอ่อนที่ต้องระวัง ตามหลักเบญจธาตุ (ดิน น้ำ ไฟ ไม้ ทอง)\n"
            f"2. **ระดับวาสนาและคำเตือนที่ต้องจำให้ขึ้นใจ:** จากการวิเคราะห์ทั้งหมด ให้ประเมิน 'คะแนนวาสนา' เต็ม 100 (เกณฑ์: 90+ คือดวงชะตาระดับสูง, 60-89 คือระดับปานกลาง-ดี) จากนั้นให้อธิบายถึง 'วาสนาที่ดี' หรือพรสวรรค์ที่โดดเด่นของดวงชะตานี้ แล้วจึงให้ **'คำเตือน' ที่ใช้ภาษากระชับ รุนแรง แต่แฝงด้วยความปรารถนาดี (ขอความยาวเป็นพิเศษในส่วนนี้เพื่อความชัดเจน) เพื่อให้ผู้รับสารจำขึ้นใจและตระหนักถึงผลที่จะตามมา**\n"
            f"3. **พยากรณ์ชะตา 6 เดือนข้างหน้า:** วิเคราะห์แนวโน้มสำคัญในด้าน การงาน, การเงิน, และความรัก ที่จะเกิดขึ้นในอีก 6 เดือนนับจากนี้ ชี้ชัดถึงเดือนที่โดดเด่นและเดือนที่ต้องระมัดระวัง\n"
            f"4. **เส้นทางแห่งความมั่งคั่ง (การงาน-การเงิน):** ชี้แนะอาชีพที่ส่งเสริมธาตุประจำตัว ทิศทางการลงทุนที่เหมาะสม **เพิ่มหัวข้อ 'มุมมองจากเจ้าคนนายคน (สิ่งที่หัวหน้างานคิดกับท่านในตอนนี้)' โดยให้วิเคราะห์แบบตรงไปตรงมา ไม่ต้องอ้อมค้อม แต่ให้เป็นไปในเชิงสร้างสรรค์เพื่อการพัฒนา ไม่บั่นทอนกำลังใจ** และสุดท้ายมอบ 'คำคมนำทาง' ที่สร้างแรงบันดาลใจในการทำงาน 1 ประโยค\n"
            f"5. **วาสนาแห่งรักและเครือข่ายสัมพันธ์ (ความรัก-สังคม):** วิเคราะห์ลักษณะเนื้อคู่ตามธาตุที่สมพงษ์ วิธีการเสริมสร้างเสน่ห์ และการบริหารความสัมพันธ์กับคนรอบข้าง\n"
            f"6. **สมดุลแห่งสังขาร (สุขภาพ):** ให้คำแนะนำในการดูแลสุขภาพตามธาตุเจ้าเรือน และอวัยวะที่ต้องใส่ใจเป็นพิเศษ\n"
            f"7. **กลยุทธ์ปรับเปลี่ยนชะตา:** แนะนำแนวทางการใช้ชีวิต การปรับสภาพแวดล้อม (ฮวงจุ้ย) หรือการใช้วัตถุมงคล/สีมงคล เพื่อปรับสมดุลธาตุและเสริมสร้างสิริมงคล\n\n"
            f"**ส่วนสุดท้าย: บทสรุปสำหรับท่าน (ฉบับเข้าใจง่าย)**\n"
            f"หลังจากคำพยากรณ์ทั้งหมด จงสรุปใจความสำคัญในแต่ละด้าน (ภาพรวม, การงาน, ความรัก, และคำเตือนที่สำคัญที่สุด) ให้เป็นภาษาที่คนทั่วไปเข้าใจง่ายและนำไปใช้ได้ทันที โดยแยกเป็นข้อๆ\n\n"
            f"จงรจนาคำพยากรณ์ทั้งหมดเป็น **'ภาษาไทย'** ด้วยลีลาของซินแสผู้ทรงภูมิ มีความหนักแน่น ชัดเจน และให้คำแนะนำที่สามารถนำไปปรับใช้ในชีวิตได้จริง"
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system", 
                    "content": "คุณเป็นซินแสผู้เชี่ยวชาญศาสตร์จีนระดับปรมาจารย์ มีประสบการณ์กว่า 50 ปี เชี่ยวชาญทั้งโหราศาสตร์ไทยและจีน ปาจื่อ ฮวงจุ้ย และเบญจธาตุ ให้คำทำนายที่ลึกซึ้ง แม่นยำ และสร้างสรรค์"
                },
                {"role": "user", "content": text_prompt}
            ],
            max_tokens=2000,
            temperature=0.8
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {str(e)}"

# CSS
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

.fortune-content {
    background: rgba(255,255,255,0.95);
    padding: 30px;
    border-radius: 15px;
    margin: 20px 0;
    line-height: 1.8;
    color: #333;
    border-left: 5px solid #dc2626;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    font-size: 1.1em;
}

.fortune-section {
    margin-bottom: 25px;
    padding-bottom: 20px;
    border-bottom: 1px solid #e5e5e5;
}

.fortune-section:last-child {
    border-bottom: none;
}

.section-title {
    color: #dc2626;
    font-weight: 700;
    font-size: 1.3em;
    margin-bottom: 15px;
    text-decoration: underline;
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
    <p style="color: rgba(255, 255, 255, 0.8); font-size: 1em;">
        📜 วิเคราะห์ลึก ด้วยปรมาจารย์ซินแสแห่งศาสตร์จีน 📜
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
    )

# Button
if st.button("🔮 เปิดดวงชะตา", use_container_width=True, type="primary"):
    st.balloons()
    
    day_name, thai_color = get_thai_fortune_details(birth_date)
    thai_animal, english_animal = get_chinese_fortune_details(birth_date.year)
    bazi = get_bazi_elements(birth_date, birth_time)
    
    col_left, col_right = st.columns(2)
    
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
    
    st.markdown("### 📜 คำพยากรณ์ดวงชะตาจากซินแสปรมาจารย์")
    
    with st.spinner("🤖 ซินแสปรมาจารย์กำลังเปิดฟ้าอ่านชะตา กรุณารอสักครู่..."):
        fortune_text = generate_enhanced_ai_fortune(birth_date, birth_time, day_name, thai_color, thai_animal)
    
    if fortune_text:
        st.markdown(f"""
        <div class="fortune-content">
            {fortune_text.replace('\\n', '<br>').replace('**', '<strong>').replace('**', '</strong>')}
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: rgba(255,255,255,0.7);">'
    'พัฒนาโดย AI โหราจารย์ | ใช้ OpenAI GPT-4o | Enhanced by ซินแสปรมาจารย์</p>', 
    unsafe_allow_html=True
)

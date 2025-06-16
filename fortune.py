# fortune.py
# This file contains the core logic for calculating Thai and Chinese fortunes
# and generating a detailed AI-powered reading in Thai using the latest gpt-4o model.

import datetime
import os
import openai # Import the openai library (older version syntax v0.28.0)

def get_thai_fortune_details(birth_date):
    """
    Determines the Thai day-of-birth details.

    Args:
        birth_date (datetime.date): The user's date of birth.

    Returns:
        tuple: A tuple containing the day name and its associated color.
    """
    day_index = birth_date.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = days[day_index]

    thai_colors = {
        "Sunday": "Red",
        "Monday": "Yellow",
        "Tuesday": "Pink",
        "Wednesday": "Green",
        "Thursday": "Orange",
        "Friday": "Blue",
        "Saturday": "Purple"
    }
    return day_name, thai_colors[day_name]

def get_chinese_fortune_details(year):
    """
    Determines the Chinese Zodiac animal.

    Args:
        year (int): The user's year of birth.

    Returns:
        str: The name of the zodiac animal.
    """
    zodiac_animals = {
        "Rat": "ชวด (หนู)", "Ox": "ฉลู (วัว)", "Tiger": "ขาล (เสือ)", 
        "Rabbit": "เถาะ (กระต่าย)", "Dragon": "มะโรง (มังกร)", "Snake": "มะเส็ง (งูเล็ก)",
        "Horse": "มะเมีย (ม้า)", "Goat": "มะแม (แพะ)", "Monkey": "วอก (ลิง)",
        "Rooster": "ระกา (ไก่)", "Dog": "จอ (สุนัข)", "Pig": "กุน (หมู)"
    }
    english_zodiacs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    index = (year - 4) % 12
    animal_key = english_zodiacs[index]
    return zodiac_animals[animal_key], animal_key # Return both Thai and English names

def generate_ai_fortune(api_key, day_name, thai_color, thai_animal, birth_time):
    """
    Generates a detailed fortune in Thai.

    Args:
        api_key (str): The user's OpenAI API key.
        day_name (str): The day of the week of birth (English).
        thai_color (str): The lucky color (English).
        thai_animal (str): The Chinese zodiac animal (Thai).
        birth_time (datetime.time): The user's time of birth.

    Returns:
        str: A detailed, AI-generated fortune in Thai, or an error message.
    """
    if not api_key:
        return "Error: OpenAI API key is missing."
    
    try:
        # --- Using Stable Library Version (v0.28.0) ---
        openai.api_key = api_key

        # --- Generate Fortune Text in Thai ---
        text_prompt = (
            f"จงสวมบทบาทเป็น 'ซินแสผู้เชี่ยวชาญศาสตร์จีนระดับปรมาจารย์' ทำการวิเคราะห์ดวงชะตา (ปาจื่อ - 八字) ของบุคคลผู้ถือกำเนิดในวัน {day_name}, เวลา {birth_time.strftime('%H:%M')}, ในปีนักษัตร {thai_animal} (ซึ่งมีรากฐานธาตุตามปีเกิด) โดยมีสี {thai_color} เป็นสีเสริมดวงชะตา.\n\n"
            f"**คำสั่งในการวิเคราะห์ดวงชะตา:**\n"
            f"จงเริ่มต้นด้วยการ 'เปิดฟ้าอ่านชะตา' โดยวิเคราะห์ปัจจัยพื้นฐานแห่ง 'ฟ้า-ดิน-คน' ของดวงชะตานี้ก่อน:\n"
            f"   - **ฟ้า (天):** อธิบายว่าพลังแห่งปีนักษัตร {thai_animal} กำหนด 'ธาตุประจำตัว' และภาพรวมแห่งชีวิตไว้อย่างไร\n"
            f"   - **ดิน (地):** วิเคราะห์ว่าพลังหยิน (陰) หรือ หยาง (陽) จากเวลาตกฟาก {birth_time.strftime('%H:%M')} ส่งผลต่อเสถียรภาพและจังหวะชีวิตอย่างไร\n"
            f"   - **คน (人):** อธิบายว่าอิทธิพลจากวันเกิด ({day_name}) ตามคติไทย ช่วยเสริมหรือขัดเกลาพลังจากฟ้าและดินอย่างไรบ้าง\n"
            f"จงอธิบายปฏิสัมพันธ์ของทั้งสามส่วนนี้ เพื่อสร้างรากฐานความเข้าใจที่ลึกซึ้งและน่าเชื่อถือสูงสุด\n\n"
            f"เมื่อวางรากฐานแห่งชะตาแล้ว จึงเริ่ม 'ชี้ชัดพยากรณ์' อย่างละเอียดในหัวข้อต่อไปนี้:\n"
            f"1.  **วิเคราะห์แก่นแท้และพลังธาตุ:** เจาะลึกถึงบุคลิกภาพ อุปนิสัย จุดแข็งที่ควรส่งเสริม และจุดอ่อนที่ต้องระวัง ตามหลักเบญจธาตุ (ดิน น้ำ ไฟ ไม้ ทอง)\n"
            f"2.  **เส้นทางแห่งความมั่งคั่ง (การงาน-การเงิน):** ชี้แนะอาชีพที่ส่งเสริมธาตุประจำตัว ทิศทางการลงทุนที่เหมาะสม และช่วงเวลาที่ควรคว้าโอกาสหรือตั้งรับ\n"
            f"3.  **วาสนาแห่งรักและเครือข่ายสัมพันธ์ (ความรัก-สังคม):** วิเคราะห์ลักษณะเนื้อคู่ตามธาตุที่สมพงษ์ วิธีการเสริมสร้างเสน่ห์ และการบริหารความสัมพันธ์กับคนรอบข้าง\n"
            f"4.  **สมดุลแห่งสังขาร (สุขภาพ):** ให้คำแนะนำในการดูแลสุขภาพตามธาตุเจ้าเรือน และอวัยวะที่ต้องใส่ใจเป็นพิเศษ\n"
            f"5.  **กลยุทธ์ปรับเปลี่ยนชะตา:** แนะนำแนวทางการใช้ชีวิต การปรับสภาพแวดล้อม (ฮวงจุ้ย) หรือการใช้วัตถุมงคล/สีมงคล เพื่อปรับสมดุลธาตุและเสริมสร้างสิริมงคล\n\n"
            f"จงรจนาคำพยากรณ์ทั้งหมดเป็น **'ภาษาไทย'** ด้วยลีลาของซินแสผู้ทรงภูมิ มีความหนักแน่น ชัดเจน และให้คำแนะนำที่สามารถนำไปปรับใช้ในชีวิตได้จริง"
        )

        chat_completion = openai.ChatCompletion.create(
            model="gpt-4o", # Upgraded to the latest model for best quality
            messages=[{"role": "user", "content": text_prompt}],
            request_timeout=60
        )
        text_fortune = chat_completion['choices'][0]['message']['content']
        
        return text_fortune

    except openai.error.AuthenticationError as e:
        return f"Authentication Error: The OpenAI API key is invalid or has expired. Please check your key. Details: {e}"
    except openai.error.APIError as e:
        return f"The AI oracle's API returned an error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {type(e).__name__} - {e}"


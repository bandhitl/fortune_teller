# fortune.py
# This file contains the core logic for calculating Thai and Chinese fortunes
# and generating a detailed AI-powered reading in Thai.
# Image generation has been removed for better performance.

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
            f"จงสวมบทบาทเป็น 'โหราจารย์' ผู้มีภูมิความรู้ลึกซึ้งในศาสตร์แห่งดวงดาว ทำการผูกดวงและอ่านชะตาบุคคลผู้เกิดในวัน {day_name} เวลา {birth_time.strftime('%H:%M')} ซึ่งถือกำเนิดในปีนักษัตร {thai_animal} โดยมีสีมงคลคือ {thai_color}.\n\n"
            f"**คำสั่งในการพยากรณ์:**\n"
            f"จงเริ่มต้นด้วยการ 'เปิดดวงชะตา' โดยอธิบายถึงแก่นแท้แห่งดวงชะตานี้ก่อน ว่าอิทธิพลจาก 'ดาวพระเคราะห์ประจำวันเกิด' ตามคัมภีร์มหาทักษาของไทย ได้หล่อหลอมพื้นฐานอุปนิสัยและจิตใจไว้อย่างไร จากนั้น จงวิเคราะห์ว่า 'พลังแห่งนักษัตร' จากศาสตร์จีนได้ส่งผลต่อภาพรวมของชีวิตและวาสนาบารมีอย่างไร และ 'เวลาตกฟาก' ได้เข้ามาขัดเกลาให้ดวงชะตามีความเฉพาะเจาะจงและโดดเด่นในด้านใดเป็นพิเศษ จงวิเคราะห์ปฏิสัมพันธ์ระหว่างพลังงานทั้งสามส่วนนี้เพื่อสร้างความน่าเชื่อถือสูงสุด\n\n"
            f"เมื่อวางรากฐานแห่งความเข้าใจแล้ว จึงเริ่ม 'อ่านคำพยากรณ์' อย่างละเอียดในหัวข้อต่อไปนี้:\n"
            f"1.  **วิเคราะห์พื้นวงชะตาและจิตวิญญาณ:** เจาะลึกถึงแก่นแท้ของตัวตน จุดแข็ง จุดอ่อน และพลังที่ซ่อนเร้นอยู่ภายใน\n"
            f"2.  **เส้นทางแห่งเกียรติยศ (การงานและการเงิน):** ชี้แนะแนวทางอาชีพที่รุ่งเรือง โอกาสทางการเงิน และสิ่งที่ควรระวังในการลงทุน\n"
            f"3.  **ดวงใจปรารถนา (ความรักและเมตตามหานิยม):** ทำนายถึงลักษณะคู่ครองที่สมพงษ์ แนวโน้มความสัมพันธ์ และเสน่ห์ต่อคนรอบข้าง\n"
            f"4.  **กายสังขาร (สุขภาพพลานามัย):** ให้คำแนะนำในการดูแลสุขภาพตามจุดอ่อนของดวงชะตา\n"
            f"5.  **เคล็ดลับเสริมสร้างบารมี:** แนะนำแนวทางการปฏิบัติหรือวัตถุมงคลที่ช่วยส่งเสริมดวงชะตาให้รุ่งโรจน์ยิ่งขึ้น\n\n"
            f"จงรจนาคำทำนายทั้งหมดเป็น **'ภาษาไทย'** ด้วยลีลาของนักปราชญ์ผู้สุขุม ลึกซึ้ง และเปี่ยมด้วยเมตตา เพื่อให้ผู้รับคำทำนายได้ทั้งสติปัญญาและกำลังใจในการดำเนินชีวิต"
        )

        chat_completion = openai.ChatCompletion.create(
            # Using a highly stable model to avoid server errors
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text_prompt}],
            request_timeout=60 # Set a timeout for resilience
        )
        text_fortune = chat_completion['choices'][0]['message']['content']
        
        return text_fortune

    except openai.error.AuthenticationError as e:
        return f"Authentication Error: The OpenAI API key is invalid or has expired. Please check your key. Details: {e}"
    except openai.error.APIError as e:
        return f"The AI oracle's API returned an error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {type(e).__name__} - {e}"


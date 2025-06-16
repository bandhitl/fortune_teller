# fortune.py
# This file contains the core logic for calculating Thai and Chinese fortunes
# and generating a detailed AI-powered reading and infographic in Thai.

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

def generate_ai_fortune_and_image(api_key, day_name, thai_color, thai_animal, english_animal, birth_time):
    """
    Generates a detailed fortune in Thai and a visual infographic.

    Args:
        api_key (str): The user's OpenAI API key.
        day_name (str): The day of the week of birth (English).
        thai_color (str): The lucky color (English).
        thai_animal (str): The Chinese zodiac animal (Thai).
        english_animal (str): The Chinese zodiac animal (English).
        birth_time (datetime.time): The user's time of birth.

    Returns:
        tuple: (A detailed, AI-generated fortune in Thai, URL for the infographic)
    """
    if not api_key:
        return "Error: OpenAI API key is missing.", None
    
    try:
        # --- Using Stable Library Version (v0.28.0) ---
        openai.api_key = api_key

        # --- 1. Generate Fortune Text in Thai ---
        text_prompt = (
            f"ทำตัวเป็นนักโหราศาสตร์ผู้เชี่ยวชาญที่ผสมผสานศาสตร์ไทยและจีนเข้าด้วยกัน "
            f"มีคนเกิดวัน {day_name} เวลา {birth_time.strftime('%H:%M')} สีนำโชคของเขาคือ {thai_color} และปีนักษัตรจีนของเขาคือ {thai_animal}. "
            f"โปรดทำนายดวงชะตาอย่างละเอียดและลึกซึ้งให้แก่บุคคลนี้ โดยครอบคลุมหัวข้อต่อไปนี้:\n\n"
            f"1.  **ภาพรวมและลักษณะนิสัย:** เจาะลึกถึงบุคลิกภาพ โดยผสมผสานลักษณะจากวันเกิด เวลาเกิด และปีนักษัตร\n"
            f"2.  **การงานและอาชีพ:** คำแนะนำเกี่ยวกับเส้นทางอาชีพที่เหมาะสมและจุดแข็งในการทำงาน\n"
            f"3.  **ความรักและความสัมพันธ์:** คำแนะนำเกี่ยวกับความรักและความเข้ากันได้กับผู้อื่น\n"
            f"4.  **สุขภาพ:** ข้อควรระวังและคำแนะนำด้านสุขภาพตามหลักโหราศาสตร์\n"
            f"5.  **วัตถุมงคลเสริมดวงประจำปี:** แนะนำวัตถุมงคลที่เรียบง่ายและเป็นสัญลักษณ์สำหรับปีนี้\n\n"
            f"**คำสั่งสำคัญ: โปรดเขียนคำตอบทั้งหมดเป็นภาษาไทยเท่านั้น** ใช้น้ำเสียงที่อบอุ่น ให้กำลังใจ และลึกซึ้ง"
        )

        chat_completion = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": text_prompt}]
        )
        text_fortune = chat_completion['choices'][0]['message']['content']

        # --- 2. Generate Infographic Image ---
        image_prompt = (
            f"Create a beautiful, mystical infographic for a Thai astrology reading. The subject's Chinese Zodiac animal is the {english_animal}. "
            f"Their lucky color is {thai_color}. The style should be elegant and modern with a magical feel, incorporating subtle Thai design motifs. "
            f"Visually feature the {english_animal} as the centerpiece. Use a color palette dominated by {thai_color}. "
            f"Do not include any text. Focus on abstract symbols representing luck, career, and love. High-resolution digital art."
        )
        
        image_response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size="1024x1024",
            model="dall-e-3" # Explicitly use DALL-E 3
        )
        image_url = image_response['data'][0]['url']
        
        return text_fortune, image_url

    except openai.error.AuthenticationError as e:
        return f"Authentication Error: The OpenAI API key is invalid or has expired. Please check your key. Details: {e}", None
    except openai.error.APIError as e:
        return f"The AI oracle's API returned an error: {e}", None
    except Exception as e:
        return f"An unexpected error occurred: {type(e).__name__} - {e}", None


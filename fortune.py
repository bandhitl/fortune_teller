# fortune.py
# This file contains the core logic for calculating Thai and Chinese fortunes
# and generating a detailed AI-powered reading.

import datetime
import os
import httpx
from openai import OpenAI

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
    zodiac_animals = [
        "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
        "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
    ]
    index = (year - 4) % 12
    return zodiac_animals[index]

def generate_ai_fortune(api_key, day_name, thai_color, animal_name, birth_time):
    """
    Generates a detailed fortune using the OpenAI API.

    Args:
        api_key (str): The user's OpenAI API key.
        day_name (str): The day of the week of birth.
        thai_color (str): The lucky color associated with the day.
        animal_name (str): The Chinese zodiac animal.
        birth_time (datetime.time): The user's time of birth.

    Returns:
        str: A detailed, AI-generated fortune, or an error message.
    """
    if not api_key:
        return "Error: OpenAI API key is missing. Please provide your API key to generate a fortune."
    
    try:
        # Conditionally initialize the client based on proxy environment variables
        # This is a robust way to handle environments like Render that may inject proxy settings.
        proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY")
        
        if proxy_url:
            # If a proxy is set in the environment, create an httpx client with it
            http_client = httpx.Client(proxies=proxy_url)
            client = OpenAI(api_key=api_key, http_client=http_client)
        else:
            # If no proxy is set, initialize the client normally
            client = OpenAI(api_key=api_key)


        # Construct a detailed prompt for the AI
        prompt = (
            f"Act as an expert astrologer combining Thai and Chinese traditions. "
            f"A person was born on a {day_name} at {birth_time.strftime('%H:%M')}. Their lucky color is {thai_color} and their Chinese Zodiac animal is the {animal_name}. "
            f"Please provide a detailed and insightful fortune for them, taking the specific time of birth into account for a more precise reading. Cover the following sections:\n\n"
            f"1.  **Personality Insight:** A deep dive into their character, blending traits from their birth day, time, and zodiac animal.\n"
            f"2.  **Career & Path:** Guidance on suitable career paths and their professional strengths.\n"
            f"3.  **Love & Relationships:** Advice on their approach to love and compatibility.\n"
            f"4.  **Health & Wellness:** Astrological insights into their well-being.\n"
            f"5.  **Lucky Charm for the Year:** Suggest a simple, symbolic lucky charm.\n\n"
            f"Write this in a warm, encouraging, and mystical tone. Use markdown for formatting."
        )

        # Make the API call
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4-turbo",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        # Provide a more detailed error message for easier debugging
        return f"An error occurred while communicating with the AI oracle: {type(e).__name__} - {e}"

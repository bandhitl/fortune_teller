# fortune.py
# This file contains the core logic for calculating Thai and Chinese fortunes.

import datetime
import os

try:
    import openai  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    openai = None


def get_thai_fortune(birth_date):
    """
    Calculates the Thai fortune based on the day of the week of birth.

    Args:
        birth_date (datetime.date): The user's date of birth.

    Returns:
        tuple: A tuple containing the day name, color, description, and a
        daily prediction.
    """
    # Determine the day of the week (Monday is 0 and Sunday is 6)
    day_index = birth_date.weekday()
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_name = days[day_index]

    thai_fortunes = {
        "Sunday": (
            "Red",
            "You are respectable, wise, and beloved by friends and family.",
        ),
        "Monday": ("Yellow", "You have a good memory, are serious, and enjoy travel."),
        "Tuesday": ("Pink", "You are brave, active, and have a broad mind."),
        "Wednesday": (
            "Green",
            "You are ambitious, fun-loving, and have good social skills.",
        ),
        "Thursday": ("Orange", "You are good-hearted, honest, and calm."),
        "Friday": (
            "Blue",
            "You are ambitious, fun-loving, and have a cheerful disposition.",
        ),
        "Saturday": ("Purple", "You are logical, confident, and a bit of a recluse."),
    }

    thai_predictions = {
        "Sunday": "A chance encounter will brighten your day.",
        "Monday": "Hard work pays off; stay focused on your tasks.",
        "Tuesday": "Today is ideal for pursuing personal goals.",
        "Wednesday": "Expect good news from a friend or colleague.",
        "Thursday": "Your generosity will open new doors.",
        "Friday": "A light-hearted conversation leads to inspiration.",
        "Saturday": "Take some time to relax and plan for the week ahead.",
    }

    color, description = thai_fortunes[day_name]
    prediction = thai_predictions[day_name]
    return day_name, color, description, prediction


def get_chinese_fortune(year):
    """
    Calculates the Chinese Zodiac animal based on the year of birth.

    Args:
        year (int): The user's year of birth.

    Returns:
        tuple: A tuple containing the zodiac animal name, its description,
        and a prediction for the upcoming days.
    """
    zodiac_animals = [
        ("Rat", "Intelligent, adaptable, quick-witted."),
        ("Ox", "Loyal, reliable, hardworking."),
        ("Tiger", "Brave, confident, competitive."),
        ("Rabbit", "Quiet, elegant, kind."),
        ("Dragon", "Confident, intelligent, enthusiastic."),
        ("Snake", "Enigmatic, intelligent, wise."),
        ("Horse", "Energetic, independent, impatient."),
        ("Goat", "Calm, gentle, creative."),
        ("Monkey", "Sharp, smart, curious."),
        ("Rooster", "Observant, hardworking, courageous."),
        ("Dog", "Loyal, honest, responsible."),
        ("Pig", "Compassionate, generous, diligent."),
    ]

    # The formula calculates the index for the zodiac_animals list
    index = (year - 4) % 12
    animal, description = zodiac_animals[index]

    chinese_predictions = {
        "Rat": "Financial luck is on your side.",
        "Ox": "Patience will lead you to success soon.",
        "Tiger": "An adventure awaits; be prepared.",
        "Rabbit": "Your kindness will be rewarded.",
        "Dragon": "A powerful opportunity approaches.",
        "Snake": "Trust your intuition today.",
        "Horse": "Energy is high; tackle new projects.",
        "Goat": "Creativity will help solve a problem.",
        "Monkey": "Your wit attracts helpful allies.",
        "Rooster": "Stay organized to avoid mishaps.",
        "Dog": "Loyalty from friends brings comfort.",
        "Pig": "Generosity opens unexpected doors.",
    }

    prediction = chinese_predictions[animal]
    return animal, description, prediction


def generate_fortune_text(birth_date: datetime.date, birth_time: datetime.time) -> str:
    """Generate a combined fortune text using optional OpenAI API."""

    day_name, color, thai_desc, thai_pred = get_thai_fortune(birth_date)
    animal, chinese_desc, chinese_pred = get_chinese_fortune(birth_date.year)

    prompt = (
        "Based on Thai astrology and Chinese zodiac, give a short prediction. "
        f"Day: {day_name} ({color}) - {thai_desc}. Thai prediction: {thai_pred}. "
        f"Zodiac: {animal} - {chinese_desc}. Chinese prediction: {chinese_pred}. "
        f"Birth time: {birth_time.strftime('%H:%M')}."
    )

    if openai and os.getenv("OPENAI_API_KEY"):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content.strip()
        except Exception:
            pass

    return (
        f"{thai_pred} As a {animal}, {chinese_pred} "
        "Your combined signs point to a positive outlook."
    )


def main():
    """
    Main function to run the command-line version of the fortune teller.
    """
    print("Welcome to the Thai-Chinese Fortune Teller!")

    while True:
        date_str = input("Please enter your date of birth (DD/MM/YYYY): ")
        try:
            # Attempt to parse the input string into a datetime object
            day, month, year = map(int, date_str.split("/"))
            birth_date = datetime.date(year, month, day)
            break  # Exit loop if date is valid
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")

    while True:
        time_str = input("Please enter your time of birth (HH:MM, 24h): ")
        try:
            hour, minute = map(int, time_str.split(":"))
            birth_time = datetime.time(hour, minute)
            break
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

    print("\n--- Your Fortune ---")

    # Get and display Thai fortune
    day_name, color, thai_desc, thai_pred = get_thai_fortune(birth_date)
    print("\n[THAI]")
    print(f"You were born on a {day_name} at {birth_time.strftime('%H:%M')}.")
    print(f"Your color is {color}, and {thai_desc}")
    print(f"Prediction: {thai_pred}")

    # Get and display Chinese fortune
    animal, chinese_desc, chinese_pred = get_chinese_fortune(birth_date.year)
    print("\n[CHINESE]")
    print(f"Your Chinese Zodiac animal is the {animal}.")
    print(f"You are known for being {chinese_desc}")
    print(f"Prediction: {chinese_pred}")

    print("\n[Combined Prediction]")
    print(generate_fortune_text(birth_date, birth_time))


if __name__ == "__main__":
    main()

# fortune.py
# This file contains the core logic for calculating Thai and Chinese fortunes.

import datetime


def get_thai_fortune(birth_date):
    """
    Calculates the Thai fortune based on the day of the week of birth.

    Args:
        birth_date (datetime.date): The user's date of birth.

    Returns:
        tuple: A tuple containing the day name, color, and description.
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

    color, description = thai_fortunes[day_name]
    return day_name, color, description


def get_chinese_fortune(year):
    """
    Calculates the Chinese Zodiac animal based on the year of birth.

    Args:
        year (int): The user's year of birth.

    Returns:
        tuple: A tuple containing the zodiac animal name and its description.
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
    return animal, description


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

    print("\n--- Your Fortune ---")

    # Get and display Thai fortune
    day_name, color, thai_desc = get_thai_fortune(birth_date)
    print("\n[THAI]")
    print(f"You were born on a {day_name}.")
    print(f"Your color is {color}, and {thai_desc}")

    # Get and display Chinese fortune
    animal, chinese_desc = get_chinese_fortune(birth_date.year)
    print("\n[CHINESE]")
    print(f"Your Chinese Zodiac animal is the {animal}.")
    print(f"You are known for being {chinese_desc}")


if __name__ == "__main__":
    main()

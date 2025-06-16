# Fortune telling service for Thai and Chinese traditions

THAI_FORTUNES = {
    'monday':    ('yellow', 'intelligent and charming'),
    'tuesday':   ('pink',   'confident and competitive'),
    'wednesday': ('green',  'creative and thoughtful'),
    'thursday':  ('orange', 'generous and wise'),
    'friday':    ('blue',   'sociable and fun-loving'),
    'saturday':  ('purple', 'strong and independent'),
    'sunday':    ('red',    'energetic and decisive'),
}

ZODIAC_ANIMALS = [
    'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
    'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'
]

ZODIAC_TRAITS = {
    'Rat': 'resourceful and quick-witted',
    'Ox': 'reliable and determined',
    'Tiger': 'brave and confident',
    'Rabbit': 'gentle and compassionate',
    'Dragon': 'ambitious and energetic',
    'Snake': 'wise and enigmatic',
    'Horse': 'active and free-spirited',
    'Goat': 'calm and gentle',
    'Monkey': 'clever and curious',
    'Rooster': 'hardworking and observant',
    'Dog': 'loyal and honest',
    'Pig': 'generous and diligent',
}

def get_thai_fortune(day: str):
    day_key = day.strip().lower()
    return THAI_FORTUNES.get(day_key, (None, None))


def get_chinese_zodiac(year: int):
    index = (year - 1900) % 12
    animal = ZODIAC_ANIMALS[index]
    trait = ZODIAC_TRAITS[animal]
    return animal, trait


def main():
    day = input('Enter the day of the week you were born: ')
    year_input = input('Enter the year you were born: ')
    try:
        year = int(year_input)
    except ValueError:
        print('Invalid year provided.')
        return

    color, thai_trait = get_thai_fortune(day)
    if color is None:
        print('Unknown day of the week provided.')
        return

    animal, zodiac_trait = get_chinese_zodiac(year)

    print('\nThai Fortune')
    print('------------')
    print(f'Day: {day.strip().title()}')
    print(f'Lucky Color: {color.title()}')
    print(f'Traits: {thai_trait}')

    print('\nChinese Fortune')
    print('---------------')
    print(f'Zodiac Animal: {animal}')
    print(f'Traits: {zodiac_trait}')


if __name__ == '__main__':
    main()

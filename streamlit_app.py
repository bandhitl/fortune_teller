import streamlit as st
from fortune import get_thai_fortune, get_chinese_zodiac, THAI_FORTUNES

st.title('Fortune Teller')

# Select day of the week
choices = [day.title() for day in THAI_FORTUNES.keys()]
day = st.selectbox('Day of the week you were born:', choices)

# Input for birth year
year = st.number_input('Year you were born:', min_value=1900, max_value=2100, step=1)

if st.button('Tell my fortune'):
    color, thai_trait = get_thai_fortune(day)
    animal, zodiac_trait = get_chinese_zodiac(int(year))

    st.subheader('Thai Fortune')
    st.write(f'Day: {day}')
    st.write(f'Lucky Color: {color.title()}')
    st.write(f'Traits: {thai_trait}')

    st.subheader('Chinese Fortune')
    st.write(f'Zodiac Animal: {animal}')
    st.write(f'Traits: {zodiac_trait}')

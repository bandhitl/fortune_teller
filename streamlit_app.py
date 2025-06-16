# streamlit_app.py
# This file creates a web application interface for the fortune teller.

import datetime

import streamlit as st  # type: ignore

from fortune import get_chinese_fortune, get_thai_fortune

# --- Page Configuration ---
st.set_page_config(
    page_title="Thai-Chinese Fortune Teller", page_icon="🔮", layout="centered"
)

# --- Application UI ---
st.title("🔮 Thai-Chinese Fortune Teller")
st.write("Discover your destiny based on ancient wisdom. Enter your birth date below.")

# --- User Input ---
# Set default date to 20 years ago to make it easier for users
default_date = datetime.date.today() - datetime.timedelta(days=365 * 20)
birth_date = st.date_input(
    "Enter your date of birth:",
    default_date,
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today(),
)

# --- Fortune Calculation and Display ---
if st.button("✨ Tell My Fortune"):
    if birth_date:
        # Get Thai Fortune
        day_name, color, thai_desc = get_thai_fortune(birth_date)

        # Get Chinese Fortune
        animal, chinese_desc = get_chinese_fortune(birth_date.year)

        st.balloons()
        st.success("Your fortune has been revealed!")

        # --- Display Results ---
        st.subheader("🇹🇭 Your Thai Fortune (from Day of Birth)")
        col1, col2 = st.columns([1, 4])
        with col1:
            st.metric(label="Your Day", value=day_name)
            st.metric(label="Your Color", value=color)
        with col2:
            st.write("**Personality Trait:**")
            st.info(thai_desc)

        st.subheader("🇨🇳 Your Chinese Fortune (from Year of Birth)")
        col3, col4 = st.columns([1, 4])
        with col3:
            st.metric(label="Your Animal", value=animal)
        with col4:
            st.write("**Personality Trait:**")
            st.info(chinese_desc)
    else:
        st.error("Please enter a valid date.")

# --- Footer ---
st.markdown("---")
st.markdown("_Created with a blend of tradition and technology._")

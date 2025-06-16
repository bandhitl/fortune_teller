# streamlit_app.py
# This file creates a production-ready web application that securely uses
# an API key from the server's environment variables (e.g., on Render).

import streamlit as st
import datetime
import os # Import the 'os' module to access environment variables
from fortune import get_thai_fortune_details, get_chinese_fortune_details, generate_ai_fortune

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Thai-Chinese Fortune Teller",
    page_icon="✨",
    layout="wide"
)

# --- Securely Get API Key ---
# This line reads the 'OPENAI_API_KEY' from the environment variables
# that you set in your Render dashboard.
api_key = os.environ.get("OPENAI_API_KEY")

# --- Application UI ---
st.title("✨ AI Thai-Chinese Fortune Teller")
st.markdown("Unlock the secrets of your destiny by combining ancient wisdom with modern AI. Provide your birth date and time for a personalized reading.")

# --- Sidebar for Inputs ---
st.sidebar.header("Your Details")

# Date of Birth Input
default_date = datetime.date.today() - datetime.timedelta(days=365*25)
birth_date = st.sidebar.date_input(
    "Enter your date of birth:",
    default_date,
    min_value=datetime.date(1920, 1, 1),
    max_value=datetime.date.today()
)

# Time of Birth Input
birth_time = st.sidebar.time_input(
    "Enter your time of birth (optional):",
    datetime.time(12, 00)
)


# --- Fortune Button and Logic ---
if st.sidebar.button("🔮 Reveal My AI Fortune"):
    # Check if the API key was found in the environment
    if not api_key:
        st.error("Configuration Error: The OpenAI API key is not set on the server. The administrator needs to set the OPENAI_API_KEY environment variable.")
    elif not birth_date:
        st.error("Please enter your date of birth.")
    else:
        st.balloons()
        with st.spinner("Consulting the celestial AI oracles... This may take a moment."):
            # 1. Get the basic astrological details
            day_name, thai_color = get_thai_fortune_details(birth_date)
            animal_name = get_chinese_fortune_details(birth_date.year)
            
            # 2. Generate the AI fortune, now including the birth time
            ai_fortune = generate_ai_fortune(api_key, day_name, thai_color, animal_name, birth_time)
            
            # 3. Display the results
            st.subheader("📜 Your Personalized Astrological Reading")
            st.info(f"Based on being born on a **{day_name}** at **{birth_time.strftime('%H:%M')}**, with a Zodiac sign of the **{animal_name}**.")
            st.markdown("---")
            st.markdown(ai_fortune)

st.markdown("---")
st.markdown("### About This App")
st.markdown("This fortune teller combines Thai and Chinese astrological traditions with the power of AI to create a unique and insightful reading just for you.")

# my_portfolio.py

import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")
st.title("👨‍💻 My Portfolio Website")
st.subheader("Made with Streamlit")

st.header("💼 About Me")
st.write("Hi! I'm learning Python and building Streamlit apps as projects.")

st.header("📂 Projects")
st.markdown("""
- 📝 Mad Libs
- 🎯 Guess the Number
- ✊ Rock Paper Scissors
- 🪓 Hangman
- ⏱ Countdown Timer
- 🔐 Password Generator
- ⚖️ BMI Calculator
""")

st.header("📧 Contact")
st.write("Email: your.email@example.com")
st.success("Thanks for visiting!")

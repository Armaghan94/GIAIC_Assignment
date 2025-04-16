# guess_number_user.py

import streamlit as st
import random

st.title("🎯 Guess the Number Game")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.warning("Too low!")
    elif guess > st.session_state.number:
        st.warning("Too high!")
    else:
        st.success(f"Correct! You guessed it in {st.session_state.attempts} tries.")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0

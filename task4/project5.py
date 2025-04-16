# hangman_game.py

import streamlit as st
import random

st.title("🪓 Hangman Game")

words = ['python', 'streamlit', 'developer', 'challenge']

if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.display = ['_'] * len(st.session_state.word)
    st.session_state.tries = 6
    st.session_state.guessed = []

letter = st.text_input("Guess a letter:")

if st.button("Submit"):
    if letter and letter not in st.session_state.guessed:
        st.session_state.guessed.append(letter)
        if letter in st.session_state.word:
            for i, char in enumerate(st.session_state.word):
                if char == letter:
                    st.session_state.display[i] = letter
        else:
            st.session_state.tries -= 1

    st.write("Word: " + ' '.join(st.session_state.display))
    st.write(f"Tries left: {st.session_state.tries}")

    if '_' not in st.session_state.display:
        st.success(f"Congratulations! You guessed the word: {st.session_state.word}")
    elif st.session_state.tries <= 0:
        st.error(f"You lost! The word was: {st.session_state.word}")
        if st.button("Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]

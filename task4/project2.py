# guess_number_computer.py

import streamlit as st

st.title("🧠 Computer Guesses Your Number")

st.write("Think of a number between 1 and 100. Let the computer guess it!")

if 'low' not in st.session_state:
    st.session_state.low = 1
if 'high' not in st.session_state:
    st.session_state.high = 100

if st.button("Start Guessing"):
    st.session_state.low = 1
    st.session_state.high = 100

if st.session_state.high >= st.session_state.low:
    guess = (st.session_state.low + st.session_state.high) // 2
    st.write(f"Is your number {guess}?")
    col1, col2, col3 = st.columns(3)
    if col1.button("Too Low"):
        st.session_state.low = guess + 1
    elif col2.button("Correct"):
        st.success(f"Yay! I guessed your number: {guess}")
    elif col3.button("Too High"):
        st.session_state.high = guess - 1

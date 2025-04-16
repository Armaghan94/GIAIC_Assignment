# rock_paper_scissors.py

import streamlit as st
import random

st.title("✊ Rock, 🖐️ Paper, ✌️ Scissors")

user = st.selectbox("Choose your move:", ['rock', 'paper', 'scissors'])
computer = random.choice(['rock', 'paper', 'scissors'])

if st.button("Play"):
    st.write(f"Computer chose: **{computer}**")
    if user == computer:
        st.info("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        st.success("You win!")
    else:
        st.error("You lose!")

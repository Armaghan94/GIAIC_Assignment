# countdown_timer.py

import streamlit as st
import time

st.title("⏳ Countdown Timer")

minutes = st.number_input("Enter time in minutes:", min_value=1)
start = st.button("Start Timer")

if start:
    total_seconds = int(minutes * 60)
    with st.empty():
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            st.write(f"⏱ {mins:02d}:{secs:02d}")
            time.sleep(1)
        st.success("Time's up!")

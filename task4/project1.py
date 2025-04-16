#Mad Libs – Streamlit

import streamlit as st

st.title("📝 Mad Libs Generator")

st.write("Fill in the blanks below to generate your funny story!")

adj = st.text_input("Enter an adjective:")
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
place = st.text_input("Enter a place:")

if st.button("Generate Story"):
    if adj and noun and verb and place:
        story = f"Today I went to the {place} and saw a very {adj} {noun} trying to {verb}!"
        st.success("Here's your story:")
        st.write(story)
    else:
        st.warning("Please fill in all fields.")

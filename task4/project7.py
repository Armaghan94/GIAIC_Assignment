# password_generator.py

import streamlit as st
import random
import string

st.title("🔐 Password Generator")

length = st.slider("Select password length:", 6, 50, 12)

if st.button("Generate Password"):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    st.success(f"Generated password: `{password}`")

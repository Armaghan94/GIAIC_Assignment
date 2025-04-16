import streamlit as st
import re
import random

# Common weak passwords
blacklist = ["password", "123456", "password123", "qwerty", "letmein", "admin"]
special_chars = "!@#$%^&*"

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ This password is too common.")
        return score, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Minimum 8 characters required.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number.")

    if re.search(f"[{re.escape(special_chars)}]", password):
        score += 1
    else:
        feedback.append(f"❌ Add special character ({special_chars}).")

    return score, feedback

def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = special_chars

    base = (
        random.choice(lower) +
        random.choice(upper) +
        random.choice(digits) +
        random.choice(symbols)
    )
    all_chars = lower + upper + digits + symbols
    base += ''.join(random.choice(all_chars) for _ in range(8))
    return ''.join(random.sample(base, len(base)))

# Streamlit App
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password")
    else:
        st.error("❌ Weak Password")



    st.markdown("---")
    if st.button("Suggest Strong Password"):
        st.code(generate_password(), language="text")

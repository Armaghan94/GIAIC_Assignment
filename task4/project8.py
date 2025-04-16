# bmi_calculator.py

import streamlit as st

st.title("⚖️ BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (cm):", min_value=1.0)

if weight and height:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")

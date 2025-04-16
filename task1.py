import streamlit as st

# Title and Description
st.title("Google Style Unit Converter")
st.subheader("Length Conversion")

# Supported units
units = {
    "Metre": 1,
    "Centimetre": 100,
    "Kilometre": 0.001,
    "Millimetre": 1000,
    "Inch": 39.3701,
    "Foot": 3.28084,
    "Yard": 1.09361,
    "Mile": 0.000621371
}

# Dropdowns
input_unit = st.selectbox("From", units.keys(), index=0)
output_unit = st.selectbox("To", units.keys(), index=1)

# Input value
input_value = st.number_input("Enter value", min_value=0.0, value=1.0)

# Conversion Logic
converted_value = input_value * (units[output_unit] / units[input_unit])

# Display result
st.markdown(f"### {input_value} {input_unit} = {converted_value:.4f} {output_unit}")

# Formula display (only for metre to cm like image)
if input_unit == "Metre" and output_unit == "Centimetre":
    st.markdown("📘 **Formula**: multiply the length value by 100")

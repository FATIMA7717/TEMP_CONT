import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app title
st.title("Temperature Converter")

# Choose conversion type
conversion_type = st.radio("Select Conversion Type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input temperature and perform conversion based on selected option
if conversion_type == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:")
    if st.button("Convert"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius}°C is equal to {fahrenheit}°F")

elif conversion_type == "Fahrenheit to Celsius":
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:")
    if st.button("Convert"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.write(f"{fahrenheit}°F is equal to {celsius}°C")

st.markdown("- Click the **Convert** button to see your results instantly!")

st.caption("Created with ❤️ using Streamlit")


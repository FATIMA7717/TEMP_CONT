import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Set a more interactive app title with emojis
st.title("🌡️ Temperature Converter")

# Add a subheader for user guidance
st.subheader("Convert temperatures easily between Celsius and Fahrenheit!")

# Choose conversion type with a better description
conversion_type = st.radio(
    "Select the conversion type you want to perform:",
    ("🌡️ Celsius to Fahrenheit", "🌡️ Fahrenheit to Celsius")
)

# Input temperature and perform conversion based on selected option
if conversion_type == "🌡️ Celsius to Fahrenheit":
    st.info("Enter the temperature in Celsius and click 'Convert' to see the result.")
    celsius = st.slider("Select temperature in Celsius:", min_value=-100, max_value=100, value=0)
    if st.button("Convert"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"✅ {celsius}°C is equal to {fahrenheit:.2f}°F")

elif conversion_type == "🌡️ Fahrenheit to Celsius":
    st.info("Enter the temperature in Fahrenheit and click 'Convert' to see the result.")
    fahrenheit = st.slider("Select temperature in Fahrenheit:", min_value=-150, max_value=212, value=32)
    if st.button("Convert"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"✅ {fahrenheit}°F is equal to {celsius:.2f}°C")

# Add a footer or extra information
st.markdown("### 🌟 Tips:")
st.markdown("- Use the slider for an interactive input experience.")
st.markdown("- Click the **Convert** button to see your results instantly!")

st.caption("Created with ❤️ using Streamlit")


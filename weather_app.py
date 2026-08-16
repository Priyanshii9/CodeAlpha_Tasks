import streamlit as st
import requests

# Apna API key yahan paste karo
API_KEY = "eaad99879efd6546fadca7382207cd65"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# App Title
st.title("🌤 Weather App")

# User input
city = st.text_input("Enter city name:")

if city:
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather = data['weather'][0]['description']

        # Output
        st.subheader(f"Weather in {city}")
        st.write(f"**Temperature:** {temperature} °C")
        st.write(f"**Humidity:** {humidity} %")
        st.write(f"**Pressure:** {pressure} hPa")
        st.write(f"**Condition:** {weather}")
    else:
        st.error("City not found or API error!")

# 🌦️ My Weather API App 🌟

## Table of Contents 📚
- [Overview](#overview-)
- [Features](#features-)
- [Prerequisites](#prerequisites-)
- [Installation](#installation-)
- [Setup](#setup-)
- [Usage](#usage-)
- [How It Works](#how-it-works-)
- [Code Explanation](#code-ecplanation-)
- [Troubleshootings](#troubleshootings-)
- [Acknowledgments](#acknowledgments-)

## Overview 📋

My Weather App is a user-friendly weather application created with Python's Tkinter library and powered by the [OpenWeatherMap](https://openweathermap.org/) API. 🎉 This app lets you select a city from a list of Indian states and displays current weather conditions including climate, description, temperature, and pressure. 🌍<br>

## Features 📄

◻️ Select a city from a dropdown list.<br>
◻️ Fetch and display current weather conditions.<br>
◻️ Show weather climate, description, temperature (in Celsius), and pressure.<br>

## Prerequisites ⚙️

◻️ Python 3.x<br>
◻️ *'requests'* library (for making API requests)<br>
◻️ tkinter library (comes with Python standard library)<br>.

## Installation 📥

1. **Clone the Repository**<br>

       git clone https://github.com/YuiSurbhi/Weather-API.git
       cd Weather-API

2. **Install Required Libraries**<br>

   Ensure you have the *'requests'* library installed. You can install it using pip:<br>

        pip install requests

3. **Get Your API Key**<br>

   ◻️ Sign up at [OpenWeatherMap](https://openweathermap.org/) and get a free API key. Replace the placeholder API key in the *'data_get'* function with your actual API key.<br>

## Setup 🛠️

1. **OpenWeatherMap API Key:** The application uses the OpenWeatherMap API to fetch weather data. You need an API key to use this service. Obtain your API key from OpenWeatherMap.<br>

2. **Update API Key in Code:** Replace *'02d85d9f3247243a3d39d1d24c7976b9'* in the code with your actual API key.<br>
  
       data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=02d85d9f3247243a3d39d1d24c7976b9").json()

## Usage 🚀

1. **Run the Application**<br>

   Execute the script using Python:<br>

        python weather_app.py

2. **Interact with the GUI**<br>

   ◻️ Choose a city from the dropdown list.<br>
   
   ◻️ Click the "Done" button to fetch and display the weather data.<br>

3. **Output**
   The application displays:<br>

   ◻️ **Weather Climate:** General weather condition (e.g., Clear, Cloudy). ☀️🌥️<br>
   ◻️ **Weather Description:** Detailed description of the weather (e.g., clear sky, light rain). 🌧️<br>
   ◻️ **Temperature:** Current temperature in Celsius. 🌡️<br>
   ◻️ **Pressure:** Atmospheric pressure in hPa. 🌬️<br>

## How It Works 🧩

◻️ **City Selection:** Choose a city from the dropdown list.<br>
◻️ **Fetch Weather Data:** Click the "Done" button to get weather details.<br>
◻️ **Display Results:** Weather, description, temperature, and pressure are displayed on the interface.<br>

## Code Explanation 📜

  ### Main Components
***'data_get'* Function:** Triggered by the "Done" button. It sends a request to the OpenWeatherMap API and updates the GUI with the weather data. 🔄<br>

 **GUI Elements:**

  ◻️ *'Label':* Displays text such as weather conditions, description, temperature, and pressure. 🖼️<br>
  ◻️ *'ttk.Combobox':* Dropdown menu for city selection. 🗂️<br>
  ◻️ *'Button':* Executes the data_get function when clicked. 🖱️<br>

### Code Overview 🛠️

◻️ ***'data_get()'* Function:** Fetches weather data using the OpenWeatherMap API and updates the labels with the fetched data.<br>
◻️ **Tkinter Widgets:** Used to create the GUI elements such as labels, buttons, and dropdown menus.<br>

## Troubleshooting ⚠️

◻️ **No Data Displayed:** Verify that the API key is correct and the city name is accurate. 🧐<br>
◻️ **Library Issues:** Ensure all required libraries are installed. Install missing libraries using pip. ⚠️<br>
◻️ **Internet Connection:** Check your internet connection as the app needs network access. 🌐<br>

## Acknowledgments 🌟   

◻️ **Tkinter:** For the graphical user interface.<br>
◻️ **OpenWeatherMap:** For providing weather data.<br> 

---

Enjoy using the My Weather App! ☀️🌧️

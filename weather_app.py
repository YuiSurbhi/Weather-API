from tkinter import *
from tkinter import ttk
import requests

# Function to fetch Weather Data and update the labels
def data_get():
    # Get the city name from the combobox
    city = city_name.get()

    # Make a request to OpenWeatherMap API with the city name
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=02d85d9f3247243a3d39d1d24c7976b9").json()

    # Update the weather climate label
    w_label1.config(text=data["weather"][0]["main"])

    # Update the weather description label
    wb_label1.config(text=data["weather"][0]["description"])

    # Updae the temprature label (converted from Kelvin to Celsius)
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))

    # Update the pressure label
    per_label1.config(text=data["main"]["pressure"])

# Creating main application window
win = Tk()
win.title("YuiSurbhi")      # Set the title of the window
win.config(bg = "dark blue")       # Set the background color of the window
win.geometry("500x570")      # Set the dimension of the window

# Create and place label for the application title
name_label = Label(win, text = "My Weather App",
                   font = ("Helvetica", 30, "bold" ))
name_label.place(x=25, y=50, height=50, width=450)

# Create the StringVar to hold the selected city names
city_name = StringVar()

# List of city names (state names) from the combobox
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","National Capital Territory of Delhi","Puducherry"]

# Create and place a combobox for selecting the city 
com = ttk.Combobox(win, text = "My Weather App", values = list_name,
                   font = ("Helvetica", 20, "bold" ), textvariable = city_name)
com.place(x=25, y=120, height=50, width=450)

# Create and place label for weather climate
w_label = Label(win, text = "Weather Climate",
           font = ("Helvetica", 20))
w_label.place(x=25, y= 260, height=50, width=210)

# Create and place label to display weather climate information
w_label1 = Label(win, text = "",
           font = ("Helvetica", 20))
w_label1.place(x=250, y= 260, height=50, width=210)

# Create and place label for weather description
wb_label = Label(win, text = "Weather Description",
           font = ("Helvetica", 17))
wb_label.place(x=25, y= 330, height=50, width=210)

# Create and place label to display weather description information
wb_label1 = Label(win, text = "",
           font = ("Helvetica", 17))
wb_label1.place(x=250, y= 330, height=50, width=210)

# Create and place label for temperature
temp_label = Label(win, text = "Temperature",
           font = ("Helvetica", 20))
temp_label.place(x=25, y= 400, height=50, width=210)

# create and place label to display temperature information
temp_label1 = Label(win, text = "",
           font = ("Helvetica", 20))
temp_label1.place(x=250, y= 400, height=50, width=210)

# Create and place label for pressure
per_label = Label(win, text = "Pressure",
           font = ("Helvetica", 20))
per_label.place(x=25, y= 470, height=50, width=210)

# create and place label to display pressure information
per_label1 = Label(win, text = "",
           font = ("Helvetica", 20))
per_label1.place(x=250, y= 470, height=50, width=210)

# Create and place a button to fetch Weather Data
done_button = Button(win, text = "Done",
                     font = ("Helvetica", 20, "bold" ), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

# Start the Tkinter event loop
win.mainloop()

import tkinter
from tkinter import *
import requests
import customtkinter
from pytube import YouTube
from datetime import datetime






# System settings
customtkinter.set_appearance_mode("blue")
customtkinter.set_default_color_theme("blue")

# app frame

root = customtkinter.CTk()
root.geometry("400x400")  # size of the window by default
root.resizable(0, 0)  # to make the window size fixed
root.config(background="#89cff0")

#Icon



# title of our window

root.title('Aplicatie vreme - Badea Andrei')

# ----------------------Functions to fetch and display weather info
city_value = StringVar()


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_value = StringVar()


def showWeather():
    # Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "HIDDEN"  # sample API

    # Get city name from user from the input field (later in the code)
    city_name = city_value.get()

    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

    # Get the response from fetched url
    response = requests.get(weather_url)

    # changing response from json to python readable
    weather_info = response.json()

    tfield.delete("1.0", "end")  # to clear the text field for every new output

    # as per API documentation, if the cod is 200, it means that weather data was successfully fetched

    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

        # -----------Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        # assigning Values to our weather varaible, to display as output

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)  # to insert or send value in our Text Field to display output


# ------------------------------Frontend part of code - Interface

# city_head = customtkinter.CTkLabel(Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10))
city_frame = customtkinter.CTkFrame(master=root,corner_radius=25,bg_color="#89cff0")
city_frame.pack(pady=20, padx=60, fill="both", expand="false")
city_label = customtkinter.CTkLabel(master=city_frame, text='Enter city name',corner_radius=25, font=("Roboto", 24))
city_label.pack(pady=12, padx=10)

city_tb = customtkinter.CTkEntry(master=city_frame, textvariable=city_value,corner_radius=16, width=200,height=25).pack(pady=10)
button = customtkinter.CTkButton(master=city_frame, command=showWeather, text="Check Weather",corner_radius=20, width=200, height=40).pack(pady=10)


# to show output
weather_label = customtkinter.CTkLabel(master=city_frame, text=None, font=("Roboto", 10))


tfield = Text(root, width=85, height=10,background="#D3D3D3")
tfield.pack()

root.mainloop()

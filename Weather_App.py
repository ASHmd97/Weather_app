import requests
import tkinter as tk
from tkinter import ttk, messagebox

def weather_app():
    # Get the country name from the entry widget
    get_country = country_entry.get()

    # Check if a country name is entered
    if not get_country:
        messagebox.showwarning("Warning", "Please enter a country name.")
        return

    try:
        # Fetch geographical information for the country
        response_geocoding = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={get_country}&limit=5&appid=a4fa82eb10c9fd862bcdaf4edd3e4f35")
        location = response_geocoding.json()

        # Extract some geographical information
        name = location[0]["name"]
        lat = location[0]["lat"]
        lon = location[0]["lon"]
        country = location[0]["country"]
        state = location[0]["state"]

        # Fetch weather information using the coordinates
        response_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid=a4fa82eb10c9fd862bcdaf4edd3e4f35")
        open_weather = response_weather.json()

        # Extract some weather information
        weather_status = open_weather["weather"][0]["main"]
        temp = open_weather["main"]["temp"]
        pressure = open_weather["main"]["pressure"]
        humidity = open_weather["main"]["humidity"]
        wind_speed = open_weather["wind"]["speed"]

        # Update labels with the new data
        weather_status_label.config(text=f"Weather status:    {weather_status}")
        temp_label.config(text=f"temp   :    {temp} Celsius")
        pressure_label.config(text=f"pressure   :    {pressure} hpa")
        humidity_label.config(text=f"humidity   :    {humidity} %")
        wind_speed_label.config(text=f"wind_speed   :    {wind_speed} meter/sec")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    except (IndexError, KeyError) as e:
        messagebox.showerror("Error", f"Error parsing API response: {e}")

# Set up the user interface
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")

frame = ttk.Frame(app, padding=20)
frame.grid(row=0, column=0)

country_label = ttk.Label(frame, text="Country")
country_label.grid(row=0, column=0)

country_entry = ttk.Entry(frame, width=40)
country_entry.grid(row=0, column=1, columnspan=2, padx=10)

get_weather_button = ttk.Button(frame, text="Get Weather", command=weather_app)
get_weather_button.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

# Set default values for labels
weather_status_label = ttk.Label(frame, text="Weather status: N/A")
weather_status_label.grid(row=2, column=0, columnspan=3, pady=10)

temp_label = ttk.Label(frame, text="Temperature: N/A")
temp_label.grid(row=3, column=0, columnspan=3, pady=10)

pressure_label = ttk.Label(frame, text="Pressure: N/A")
pressure_label.grid(row=4, column=0, columnspan=3, pady=10)

humidity_label = ttk.Label(frame, text="Humidity: N/A")
humidity_label.grid(row=5, column=0, columnspan=3, pady=10)

wind_speed_label = ttk.Label(frame, text="Wind Speed: N/A")
wind_speed_label.grid(row=6, column=0, columnspan=3)

app.mainloop()

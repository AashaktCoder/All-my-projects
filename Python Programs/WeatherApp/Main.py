from tkinter import *
import requests
from geopy.geocoders import Nominatim

WIN = Tk()
WIN.geometry("350x150")
WIN.maxsize(350, 150)
WIN.minsize(350, 150)
WIN.title("Weather App By Aashakt")

StartScreen = Canvas(WIN)
StartScreen.place(x=0, y=0)

ShowScreen = Canvas(WIN)
ShowScreen.pack_forget()

LocLabel = Label(StartScreen, text="Location:", font="Aerial 16")
LocLabel.place(x=20, y=20)

Location = ""

LocationVal = StringVar()
LocationE = Entry(StartScreen, textvariable=LocationVal, width=16, font="Aerial 16")
LocationE.place(x=130, y=22)

def GetLocation(Location):
    Location = LocationVal.get()
    loc = Nominatim(user_agent='GetLoc')

    getLoc = loc.geocode(f"{Location}")

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={getLoc.latitude}&longitude={getLoc.longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")

    Temperature = response.json()['current_weather']['temperature']

    ShowScreen.pack()

    TempLabel = Label(ShowScreen, text=f"Temperature of {Location} is {Temperature}")
    TempLabel.place(x=0, y=0)

    AgainButton = Button(ShowScreen, text="Again", command=lambda: ShowScreen.pack_forget())
    AgainButton.place(x=20, y=20)

LocationButton = Button(StartScreen, text="Submit", command=lambda:GetLocation(Location), font="Aerial 18")
LocationButton.place(x=125, y=80)

WIN.mainloop()
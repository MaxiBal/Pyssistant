from gtts import gTTS
from playsound import playsound
import pyowm
import os
def getWeather(place):
    owm = pyowm.OWM('XXXXXXXXXXXXXXXXXXXXXX') #Open Weather Map API Key
    observation = owm.weather_at_place(place)
    w = str(observation.get_weather()).strip("<").strip(">").replace("pyowm.webapi25.weather.Weather - reference time=", "").replace(":00+00, status=", "")
    w2 = observation.get_weather()
    temperature = str(w2.get_temperature('celsius')).strip("{").strip("}")
    finalWeather = w + temperature
    finalWeather = finalWeather.replace(finalWeather[:28], "")
    finalWeather = finalWeather.replace(finalWeather[:-52], "")
    audioFile = gTTS(text=finalWeather, lang="en")
    audioFile.save("weatherReport.mp3")
    playsound("weatherReport.mp3")
    print(finalWeather)

def notFound():
    audioFile = gTTS(text="Sorry, but this location could not be found", lang="en")
    audioFile.save("weatherLocationNotFound.mp3")
    playsound("weatherLocationNotFound.mp3")

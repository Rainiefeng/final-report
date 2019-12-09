
import requests



key = "219b74026949c164fc504f625a7b805c"
url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = url + "appid=" + key + "&q=" + city_name
response = requests.get(complete_url)


data = response.json()
def celcius(K):
    return round(int(K)-273.15 )
def fahrenheit(K):
    return round((int((K)-273.15) * 9/5 + 32))

if data["cod"] != "404":
    base = data["main"]
    current_temperature = base["temp"]
    current_pressure = base["pressure"]
    current_humidiy = base["humidity"]
    weather = data["weather"]
    weather_description = weather[0]["description"]


    print(f' Temperature (in kelvin) = {current_temperature}K \n Temperature (in celcius) ={celcius(current_temperature)}C \n Temperature (in fahrenheit) ={fahrenheit(current_temperature)}F'
        "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity = " +
                    str(current_humidiy) + "%" +
          "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")

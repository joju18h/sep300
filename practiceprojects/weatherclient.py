import requests

def geocoder(key, location):
    baseurl = "http://api.openweathermap.org/geo/1.0"

    parameters = {
        "q" : location,
        "appid" : key,
    }

    response = requests.get(baseurl + "/direct", params=parameters)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None
    
def getWeather(l, longitutde, key):
    baseurl = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "lat" :  l,
        "lon" : longitutde,
        "appid" : key,
        "units" : "metric",
    }

    response = requests.get(baseurl,parameters)

    if response.status_code ==  200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None





def main():
    API_KEY = "e7466c7574d23a1349e0929ef77c106e"
    user_location = input("enter a location ")
    data = geocoder(API_KEY, user_location)

    location_data = data[0]

    latitude = location_data['lat']
    longitude = location_data['lon']
    
    weather_data = getWeather(latitude, longitude, API_KEY)

    if weather_data:
        print(f"Weather in {user_location}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")

main()
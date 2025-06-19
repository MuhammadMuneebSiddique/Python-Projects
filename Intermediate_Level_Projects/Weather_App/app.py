import requests


def weather_app():
    country = input("Enter the country: ")
    api_key = "fe7c6c564ac0a5bc2952c151653335d7"

    api = f"https://api.openweathermap.org/data/2.5/weather?q={country.lower()}&appid={api_key}&units=metric"
    response = requests.get(api)
    weather = response.json()
    print()
    print(f"Weather in {weather["name"]}")
    print(f"Temperature: {weather["main"]["temp"]}C")
    print(f"Description: {weather["weather"][0]["description"]}")
    print(f"Humadity: {weather["main"]["humidity"]}%")
    print(f"Wind Speed: {weather["wind"]["speed"]}m/s")


weather_app()



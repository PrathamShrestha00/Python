import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to display weather information
def display_weather(weather_data):
    if weather_data["cod"] == "404":
        print("City not found!")
    else:
        city = weather_data["name"]
        main = weather_data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_desc = weather_data["weather"][0]["description"]
        print(f"Weather Information for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_desc}")

# Main function to run the app
def main():
    print("Weather App")
    city_name = input("Enter city name: ")
    api_key = "95fdc1b12a671b4ed3516fbbf6a0c5eb"  # Replace with your actual API key
    weather_data = get_weather(city_name, api_key)
    display_weather(weather_data)

# Run the app
if __name__ == "__main__":
    main()


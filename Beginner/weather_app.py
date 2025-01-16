import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API URL and API key from environment variables
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('WEATHER_API_KEY')


def get_weather(city):
    """Fetch weather data from the API."""
    if API_URL and API_KEY:
        # Make an API request using the stored URL and API key
        url = f"{API_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            name = data.get('name')
            temp = data.get('main', {}).get('temp')
            pressure = data.get('main', {}).get('pressure')
            humidity = data.get('main', {}).get('humidity')

            print(f"City: {name}")
            print(f"Temperature: {temp}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
        else:
            print("City not found or an error occurred.")
    else:
        print("API URL or API key is missing.")


def main():
    """Main function to run the weather app."""
    city = input("Enter city name: ").strip()
    get_weather(city)


if __name__ == "__main__":
    main()

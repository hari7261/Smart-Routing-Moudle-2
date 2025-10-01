import requests
import os
from dotenv import load_dotenv

load_dotenv()
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather_data(lat, lon):
    if not OPENWEATHER_API_KEY:
        print("OpenWeather API key not found")
        return {
            "temp_c": 20,
            "conditions": "Clear",
            "rain_mm": 0,
            "wind_speed_kmh": 10
        }
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"OpenWeather API error: {response.status_code}")
            return None

        data = response.json()
        return {
            "temp_c": data["main"]["temp"],
            "conditions": data["weather"][0]["main"],
            "rain_mm": data.get("rain", {}).get("1h", 0),
            "wind_speed_kmh": data["wind"]["speed"] * 3.6
        }
    except Exception as e:
        print(f"OpenWeather API error: {e}")
        return {
            "temp_c": 20,
            "conditions": "Clear",
            "rain_mm": 0,
            "wind_speed_kmh": 10
        }
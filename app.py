from flask import Flask, request, jsonify, render_template
from utils.tomtom import get_route_data
from utils.weather import get_weather_data
from utils.gemini import get_ai_suggestions
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Mock user vehicle profile (replace with OBD-II data in production)
VEHICLE_PROFILE = {
    "fuel_type": "gasoline",
    "weight_kg": 1500,
    "max_power_kw": 120
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/analyze_route", methods=["POST"])
def analyze_route():
    try:
        data = request.json
        if not data or "start" not in data or "end" not in data:
            return jsonify({"error": "Missing start or end coordinates"}), 400
        start = data["start"]
        end = data["end"]

        print(f"Analyzing route from {start} to {end}")  # Debug logging

        # Step 1: Get route data from TomTom
        route = get_route_data(start, end)
        if not route:
            return jsonify({"error": "Route not found"}), 404

        # Step 2: Get weather along the route
        waypoint = route["waypoints"][0]  # First major waypoint
        weather = get_weather_data(waypoint["lat"], waypoint["lon"])

        # Fallback weather if API fails
        if not weather:
            weather = {
                "temp_c": 20,
                "conditions": "Clear",
                "rain_mm": 0,
                "wind_speed_kmh": 10
            }

        # Step 3: Generate AI suggestions
        context = {
            "route": route,
            "weather": weather,
            "vehicle": VEHICLE_PROFILE
        }
        suggestions = get_ai_suggestions(context)
        print("[DEBUG] Suggestions type:", type(suggestions))
        print("[DEBUG] Suggestions content:", suggestions)

        return jsonify({
            "route": route,
            "weather": weather,
            "suggestions": suggestions
        })
    except Exception as e:
        print(f"Route analysis error: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route("/api/current_weather", methods=["GET"])
def current_weather():
    try:
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        
        if not lat or not lon:
            return jsonify({"error": "Missing lat or lon parameters"}), 400
        
        weather = get_weather_data(float(lat), float(lon))
        if not weather:
            return jsonify({"error": "Weather data not available"}), 404
        
        # Try to get city name from reverse geocoding
        city_name = get_city_name(float(lat), float(lon))
        
        return jsonify({
            "weather": weather,
            "city": city_name
        })
    except Exception as e:
        print(f"Current weather error: {e}")
        return jsonify({"error": "Failed to get weather data"}), 500

def get_city_name(lat, lon):
    """Get city name from coordinates using reverse geocoding"""
    try:
        import requests
        # Use a simple reverse geocoding service
        url = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={lon}&localityLanguage=en"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            city = data.get('city') or data.get('locality') or data.get('principalSubdivision')
            return city if city else "Unknown location"
    except Exception as e:
        print(f"Reverse geocoding error: {e}")
    return "Current location"

# GET handler for analyze_route returns 405
@app.route("/api/analyze_route", methods=["GET"])
def analyze_route_get():
    return jsonify({"error": "GET method not allowed for this endpoint. Use POST."}), 405

if __name__ == "__main__":
    app.run(debug=True)
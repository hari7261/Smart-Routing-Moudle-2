# 🚗 Smart Routing Module 2

A comprehensive smart routing and navigation system that combines intelligent route planning with real-time weather data and AI-powered driving suggestions. This project provides two different modules for navigation and smart driving assistance.

## ✨ Features

### Main Smart Driving Assistant (Root Module)
- 🗺️ **Intelligent Route Planning**: Calculate optimal routes between cities or coordinates using TomTom Routing API
- 🌦️ **Real-Time Weather Integration**: Get current weather conditions along your route using OpenWeather API
- 🤖 **AI-Powered Suggestions**: Receive personalized driving recommendations using Google Gemini AI
- 📊 **Detailed Route Analytics**: Distance, duration, traffic delays, and waypoint information
- 💡 **Smart Driving Tips**: Speed recommendations, throttle advice, terrain tips, and safety messages
- 🎨 **Clean Web Interface**: User-friendly interface for route analysis

### TomTom Navigation Module (module1)
- 🗺️ **Interactive Map Navigation**: Visual route display using Leaflet and TomTom Maps
- 📍 **Geocoding Support**: Enter city names or addresses - automatic conversion to coordinates
- 🚦 **Multiple Route Types**: Choose from fastest, shortest, eco, or thrilling routes
- 🚗 **Traffic-Aware Routing**: Real-time traffic integration for accurate ETA
- 📋 **Turn-by-Turn Instructions**: Detailed navigation instructions with distance markers
- 🎯 **Custom Vehicle Parameters**: Configure vehicle specifications for optimized routing

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **APIs**: 
  - TomTom Routing & Geocoding API
  - OpenWeather API
  - Google Gemini AI API
- **Frontend**: 
  - HTML5, CSS3, JavaScript
  - Leaflet.js (Interactive maps)
  - TomTom Maps SDK
- **Dependencies**: 
  - `requests` - HTTP library
  - `python-dotenv` - Environment variable management
  - `google-generativeai` - Gemini AI integration

## 📋 Prerequisites

Before running this project, you'll need to obtain API keys from:

1. **TomTom API**: 
   - Sign up at [TomTom Developer Portal](https://developer.tomtom.com/)
   - Get your API key for Routing and Geocoding services

2. **OpenWeather API**:
   - Register at [OpenWeather](https://openweathermap.org/api)
   - Get your free API key

3. **Google Gemini AI** (Optional but recommended):
   - Access [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Generate your Gemini API key

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hari7261/Smart-Routing-Moudle-2.git
cd Smart-Routing-Moudle-2
```

### 2. Install Dependencies

#### For Main Module (Smart Driving Assistant):
```bash
pip install -r requirements.txt
```

#### For Module 1 (TomTom Navigation):
```bash
cd module1
pip install -r requirements.txt
cd ..
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with your API keys:

```env
TOMTOM_API_KEY=your_tomtom_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

**Note**: The project includes fallback mechanisms, so if some API keys are missing:
- TomTom: Returns mock data
- OpenWeather: Returns default weather conditions
- Gemini AI: Returns basic driving suggestions

## 📖 Usage

### Running the Main Smart Driving Assistant

```bash
python app.py
```

Then open your browser and navigate to: `http://localhost:5000`

**How to use:**
1. Enter your starting location (city name or coordinates)
2. Enter your destination (city name or coordinates)
3. Click "Analyze Route"
4. View comprehensive route details, weather conditions, and AI-powered suggestions

### Running TomTom Navigation Module

```bash
cd module1
python app.py
```

Then open your browser and navigate to: `http://localhost:5000`

**How to use:**
1. Enter start and end locations (addresses or city names)
2. Select route type (fastest, shortest, eco, or thrilling)
3. Choose whether to include real-time traffic
4. Click "Calculate Route"
5. View the route on the interactive map with turn-by-turn instructions

## 📁 Project Structure

```
Smart-Routing-Moudle-2/
├── app.py                      # Main application (Smart Driving Assistant)
├── requirements.txt            # Main dependencies
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore rules
│
├── utils/                      # Utility modules
│   ├── __init__.py
│   ├── tomtom.py              # TomTom API integration
│   ├── weather.py             # OpenWeather API integration
│   └── gemini.py              # Google Gemini AI integration
│
├── templates/                  # HTML templates for main module
│   └── index.html             # Main interface
│
├── static/                     # Static assets for main module
│   └── style.css              # Styling
│
└── module1/                    # TomTom Navigation Module
    ├── app.py                 # Navigation app
    ├── requirements.txt       # Module-specific dependencies
    ├── templates/
    │   └── index.html        # Navigation interface
    └── static/
        └── style.css         # Navigation styling
```

## 🌐 API Endpoints

### Main Module (Smart Driving Assistant)

#### `GET /`
Returns the main web interface

#### `POST /api/analyze_route`
Analyzes a route and returns comprehensive data

**Request Body:**
```json
{
  "start": "New York",
  "end": "Boston"
}
```

**Response:**
```json
{
  "route": {
    "distance_km": 215.5,
    "duration_min": 195.2,
    "waypoints": [...],
    "traffic_delay_sec": 300
  },
  "weather": {
    "temp_c": 18.5,
    "conditions": "Clear",
    "rain_mm": 0,
    "wind_speed_kmh": 15.2
  },
  "suggestions": {
    "recommended_speed_kmh": 85,
    "throttle_advice": "...",
    "terrain_advice": "...",
    "safety_message": "...",
    "extra_tips": "..."
  }
}
```

#### `GET /api/current_weather?lat={lat}&lon={lon}`
Get current weather for specific coordinates

### Module 1 (TomTom Navigation)

#### `GET /`
Returns the navigation interface

#### `POST /calculate_route`
Calculates a route with specified parameters

**Request Body:**
```json
{
  "start": "London",
  "end": "Paris",
  "routeType": "fastest",
  "traffic": "true"
}
```

## 🎨 Features in Detail

### Smart Driving Assistant Features

1. **Route Analysis**
   - Calculates distance and estimated travel time
   - Identifies waypoints along the route
   - Provides traffic delay information

2. **Weather Integration**
   - Real-time weather at route waypoints
   - Temperature, conditions, rain, and wind speed
   - Weather-aware driving suggestions

3. **AI Suggestions**
   - Recommended driving speed based on route and weather
   - Fuel-efficient throttle advice
   - Terrain-specific safety tips
   - Personalized comfort recommendations

### TomTom Navigation Features

1. **Multiple Route Types**
   - **Fastest**: Minimize travel time
   - **Shortest**: Minimize distance
   - **Eco**: Optimize for fuel efficiency
   - **Thrilling**: For scenic or exciting routes

2. **Interactive Mapping**
   - Visual route display on Leaflet map
   - Start/end location markers
   - Route polyline overlay
   - Zoom and pan controls

3. **Vehicle Customization**
   - Configure max speed, weight, dimensions
   - Commercial vs. personal vehicle settings
   - Optimized routing based on vehicle specs

## 🔧 Configuration Options

### Vehicle Profile (Main Module)
Located in `app.py`:
```python
VEHICLE_PROFILE = {
    "fuel_type": "gasoline",    # or "diesel", "electric"
    "weight_kg": 1500,          # Vehicle weight
    "max_power_kw": 120         # Maximum power
}
```

### Route Parameters (Module 1)
Customizable via the web interface:
- Route type selection
- Traffic enable/disable
- Vehicle specifications

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

## 🐛 Known Issues & Limitations

- API rate limits may apply based on your subscription tier
- Geocoding works best with well-known city names
- Mock data is returned if API keys are not configured
- Gemini AI may occasionally return non-JSON responses (handled with fallbacks)

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Hari**
- GitHub: [@hari7261](https://github.com/hari7261)

## 🙏 Acknowledgments

- TomTom for their excellent routing and mapping APIs
- OpenWeather for weather data integration
- Google for Gemini AI capabilities
- Leaflet.js for interactive mapping

## 📞 Support

For issues, questions, or contributions, please:
- Open an issue on GitHub
- Submit a pull request
- Contact the repository maintainer

---

**Happy Routing! 🚗💨**

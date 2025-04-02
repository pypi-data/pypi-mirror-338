import os
from typing import Any, Dict
import requests
from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def current_weather(city: str) -> Dict[str, Any]:
    """Query the current weather by city name"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable is required")

    # Step 1: Get city coordinates
    try:
        geo_response = requests.get(
            "http://api.openweathermap.org/geo/1.0/direct",
            params={
                "q": city,
                "limit": 1,
                "appid": api_key
            }
        )
        geo_response.raise_for_status()
        locations = geo_response.json()
        
        if not locations:
            return {"error": f"Could not find location data for city: {city}"}
            
        location = locations[0]
        
        # Step 2: Get weather data using coordinates
        weather_response = requests.get(
            "https://api.openweathermap.org/data/3.0/onecall",
            params={
                "lat": location["lat"],
                "lon": location["lon"],
                "units": "metric",
                "exclude": "minutely,hourly,daily,alerts",
                "appid": api_key
            }
        )
        weather_response.raise_for_status()
        data = weather_response.json()
        current = data["current"]

        formatted_response = {
            "city": location["name"],
            "country": location["country"],
            "state": location.get("state"),
            "coordinates": {
                "lat": location["lat"],
                "lon": location["lon"]
            },
            "temperature": {
                "current": f"{current['temp']}°C",
                "feels_like": f"{current['feels_like']}°C"
            },
            "weather": {
                "main": current["weather"][0]["main"],
                "description": current["weather"][0]["description"],
                "icon": f"https://openweathermap.org/img/wn/{current['weather'][0]['icon']}@2x.png",
            },
            "details": {
                "humidity": f"{current['humidity']}%",
                "pressure": f"{current['pressure']} hPa",
                "wind_speed": f"{current['wind_speed']} m/s",
                "wind_direction": f"{current['wind_deg']}°",
                "wind_gust": f"{current.get('wind_gust', 0)} m/s",
                "cloudiness": f"{current['clouds']}%",
                "uvi": current["uvi"],
                "visibility": f"{current.get('visibility', 0)/1000:.1f} km"
            },
            "sun": {
                "sunrise": datetime.fromtimestamp(current["sunrise"]).strftime("%H:%M:%S"),
                "sunset": datetime.fromtimestamp(current["sunset"]).strftime("%H:%M:%S"),
            },
            "timezone": {
                "name": data["timezone"],
                "offset": data["timezone_offset"]
            },
            "timestamp": datetime.fromtimestamp(current["dt"]).isoformat()
        }

        return formatted_response
    except requests.exceptions.RequestException as e:
        error_message = f"Weather API error: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                if 'message' in error_data:
                    error_message = f"Weather API error: {error_data['message']}"
            except ValueError:
                pass
        return {"error": error_message}
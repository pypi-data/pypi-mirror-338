from .base import Tool
import numpy as np
from typing import List, Dict
from datetime import datetime
import pytz
import json
from duckduckgo_search import DDGS
import requests
import os
import dotenv
from bs4 import BeautifulSoup

# Load environment variables from .env file if it exists
dotenv.load_dotenv()

class WeatherTool(Tool):
    "Tool to get current weather information from OpenWeatherMap API. Query is performed by city name."
    def __init__(self, api_key: str):
        super().__init__(
            name="weather",
            description="Get current weather information from OpenWeatherMap API"
        )

        self.api_key = os.environ['WEATHER_API_KEY'] if api_key is None else api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.params = {
            "appid": self.api_key,
            "units": "metric"  # Use metric units by default
        }

    def execute(self, location: str) -> Dict:
        """
        Execute a weather query using OpenWeatherMap API.
        """
        try:
            self.params["q"] = location
            response = requests.get(self.base_url, params=self.params)
            response.raise_for_status()  # Raise an error for bad responses
            
            data = response.json()
            
            if data.get("cod") != 200:
                return {"error": "City not found"}
            
            # Extract relevant information from the response
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            
            return weather_info
        
        except Exception as e:
            return {"error": str(e)}
        

class WebSearch(Tool):
    """
    Tool to perform web searches using DuckDuckGo API. This performs a search query and returns the results, typically a wide range of information.
    """
    def __init__(self, api_key: str = None):  # Make api_key optional since DuckDuckGo doesn't require one
        super().__init__(
            name="web_search",
            description="Search the web for current information using DuckDuckGo"
        )
        self.api_key = api_key  # Not used but kept for compatibility

    def execute(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Execute a web search using DuckDuckGo.
        """
        try:            
            results = []
            with DDGS() as ddgs:
                search_results = list(ddgs.text(query, max_results=max_results))
                
                for result in search_results:
                    results.append({
                        "title": result.get("title", "No title"),
                        "snippet": result.get("body", "No description"),
                        "url": result.get("href", "No URL")
                    })
            
            if not results:
                return {"message": "No results found for this query."}
            
            # Return a more structured format that's easier to format naturally
            return {
                "query": query,
                "num_results": len(results),
                "results": results
            }
            
        except Exception as e:
            import traceback
            traceback.format_exc()
            return {"error": f"Search failed: {str(e)}"}

class Calculator(Tool):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Perform mathematical calculations"
        )

    def execute(self, expression: str) -> Dict:
        try:
            # Safely evaluate mathematical expressions
            result = eval(expression, {"__builtins__": {}}, 
                       {"np": np, "sin": np.sin, "cos": np.cos, 
                        "tan": np.tan, "sqrt": np.sqrt, "log": np.log,
                        "log10": np.log10, "exp": np.exp, "pi": np.pi})
                        
            # Return a more structured result
            return {
                "expression": expression,
                "result": result,
                "formatted_result": f"{result:,}" if isinstance(result, (int, float)) else str(result)
            }
        except Exception as e:
            return {
                "expression": expression,
                "error": str(e)
            }


class TimezoneTool(Tool):
    def __init__(self):
        super().__init__(
            name="timezone",
            description="Convert between timezones"
        )

    def execute(self, time: str, from_tz: str, to_tz: str) -> str:
        """
        Convert time between different timezones.

        Args:
            time (str): ISO-8601 formatted datetime string.
            from_tz (str): Source timezone.
            to_tz (str): Target timezone.
        Returns:
            str: JSON string containing original and converted time info,
                 or an error message if conversion fails.
        """
        try:
            # Parse the ISO-8601 time string, replacing 'Z' with '+00:00'
            dt = datetime.fromisoformat(time.replace('Z', '+00:00'))
            
            # Localize the datetime to the source timezone without any tz info
            source_timezone = pytz.timezone(from_tz)
            dt_source = source_timezone.localize(dt.replace(tzinfo=None))
            
            # Convert the localized time to the target timezone
            target_timezone = pytz.timezone(to_tz)
            dt_target = dt_source.astimezone(target_timezone)
            
            result = {
                "original_time": time,
                "original_timezone": from_tz,
                "converted_time": dt_target.isoformat(),
                "converted_timezone": to_tz
            }
            return json.dumps(result)
        except Exception as e:
            return f"Error converting timezone: {str(e)}"

class UnitConverter(Tool):
    def __init__(self):
        super().__init__(
            name="unit_converter",
            description="Convert between different units"
        )

    def execute(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert values between different units of measurement."""
        # Simple mapping of conversion factors for common units
        conversion_map = {
            # Length
            "m_to_ft": 3.28084,
            "ft_to_m": 0.3048,
            "km_to_mile": 0.621371,
            "mile_to_km": 1.60934,
            # Weight/Mass
            "kg_to_lb": 2.20462,
            "lb_to_kg": 0.453592,
            # Temperature needs special handling
            "celsius_to_fahrenheit": lambda c: c * 9/5 + 32,
            "fahrenheit_to_celsius": lambda f: (f - 32) * 5/9,
        }
        
        try:
            # Create a key for the conversion map
            conversion_key = f"{from_unit.lower()}_to_{to_unit.lower()}"
            
            # Check if conversion exists
            if conversion_key in conversion_map:
                conversion = conversion_map[conversion_key]
                
                # Handle functions (e.g., temperature conversions)
                if callable(conversion):
                    result = conversion(value)
                else:
                    result = value * conversion
                    
                return {
                    "original_value": value,
                    "original_unit": from_unit,
                    "converted_value": result,
                    "converted_unit": to_unit
                }
            else:
                return f"Conversion from {from_unit} to {to_unit} is not supported"
                
        except Exception as e:
            return f"Error converting units: {str(e)}"
        

class WebScraper(Tool):
    """
    Tool to scrape data from a webpage. This tool fetches the HTML content of a given URL and returns the text content.
    """
    def __init__(self):
        super().__init__(
            name="web_scraper",
            description="Scrape data from a webpage and return the text content"
        )

    def execute(self, url: str) -> Dict:
        """
        Scrape data from a webpage.
        """

        soup = BeautifulSoup(requests.get(url).text, 'html.parser')

        try:
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            text = soup.get_text()
            # Clean up the text content
            text = ' '.join(text.split())
            text = text.replace('\n', ' ').replace('\r', ' ').strip()
            
            # Return the raw HTML content as a string
            return {
                "url": url,
                "content": text[:1000]  # Return first 1000 characters for brevity
            }
            
        except Exception as e:
            return {"error": str(e)}

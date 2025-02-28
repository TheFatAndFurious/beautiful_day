
import requests
from click import style
from rich.console import Console
from rich.table import Table

class APIQueries:
    def __init__(self, api_key:str):
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "open-weather13.p.rapidapi.com"
        }

    def current_weather(self, city_name):
        """Fetch current weather data for a given city name.
            :parameters: city_name: str
        """
        url = f"https://open-weather13.p.rapidapi.com/city/{city_name}&units=metric/FR"
        headers = self.headers
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            processed_response = self._parse_current_response(response.json())
            return processed_response
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


    def forecast(self, lat:float, lon:float):
        """Fetch 5-day weather forecast for a given location.
            :parameters: lat: float, lon: float
        """
        url = f"https://open-weather13.p.rapidapi.com/city/fivedaysforcast/{lat}/{lon}&units=metric"
        headers = self.headers
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            parsed_data = self._parse_forecast_response(response.json())
            return parsed_data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    @staticmethod
    def _parse_current_response(response: dict):
        return {
            'city': response.get('name'),
            'temperature': response.get('main', {}).get('temp'),
            'temp_feels_like': response.get('main', {}).get('feels_like'),
            'description': response.get('weather', [{}])[0].get('description'),
            'icon': response.get('weather', [{}])[0].get('icon'),
            'wind_speed': response.get('wind', {}).get('speed')
        }

    @staticmethod
    def _parse_forecast_response(response: dict):
        data = response.get('list', {})
        weather_array = []
        for occurence in data:
            weather_array.append({
                'date': occurence.get('dt_txt'),
                'temperature': occurence.get('main', {}).get('temp'),
                'temp_feels_like': occurence.get('main', {}).get('feels_like'),
                'weather': occurence.get('weather', [{}])[0].get('description')
            })
        return weather_array
def format_forecast_response(data):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Date")
    table.add_column("Temperature")
    table.add_column("Feels like")
    table.add_column("Weather")


    for occurence in data:
        table.add_row(occurence.get('date'), str(occurence.get('temperature')), str(occurence.get('temp_feels_like')), occurence.get('weather'))

    console.print(table)

def format_current_response(data):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Attribute")
    table.add_column("Value")

    table.add_row("City", data.get("city"))
    table.add_row("Temperature", str(data.get("temperature")))
    table.add_row("Feels like", str(data.get("temp_feels_like")))
    table.add_row("Description", data.get("description"))
    table.add_row("Wind speed", str(data.get("wind_speed")))

    console.print(table)







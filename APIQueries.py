
import requests
from rich.console import Console
from rich.table import Table

class APIQueries:
    def __init__(self, api_key:str):
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "open-weather13.p.rapidapi.com"
        }

    def current_weather(self, city_name):
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
        url = f"https://open-weather13.p.rapidapi.com/city/fivedaysforcast/{lat}/{lon}&units=metric"
        headers = self.headers
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def _parse_current_response(response: dict):
        return {
            'temperature': response.get('main', {}).get('temp'),
            'temp_feels_like': response.get('main', {}).get('feels_like'),
        }

def format_response(data):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Attribute")
    table.add_column("Value")

    table.add_row("Temperature", str(data.get("temperature")))
    table.add_row("Feels like", str(data.get("temp_feels_like")))

    console.print(table)







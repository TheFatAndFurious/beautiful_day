import requests

class APIQueries:
    def __init__(self, api_key:str):
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "open-weather13.p.rapidapi.com"
        }

    def current_weather(self, city_name):
        url = f"https://open-weather13.p.rapidapi.com/city/{city_name}/FR"
        headers = self.headers
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def forecast(self, city):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}"
        response = requests.get(url)
        return response.json()



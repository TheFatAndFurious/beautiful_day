CITY_COORDINATES = {
    "san francisco": {"lat": 37.7749, "lon": -122.4194},
    "new York": {"lat": 40.7128, "lon": -74.0060},
    "london": {"lat": 51.5074, "lon": -0.1278},
    "balma": {"lat": 43.6111, "lon": 1.4994},
}

def get_coordinates(city_name: str):
    coords = CITY_COORDINATES.get(city_name.lower())
    if not coords:
        raise ValueError(f"City {city_name} not found")
    return coords
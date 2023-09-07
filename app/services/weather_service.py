# /api-bridge/app/services/weather_service.py
import requests
from flask_restx import abort
from app.constants import CITY_SEARCH_CACHE_TIMEOUT, WEATHER_CACHE_TIMEOUT
from app import cache
from ..config import *


def get_weather_by_location(location):
    cache_key = f"get_weather_by_location_{location}"

    try:
        if cache.get(cache_key):
            print("Cache hit :-) ")
            return cache.get(cache_key)
        # https://api.openweathermap.org/data/2.5/weather?q=rio+de+janeiro&appid=0f407f8dd956c7204bc02a9c3423c83c&lang=pt_br
        endpoint = f"{WEATHER_API_URL}/weather?q={location}&{WEATHER_API_DEFAULT_QUERYSTRING}"
        print("Cache miss :-( ")
        response = requests.get(endpoint)
        if response.status_code != 200:
            return {"error": "Erro ao buscar dados da API do clima."}

        cache.set(cache_key, response.json(), timeout=WEATHER_CACHE_TIMEOUT)
        data = response.json()

        return {
            "name": data["name"],
            "timezone": data["timezone"],
            "dt": data["dt"],
            "country": data["sys"]["country"],
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"],
            "temp": data["main"]["temp"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"]["deg"],
            "clouds": data["clouds"]["all"]
        }

    except requests.RequestException:
        abort(500, "Erro ao buscar dados da API do clima.")


def search_city(city_name):
    cache_key = f"city_search_{city_name}"

    try:
        if cache.get(cache_key):
            print("Cache hit :-) ")
            return cache.get(cache_key)
        # https://api.openweathermap.org/geo/1.0/direct?q=janeiro&appid=0f407f8dd956c7204bc02a9c3423c83c&lang=pt_br&limit=5
        url = f"{GEOCODE_API_URL}/direct?q={city_name}&{GEOCODE_API_DEFAULT_QUERYSTRING}"
        print("Cache miss :-( ")
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "Erro ao buscar dados da API do clima."}

        data = response.json()
        cities = [{
            "name": item["name"],
            "country": item["country"],
            "state": item["state"] if "state" in item else "",
            "lat": item["lat"],
            "lon": item["lon"]
        } for item in data]

        cache.set(cache_key, cities, timeout=CITY_SEARCH_CACHE_TIMEOUT)

        return cities
    except requests.RequestException:
        abort(500, "Erro ao buscar dados da API do clima.")

# /api-bridge/app/services/location_service.py
import requests
from flask_restx import abort
from app.constants import CITY_SEARCH_CACHE_TIMEOUT
from app import cache
from ..config import *


def search_city(city_name):
    cache_key = f"city_search_{city_name}"

    try:
        if cache.get(cache_key):
            return cache.get(cache_key)
        # https://api.openweathermap.org/geo/1.0/direct?q=janeiro&appid=0f407f8dd956c7204bc02a9c3423c83c&lang=pt_br&limit=5
        url = f"{GEOCODE_API_URL}/direct?q={city_name}&{GEOCODE_API_DEFAULT_QUERYSTRING}"
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
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

        url = f"{GEOCODE_API_URL}/direct?q={city_name}&{GEOCODE_API_DEFAULT_QUERYSTRING}"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "Erro ao buscar dados da API do clima."}

        data = response.json()

        unique_ids = set()
        cities = []

        for item in data:
            unique_id = f"{item['name']}{', ' + item['state'] if 'state' in item else ''}, {item['country']}"
            if unique_id not in unique_ids:
                unique_ids.add(unique_id)
                city_data = {
                    "unique_id": unique_id,
                    "name": item["name"],
                    "country": item["country"],
                    "state": item["state"] if "state" in item else "",
                    "lat": item["lat"],
                    "lon": item["lon"]
                }
                cities.append(city_data)

        cache.set(cache_key, cities, timeout=CITY_SEARCH_CACHE_TIMEOUT)
        return cities
    except requests.RequestException:
        abort(500, "Erro ao buscar dados da API do clima.")
# /api-bridge/app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True if os.getenv("FLASK_ENV") == "development" else False
PORT = os.getenv("FLASK_RUN_PORT", 5001)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    raise ValueError("Você precisa definir a chave da API do OpenWeatherMap na variável de ambiente WEATHER_API_KEY")

WEATHER_API_URL = os.getenv("WEATHER_API_URL")
if not WEATHER_API_URL:
    raise ValueError("Você precisa definir a URL da API do OpenWeatherMap na variável de ambiente WEATHER_API_URL")

WEATHER_API_UNITS = os.getenv("WEATHER_API_UNITS", "metric")
WEATHER_API_LANG = os.getenv("WEATHER_API_LANG", "pt_br")
WEATHER_API_TIMEZONE = os.getenv("WEATHER_API_TIMEZONE", "+03:00")
WEATHER_FORECAST_DAYS_COUNT = os.getenv("WEATHER_FORECAST_DAYS_COUNT", 24)
WEATHER_API_DEFAULT_QUERYSTRING = f"appid={WEATHER_API_KEY}&units={WEATHER_API_UNITS}&lang={WEATHER_API_LANG}&timezone={WEATHER_API_TIMEZONE}&cnt={WEATHER_FORECAST_DAYS_COUNT}"

GEOCODE_API_URL = os.getenv("GEOCODE_API_URL")
if not GEOCODE_API_URL:
    raise ValueError("Você precisa definir a URL da API do OpenWeatherMap na variável de ambiente GEOCODE_API_URL")

GEOCODE_API_DEFAULT_LIMIT = os.getenv("GEOCODE_API_DEFAULT_LIMIT", 5)
GEOCODE_API_DEFAULT_QUERYSTRING = f"appid={WEATHER_API_KEY}&lang={WEATHER_API_LANG}&limit={GEOCODE_API_DEFAULT_LIMIT}"

CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 60 * 60  # 1 hora

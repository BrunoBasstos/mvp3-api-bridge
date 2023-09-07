# /api-bridge/app/__init__.py
from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_caching import Cache
from . import exceptions
from . import config

# Inicialização do Flask
app = Flask(__name__)

# Configuração do cache
cache = Cache(app, config={'CACHE_TYPE': config.CACHE_TYPE, 'CACHE_DEFAULT_TIMEOUT': config.CACHE_DEFAULT_TIMEOUT})
app.cache = cache

# Configuração do CORS
CORS(app)

# Inicialização do Flask-RESTx API
api = Api(app, version='1.0', title='API Bridge',
          description='Uma API ponte para se comunicar com APIs externas (ViaCEP e OpenWeatherMap)',
          )

from app.routes import location, weather

api.add_namespace(location.ns, path='/api/location')
api.add_namespace(weather.ns, path='/api/weather')

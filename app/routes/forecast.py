# /api-bridge/app/routes/forecast.py
from flask_restx import Namespace, Resource, fields
from app.services.weather_service import get_weather_forecast_by_location

ns = Namespace('forecast', description='Previsão do tempo')
forecast_model = ns.model('WeatherForecastByLocation', {
    'name': fields.String(required=True, description='Nome da localidade/cidade'),
    'timezone': fields.Integer(required=True, description='Fuso horário'),
    'country': fields.String(required=True, description='País'),
    'lat': fields.Float(required=True, description='Latitude'),
    'lon': fields.Float(required=True, description='Longitude'),
    'sunrise': fields.Integer(required=True, description='Nascer do sol'),
    'sunset': fields.Integer(required=True, description='Pôr do sol'),
    'forecast': fields.List(fields.Nested(ns.model('Forecast', {
        'dt': fields.Integer(required=True, description='Data e hora da previsão'),
        'description': fields.String(required=True, description='Descrição do clima'),
        'icon': fields.String(required=True, description='Ícone do clima'),
        'temp': fields.Float(required=True, description='Temperatura'),
        'temp_min': fields.Float(required=True, description='Temperatura mínima'),
        'temp_max': fields.Float(required=True, description='Temperatura máxima'),
        'feels_like': fields.Float(required=True, description='Sensação térmica'),
        'humidity': fields.Integer(required=True, description='Umidade'),
        'pressure': fields.Integer(required=True, description='Pressão'),
        'wind_speed': fields.Float(required=True, description='Velocidade do vento'),
        'wind_deg': fields.Integer(required=True, description='Direção do vento'),
        'clouds': fields.Integer(required=True, description='Nuvens')
    })))
})


# busca previsão do tempo por localidade (get_weather_forecast_by_location)
@ns.route('/<string:location>')
@ns.response(404, 'Localidade não encontrada')
@ns.param('location', 'Nome da localidade/cidade')
class WeatherForecastByLocation(Resource):

    @ns.doc('get_weather_forecast_by_location')
    @ns.marshal_with(forecast_model)
    def get(self, location):
        """
        Retorna a previsão do tempo para uma localidade/cidade
        """
        return get_weather_forecast_by_location(location)

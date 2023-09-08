# /api-bridge/app/routes/location.py
from flask_restx import Namespace, Resource, fields
from app.services.location_service import search_city

ns = Namespace('location', description='Busca de localidades/cidades')
city_search_model = ns.model('CitySearch', {
    'name': fields.String(required=True, description='Nome da localidade/cidade'),
    'country': fields.String(required=True, description='País'),
    'state': fields.String(required=True, description='Estado'),
    'lat': fields.Float(required=True, description='Latitude'),
    'lon': fields.Float(required=True, description='Longitude')
})


# busca de localidades/cidades
@ns.route('/search/<string:city_name>')
@ns.response(404, 'Nenhum resultado encontrado')
@ns.param('city_name', 'Nome da localidade/cidade')
class CitySearch(Resource):

    @ns.doc('search_city')
    @ns.marshal_list_with(city_search_model)
    def get(self, city_name):
        """
        Retorna uma lista de localidades/cidades
        """
        return search_city(city_name)

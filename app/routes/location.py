# /api-bridge/app/routes/location.py
from flask_restx import Namespace, Resource, fields, abort
from app.services.location_service import get_location_data

ns = Namespace('location', description='Operações de localidades')

location_model = ns.model('Location', {
    'cep': fields.String(required=True, description='CEP da localidade'),
    'logradouro': fields.String(description='Logradouro'),
    'complemento': fields.String(description='Complemento'),
    'bairro': fields.String(description='Bairro'),
    'localidade': fields.String(description='Localidade'),
    'uf': fields.String(description='UF'),
    'ibge': fields.String(description='IBGE'),
    'gia': fields.String(description='GIA'),
    'ddd': fields.String(description='DDD'),
    'siafi': fields.String(description='SIAFI'),
    'error': fields.String(description='Mensagem de erro')
})


@ns.route('/<string:cep>')
@ns.response(404, 'CEP não encontrado')
@ns.param('cep', 'O CEP da localidade')
class Location(Resource):
    @ns.doc('get_location_data')
    @ns.marshal_with(location_model)
    def get(self, cep):
        """
        Retorna detalhes de uma localidade baseado no CEP
        """
        data = get_location_data(cep)
        if "error" in data:
            abort(404, "CEP não encontrado")
        return data


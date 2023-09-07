# /api-bridge/app/exceptions/handler.py
from app import app, api


# error handler
@api.errorhandler(500)
def handle_500_error(error):
    if app.debug:
        return {'message': str(error)}, 500
    return {'message': 'Erro interno do servidor'}, 500


@api.errorhandler(404)
def handle_404_error(error):
    return {'message': 'Recurso não encontrado'}, 404


@api.errorhandler(400)
def handle_400_error(error):
    return {'message': 'Requisição inválida'}, 400

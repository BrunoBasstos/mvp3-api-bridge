# /api-bridge/app/services/location_service.py
import requests


def get_location_data(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        data = response.json()
        if "erro" in data:
            return {"error": "CEP não encontrado"}
        return data
    except Exception as e:
        return {"error": "Erro desconhecido"}

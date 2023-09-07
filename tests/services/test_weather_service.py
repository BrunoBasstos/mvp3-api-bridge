import unittest
from app.services import weather_service


class TestWeatherService(unittest.TestCase):

    def test_valid_location(self):
        data = weather_service.get_weather_by_location("Rio de Janeiro")
        self.assertIn("name", data)

    def test_invalid_location(self):
        data = weather_service.get_weather_by_location("cidade_que-nao-existe-para-garantir-o-erro")
        self.assertIn("error", data)

    def test_search_city(self):
        data = weather_service.search_city("York")
        self.assertGreater(len(data), 0)


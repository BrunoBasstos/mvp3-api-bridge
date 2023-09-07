import unittest
from app.services import location_service


class TestLocationService(unittest.TestCase):

    def test_valid_cep(self):
        # Use um CEP válido para este teste
        data = location_service.get_location_data("01001000")
        self.assertIn("logradouro", data)

    def test_invalid_cep(self):
        data = location_service.get_location_data("99999999")
        self.assertIn("error", data)


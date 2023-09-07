import unittest
from app import app


class TestAPIRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_location_route_valid(self):
        response = self.client.get("/api/location/01001000")
        self.assertEqual(response.status_code, 200)

    def test_location_route_invalid(self):
        response = self.client.get("/api/location/99999999")
        self.assertEqual(response.status_code, 404)

    # E assim por diante para as outras rotas...

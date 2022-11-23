from rest_framework.test import APITestCase


class TestAmenities(APITestCase):
    def test_all_amenities(self):
        reponse = self.client.get("/api/v1/rooms/amenities/")
        print(reponse)

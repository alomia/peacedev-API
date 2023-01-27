from django.test import TestCase

from .models import Hotel


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hotel = Hotel.objects.create(
            name="Hotel Casa Pestagua",
            code="HTCPE-08"
        )

    def test_model_content(self):
        self.assertEqual(self.hotel.name, "Hotel Casa Pestagua")
        self.assertEqual(self.hotel.code, "HTCPE-08")
        self.assertEqual(str(self.hotel), "Hotel Casa Pestagua")

from django.test import TestCase
from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer
from rest_framework.test import APIClient
from datetime import datetime

class MenuViewTest(TestCase):
    
    def setup(self):
        self.client = APIClient()
        item = Menu.objects.create(title="Pecan Pie", price=5.99, inventory=20)
    
    def test_get_item(self):
        response = self.client.get("/restaurant/menu/")

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

from django.test import TestCase
from rest_framework.test import APIClient
from restaurant import models, serializers
from rest_framework import status

class TestMenuView(TestCase):
    def setup(self):
        self.item_1 = models.Menu.objects.create(title='Pizza', price=10, inventory=50)
        self.item_2 = models.Menu.objects.create(title='Pasta', price=8, inventory=30)
        self.client = APIClient()
    
    def test_get_all(self):
        response = self.client.get('/restaurant/menu')
        menu_items = models.Menu.objects.all()
        expected_data = serializers.MenuSerializer(menu_items, many=True).data

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Ensure response is 200
        self.assertEqual(response.json(), expected_data)
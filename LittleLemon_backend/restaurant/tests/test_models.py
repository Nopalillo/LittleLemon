from django.test import TestCase
from restaurant import models

class MenuTest(TestCase):
    def test_instance(self):
        item = models.Menu.objects.create(title='IceCream', price=1, inventory=80)
        self.assertEqual(str(item), "IceCream : 1")
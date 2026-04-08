from django.test import TestCase
from ..models import Menu

# TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=1, name="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
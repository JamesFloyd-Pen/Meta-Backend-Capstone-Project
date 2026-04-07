from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu
from .serializers import MenuSerializer


class MenuViewTest(TestCase):
    
    def setUp(self):
        """Create test Menu instances"""
        self.menu1 = Menu.objects.create(
            id=1,
            name="Burger",
            price=8.99,
            inventory=50
        )
        self.menu2 = Menu.objects.create(
            id=2,
            name="Pizza",
            price=12.99,
            inventory=30
        )
        self.menu3 = Menu.objects.create(
            id=3,
            name="Salad",
            price=6.99,
            inventory=40
        )
        self.client = APIClient()
    
    def test_getall(self):
        """Test retrieving all Menu objects and verify serialized data"""
        # Make GET request to menu endpoint
        response = self.client.get('/restaurant/menu/')
        
        # Get all Menu objects from database
        menus = Menu.objects.all()
        
        # Serialize the Menu objects
        serializer = MenuSerializer(menus, many=True)
        
        # Assert response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert serialized data equals response data
        self.assertEqual(response.data, serializer.data)

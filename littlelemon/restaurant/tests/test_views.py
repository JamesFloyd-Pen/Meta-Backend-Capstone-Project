from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Booking, Menu
from ..serializers import BookingSerializer, MenuSerializer


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

class BookingViewTest(TestCase):
    
    def setUp(self):
        """Create test Booking instances"""
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
        self.booking1 = Booking.objects.create(
            id=1,
            name="Jane Doe",
            No_of_guests=4,
            Booking_date="2024-07-01"
        )
        self.booking2 = Booking.objects.create(
            id=2,
            name="John Smith",
            No_of_guests=2,
            Booking_date="2024-07-02"
        )
        self.booking3 = Booking.objects.create(
            id=3,
            name="Ellen Joes",
            No_of_guests=6,
            Booking_date="2024-07-03"
        )
        self.client = APIClient()
        # Authenticate the client
        self.client.force_authenticate(user=self.user)
    
    def test_getall(self):
        """Test retrieving all Booking objects and verify serialized data"""
        # Make GET request to booking endpoint
        response = self.client.get('/restaurant/booking/')
        
        # Get all Booking objects from database
        bookings = Booking.objects.all()
        
        # Serialize the Booking objects
        serializer = BookingSerializer(bookings, many=True)
        
        # Assert response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert serialized data equals response data
        self.assertEqual(response.data, serializer.data)
from django.test import TestCase
from restaurant.models import Booking, Menu
from datetime import datetime

class BookingTest(TestCase):
    def test_get_item(self):
        booking = Booking.objects.create(
            name="Lily Brown",
            no_of_guests=4,
            booking_date=datetime(2026, 4, 26, 16, 30) # April 25, 2026 at 4:30PM
        )
        self.assertEqual(str(booking), f"{booking.name} : {booking.booking_date}")

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="Pecan Pie", 
            price=5.99, 
            inventory=20)
        self.assertEqual(str(item), "Pecan Pie : 5.99")
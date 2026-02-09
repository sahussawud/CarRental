from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from managecar.models import Car, Rent, Promo


class DetailViewsTest(TestCase):
    def setUp(self):
        """Set up test data for detail views"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Add necessary permissions
        add_rent_perm = Permission.objects.get(codename='add_rent')
        view_rent_perm = Permission.objects.get(codename='view_rent')
        self.user.user_permissions.add(add_rent_perm, view_rent_perm)
        
        self.car = Car.objects.create(
            name='Test Car',
            years='2022',
            color='Red',
            category='SED',
            type_gear='AUTO',
            number_seat=4,
            number_door=4,
            status='AVAILABLE',
            price=100.00,
        )

    def test_detail_view(self):
        """Test detail view"""
        response = self.client.get(reverse('detail', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

    def test_booking_view_get(self):
        """Test booking view GET request"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('booking', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

    def test_reservation_list_view(self):
        """Test reservation list view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('reservation_list'))
        self.assertEqual(response.status_code, 200)

    def test_confirm_view(self):
        """Test confirm view"""
        # Create a rent object first
        rent = Rent.objects.create(
            status='Pending',
            total_price=500.00,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=5),
            car_id=self.car,
            customer_id=self.user,
        )
        
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('confirm', args=[rent.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

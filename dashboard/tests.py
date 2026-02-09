from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from managecar.models import Car, Rent


class DashboardViewsTest(TestCase):
    def setUp(self):
        """Set up test data for dashboard views"""
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='testpass123',
            is_staff=True
        )
        # Add necessary permissions
        change_rent_perm = Permission.objects.get(codename='change_rent')
        change_car_perm = Permission.objects.get(codename='change_car')
        self.staff_user.user_permissions.add(change_rent_perm, change_car_perm)
        
        self.regular_user = User.objects.create_user(
            username='regularuser',
            password='testpass123'
        )
        
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
        
        self.rent = Rent.objects.create(
            status='Pending',
            total_price=500.00,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=5),
            car_id=self.car,
            customer_id=self.regular_user,
        )

    def test_dashboard_view(self):
        """Test dashboard view"""
        self.client.login(username='staffuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

    def test_rent_approve_view(self):
        """Test approving a rent order"""
        self.client.login(username='staffuser', password='testpass123')
        response = self.client.post(reverse('rent_approve', args=[self.rent.id]))
        self.assertRedirects(response, reverse('dashboard'))
        updated_rent = Rent.objects.get(id=self.rent.id)
        self.assertEqual(updated_rent.status, 'Approved')

    def test_rent_deny_view(self):
        """Test denying a rent order"""
        self.client.login(username='staffuser', password='testpass123')
        response = self.client.post(reverse('rent_deniel', args=[self.rent.id]))
        self.assertRedirects(response, reverse('dashboard'))
        updated_rent = Rent.objects.get(id=self.rent.id)
        self.assertEqual(updated_rent.status, 'Denied')

from django.test import TestCase, Client
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from managecar.models import Car, Promo, Rent


class CarModelTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.car_data = {
            'name': 'Test Car',
            'years': '2022',
            'color': 'Red',
            'category': 'SED',
            'type_gear': 'AUTO',
            'number_seat': 4,
            'number_door': 4,
            'status': 'AVAILABLE',
            'price': 100.00,
        }

    def test_create_car(self):
        """Test creating a car object"""
        car = Car.objects.create(**self.car_data)
        self.assertEqual(car.name, 'Test Car')
        self.assertEqual(car.years, '2022')
        self.assertEqual(car.status, 'AVAILABLE')

    def test_car_string_representation(self):
        """Test the string representation of a car"""
        car = Car.objects.create(**self.car_data)
        expected_str = f"{car.name} {car.years} ({car.status})"
        self.assertEqual(str(car), expected_str)


class PromoModelTest(TestCase):
    def setUp(self):
        """Set up test data for promo"""
        self.promo_data = {
            'name': 'Summer Sale',
            'desc': 'Discount for summer season',
            'promotion_code': 'SUMMER20',
            'discount_percent': 20.0,
            'minimum_cost': 100.0,
            'expire_day': timezone.now() + timedelta(days=30),
            'is_active': True,
        }

    def test_create_promo(self):
        """Test creating a promo object"""
        promo = Promo.objects.create(**self.promo_data)
        self.assertEqual(promo.name, 'Summer Sale')
        self.assertEqual(promo.promotion_code, 'SUMMER20')


class RentModelTest(TestCase):
    def setUp(self):
        """Set up test data for rent"""
        self.user = User.objects.create_user(
            username='testuser',
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
        
        self.rent_data = {
            'status': 'Pending',
            'total_price': 500.00,
            'start_date': timezone.now(),
            'end_date': timezone.now() + timedelta(days=5),
            'car_id': self.car,
            'customer_id': self.user,
        }

    def test_create_rent(self):
        """Test creating a rent object"""
        rent = Rent.objects.create(**self.rent_data)
        self.assertEqual(rent.status, 'Pending')
        self.assertEqual(rent.total_price, 500.00)


class ManageCarViewsTest(TestCase):
    def setUp(self):
        """Set up test data for views"""
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='testpass123',
            is_staff=True
        )
        # Add necessary permissions
        change_car_perm = Permission.objects.get(codename='change_car')
        self.staff_user.user_permissions.add(change_car_perm)
        
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

    def test_car_hide_view(self):
        """Test hiding a car"""
        self.client.login(username='staffuser', password='testpass123')
        response = self.client.post(reverse('car_hide', args=[self.car.id]))
        self.assertRedirects(response, reverse('car_dashboard'))
        updated_car = Car.objects.get(id=self.car.id)
        self.assertEqual(updated_car.status, 'HIDE')

    def test_car_unhide_view(self):
        """Test unhiding a car"""
        # First hide the car
        self.car.status = 'HIDE'
        self.car.save()
        
        self.client.login(username='staffuser', password='testpass123')
        response = self.client.post(reverse('car_unhide', args=[self.car.id]))
        self.assertRedirects(response, reverse('car_dashboard'))
        updated_car = Car.objects.get(id=self.car.id)
        self.assertEqual(updated_car.status, 'AVAILABLE')

    def test_car_dashboard_view(self):
        """Test car dashboard view"""
        self.client.login(username='staffuser', password='testpass123')
        response = self.client.get(reverse('car_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

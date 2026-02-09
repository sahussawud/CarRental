from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from managecar.models import Car


class HomepageViewsTest(TestCase):
    def setUp(self):
        """Set up test data for homepage views"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='testpass123',
            is_staff=True
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

    def test_homepage_view(self):
        """Test homepage view"""
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

    def test_homepage_search_functionality(self):
        """Test search functionality on homepage"""
        # Test search by name
        response = self.client.post(reverse('homepage'), {
            'selection': 'name',
            'keyword': 'Test Car'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

        # Test search by year
        response = self.client.post(reverse('homepage'), {
            'selection': 'year',
            'keyword': '2022'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

        # Test search by color
        response = self.client.post(reverse('homepage'), {
            'selection': 'color',
            'keyword': 'Red'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

    def test_car_detail_view(self):
        """Test car detail view"""
        response = self.client.get(reverse('car_detail', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Car')

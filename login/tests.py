from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LoginViewsTest(TestCase):
    def setUp(self):
        """Set up test data for login views"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )

    def test_login_view_get(self):
        """Test login view GET request"""
        response = self.client.get(reverse('my_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')

    def test_login_view_post_valid_credentials(self):
        """Test login view POST with valid credentials"""
        response = self.client.post(reverse('my_login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertRedirects(response, reverse('homepage'))

    def test_login_view_post_invalid_credentials(self):
        """Test login view POST with invalid credentials"""
        response = self.client.post(reverse('my_login'), {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Missing Username OR Password')

    def test_logout_view(self):
        """Test logout view"""
        # First log in
        self.client.login(username='testuser', password='testpass123')
        
        # Then log out
        response = self.client.get(reverse('my_logout'))
        self.assertRedirects(response, reverse('my_login'))

    def test_create_account_view_get(self):
        """Test create account view GET request"""
        response = self.client.get(reverse('createAccount'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')

    def test_create_account_view_post_success(self):
        """Test create account view POST with valid data"""
        response = self.client.post(reverse('createAccount'), {
            'agree-term': 'on',
            'username': 'newuser',
            'password': 'newpass123',
            'password_again': 'newpass123',
            'fname': 'New',
            'lname': 'User',
            'email': 'newuser@example.com'
        })
        self.assertRedirects(response, reverse('my_login'))
        
        # Check that the user was created
        user_exists = User.objects.filter(username='newuser').exists()
        self.assertTrue(user_exists)

    def test_create_account_view_post_password_mismatch(self):
        """Test create account view POST with mismatched passwords"""
        response = self.client.post(reverse('createAccount'), {
            'agree-term': 'on',
            'username': 'newuser',
            'password': 'newpass123',
            'password_again': 'differentpass',
            'fname': 'New',
            'lname': 'User',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Password do not match')

    def test_change_password_view_get(self):
        """Test change password view GET request"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('ChangePassword'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Change Password')

    def test_change_password_view_post_success(self):
        """Test change password view POST with matching passwords"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('ChangePassword'), {
            'password': 'newpassword123',
            'password_again': 'newpassword123'
        })
        self.assertContains(response, 'Change Password Successfully')

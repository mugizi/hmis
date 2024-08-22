# account/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserCreationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_user_url = reverse('adduser')  # This should match the name in your urls.py
        self.login_url = reverse('login')  # This should match the name in your urls.py
    
    def test_add_user_success(self):
        response = self.client.post(self.add_user_url, {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'phone': '1234567890',
            'role': 'Test Role',
            'password': 'testpassword123',
            'confirm-password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

        User = get_user_model()
        user = User.objects.get(email='testuser@example.com')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.phone, '1234567890')
        self.assertEqual(user.role, 'Test Role')
        self.assertTrue(user.check_password('testpassword123'))

    def test_add_user_password_mismatch(self):
        response = self.client.post(self.add_user_url, {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'phone': '1234567890',
            'role': 'Test Role',
            'password': 'testpassword123',
            'confirm-password': 'differentpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Passwords do not match.")
        
        User = get_user_model()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email='testuser@example.com')

    def test_add_user_missing_field(self):
        response = self.client.post(self.add_user_url, {
            'name': 'Test User',
            'email': '',
            'phone': '1234567890',
            'role': 'Test Role',
            'password': 'testpassword123',
            'confirm-password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "All fields are required.")
        
        User = get_user_model()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email='testuser@example.com')

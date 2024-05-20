from django.test import TestCase
from django.urls import reverse
from ..models import User
from django.contrib.auth import authenticate

class LogoutViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', password='testpassword')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')       
        response = self.client.post(reverse('logout'))        
        self.assertFalse(authenticate(username='testuser', password='testpassword'))      
        self.assertRedirects(response, reverse('index'))

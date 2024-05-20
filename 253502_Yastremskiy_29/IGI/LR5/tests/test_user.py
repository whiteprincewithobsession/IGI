from django.test import TestCase
from ..models import User
from datetime import datetime, timedelta

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', birth_date=datetime(2000, 1, 1))

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('12345'))
        self.assertFalse(self.user.is_client)

    def test_user_age_calculation(self):
        birth_date = datetime.now() - timedelta(days=365 * 20)
        user = User.objects.create_user(username='age_test_user', password='12345', birth_date=birth_date)
        
        self.assertEqual(user.age, 19)

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')

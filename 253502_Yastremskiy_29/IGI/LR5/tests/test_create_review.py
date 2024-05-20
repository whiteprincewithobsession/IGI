from ..models import User
from django.test import TestCase
from ..models import Review
from django.urls import reverse

class ReviewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_review(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('create_review'), {'text': 'Test review text'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

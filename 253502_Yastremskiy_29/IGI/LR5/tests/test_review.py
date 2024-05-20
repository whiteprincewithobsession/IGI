from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from ..models import Review

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='password123')

        Review.objects.create(user=user, text='Test review', created_at=timezone.now())

    def test_review_str(self):
        review = Review.objects.get(id=1)
        current_time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(str(review), f'Review by testuser at {current_time}')

from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import DiscountCoupon
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string


class PromocodesViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_request(self):
        response = self.client.get(reverse('promocodes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promocodes.html')

    def test_post_request_valid_form(self):
        expiration_date = datetime.now() + timedelta(days=30)
        data = {
            'code': 'fwfa',
            'expiration_date': expiration_date,
            'discount_percentage': 10,
            'max_usage_count': 100,
        }
        response = self.client.post(reverse('promocodes'), data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(DiscountCoupon.objects.count(), 1)
        self.assertRedirects(response, reverse('promocodes'))

    def test_post_request_invalid_form(self):
        expiration_date = datetime.now() - timedelta(days=1)
        data = {
        'expiration_date': expiration_date,
        'discount_percentage': 10,
        'max_usage_count': 100,
    }
        response = self.client.post(reverse('promocodes'), data)
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(DiscountCoupon.objects.exists())


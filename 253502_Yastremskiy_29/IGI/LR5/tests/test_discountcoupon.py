from django.test import TestCase
from catalog.app_models.coupon import DiscountCoupon
from django.utils import timezone

class DiscountCouponModelTest(TestCase):
    def setUp(self):
        self.coupon = DiscountCoupon.objects.create(
            code='TESTCODE123',
            discount_percentage=20,
            expiration_date=timezone.now() + timezone.timedelta(days=30),
            max_usage_count=5,
            current_usage_count=2
        )

    def test_coupon_str(self):
        self.assertEqual(str(self.coupon), 'TESTCODE123 - 20% off')

    def test_generate_code(self):
        original_code = self.coupon.code
        self.coupon.generate_code()
        new_code = self.coupon.code
        self.assertNotEqual(original_code, new_code)

    def test_is_expired(self):
        expired_coupon = DiscountCoupon.objects.create(
            code='EXPIRED123',
            discount_percentage=10,
            expiration_date=timezone.now() - timezone.timedelta(days=1),
            max_usage_count=5
        )
        self.assertTrue(expired_coupon.is_expired())
        self.assertFalse(self.coupon.is_expired())

    def test_is_valid(self):
        expired_coupon = DiscountCoupon.objects.create(
            code='EXPIRED123',
            discount_percentage=10,
            expiration_date=timezone.now() - timezone.timedelta(days=1),
            max_usage_count=5
        )
        self.assertFalse(expired_coupon.is_valid())
        self.assertTrue(self.coupon.is_valid())

    def test_use_coupon(self):
        used_coupon = DiscountCoupon.objects.create(
            code='USED123',
            discount_percentage=15,
            expiration_date=timezone.now() + timezone.timedelta(days=30),
            max_usage_count=3,
            current_usage_count=3
        )
        self.assertFalse(used_coupon.use_coupon())
        self.assertTrue(self.coupon.use_coupon())
        self.assertEqual(self.coupon.current_usage_count, 3)
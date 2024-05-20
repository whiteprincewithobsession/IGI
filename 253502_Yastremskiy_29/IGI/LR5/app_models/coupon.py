from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.validators import MinValueValidator, MaxValueValidator

class DiscountCoupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount_percentage = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=30))
    max_usage_count = models.PositiveIntegerField(default=1)
    current_usage_count = models.PositiveIntegerField(default=0)

    def generate_code(self):
        self.code = get_random_string(length=10)

    def is_expired(self):
        return self.expiration_date <= timezone.now()

    def is_valid(self):
        return not self.is_expired() and self.current_usage_count < self.max_usage_count

    def use_coupon(self):
        if self.is_valid():
            self.current_usage_count += 1
            self.save()
            return True
        return False
    
    def __str__(self):
        return f"{self.code} - {self.discount_percentage}% off"

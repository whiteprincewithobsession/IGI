from django.db import models
from catalog.app_models.category import Category
from catalog.app_models.order import Order
from catalog.app_models.tag import Tag
from catalog.app_models.company_info import CompanyInfo
from catalog.app_models.vacancy import Vacancy
from catalog.app_models.coupon import DiscountCoupon
from catalog.app_models.news import NewsArticle
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_master = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    @property
    def age(self):
        if self.birth_date:
            today = datetime.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return None

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User, related_name='user_groups')

    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Review by {self.user.username} at {self.created_at}"





# Create your models here.

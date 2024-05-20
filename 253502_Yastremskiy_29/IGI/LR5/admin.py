from django.contrib import admin
from catalog.models import User, Review, Profile, Group
from catalog.app_models.category import Category
from catalog.app_models.order import Order
from catalog.app_models.tag import Tag
from catalog.app_models.company_info import CompanyInfo
from catalog.app_models.vacancy import Vacancy
from catalog.app_models.coupon import DiscountCoupon
from catalog.app_models.news import NewsArticle
from catalog.app_models.faq import FAQ

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(CompanyInfo)
admin.site.register(Vacancy)
admin.site.register(DiscountCoupon)
admin.site.register(NewsArticle)
admin.site.register(FAQ)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Group)
# Register your models here.

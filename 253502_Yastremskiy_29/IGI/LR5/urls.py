from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_company, name='about_company'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('profile/', views.profile_view, name='profile'),
    path('contacts/', views.contacts, name='contacts'),
    path('create-review/', views.create_review, name='create_review'),
    path('review-list/', views.review_list, name='review_list'),
    path('accept_order/<int:order_id>/', views.accept_order, name='accept_order'),
    path('promocodes/', views.promocodes, name='promocodes'),
    path('faq/', views.faq_view, name='faq'),
    path('news/', views.news_page, name='news_page'),
    path('order-status-pie-chart/', views.order_status_pie_chart, name='order_status_pie_chart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

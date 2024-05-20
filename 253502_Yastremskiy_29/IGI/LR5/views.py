from django.shortcuts import render, redirect
from django.db.models import Sum
from catalog.forms import RegistrationForm, OrderCreateForm, ReviewForm, PromocodeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import django.utils.timezone as timezone
import datetime
import pytz as tz
from catalog.models import User, Review
from catalog.app_models.company_info import CompanyInfo
from catalog.app_models.vacancy import Vacancy
from catalog.app_models.order import Order
from catalog.app_models.news import NewsArticle
from catalog.app_models.coupon import DiscountCoupon
from catalog.app_models.faq import FAQ
from django.contrib.auth.decorators import login_required
import requests
import calendar
from django.utils.crypto import get_random_string
import pandas as pd
from plotly.offline import plot
import plotly.express as px


def index(request):
    total_order_amount = None
    if request.user.is_authenticated and request.user.is_master:
        total_order_amount = Order.objects.filter(status='Pending').aggregate(total_price=Sum('price'))['total_price']

    
    if request.method == 'GET' and 'sort_by' in request.GET:
        sort_by = request.GET.get('sort_by')
        if sort_by == 'price_asc':
            free_orders = Order.objects.filter(status="Pending").order_by('price')
        elif sort_by == 'price_desc':
            free_orders = Order.objects.filter(status="Pending").order_by('-price')
    else:
        free_orders = Order.objects.filter(status="Pending") 

    order_form = OrderCreateForm(request.POST or None)
    if request.method == 'POST':
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            order_form.save_m2m()
            return redirect('index') 

    context = {
        'total_order_amount': total_order_amount,
        'free_orders': free_orders,
        'order_form': order_form, 
    }
    return render(request, 'index.html', context)
    
@login_required(login_url='/catalog/login/')
def accept_order(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(pk=order_id)
        if order.status == 'Pending' and order.master == 'None':
            order.master = request.user.username
            order.status = 'Accepted'
            order.save()
            return redirect('index')
    return redirect('index')

def about_company(request):
    company_data = CompanyInfo.objects.first()
    curr_tz = get_timezone()
    tz_info = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).tzinfo 
    tz_info2 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    utc_date = datetime.datetime.now(tz_info).strftime("%d/%m/%y")
    utc_time =datetime.datetime.now(tz_info).strftime("%H:%M:%S")
    year = tz_info2.year
    month = tz_info2.month
    cal = calendar.monthcalendar(year, month)

    context = {
        'timezone' : curr_tz,
        'company_data' : company_data,
        'current_date_utc': utc_date,
        'current_time_utc': utc_time,
        'calendar': cal
    }    
    return render(request, 'about_company.html', context)


def privacy_policy(request):
    cat_fact = get_random_cat_fact()
    ip_address = get_ip_address()
    context = {'cat_fact': cat_fact, 'ip_address': ip_address}
    return render(request, 'privacy_policy.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            users = User.objects.filter(username=form.cleaned_data['username'])
            if users.count() == 0:
                user = form.save()
                user.is_client = True
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Пользователь с данным именем существует')
                return render(request, 'login.html', {'error_message': 'Пользователь с данным именем существует.'})
                
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Username: {username}, Password: {password}")

        users = User.objects.filter(username=username)
        print(users)
        user = authenticate(request, username=username, password=password)
        if users.exists():
            if password == users[0].password:
                user = users[0]
            #print(f"User object: {user}")

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Пользователь не найден.')
                return render(request, 'login.html', {'error_message': 'Неправильное имя пользователя или пароль.'})
        else:
            messages.error(request, 'Пользователь не найден.')
            return render(request, 'login.html', {'error_message': 'Пользователь не найден.'})
    else:
        return render(request, 'login.html', {'error_message': ''})
    
def logout_view(request):
    logout(request)
    return redirect('index')

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy.html', {'vacancies': vacancies})

@login_required(login_url='/catalog/login/')
def profile_view(request):
    if request.user.is_master:
        user_orders = Order.objects.filter(master=request.user)
    else:
        user_orders = Order.objects.filter(user=request.user)

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            if order.status == 'Pending':
                order.delete() 
            else:
                order.status = 'Finished'
                order.save()

    context = {
        'user_orders': user_orders
    }
    return render(request, 'profile.html', context)

def contacts(request):
    masters = User.objects.filter(is_master=True)
    return render(request, 'contacts.html', {'masters': masters})

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def get_random_cat_fact():
    try:
        response = requests.get('https://catfact.ninja/fact')
        data = response.json()
        if response.status_code == 200:
            return data.get('fact')
        else:
            return 'Failed to fetch cat fact.'
    except Exception as e:
        return 'An error occurred while fetching cat fact: ' + str(e)
    
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        data = response.json()
        if response.status_code == 200:
            return data.get('ip')
        else:
            return 'Failed to fetch IP address.'
    except Exception as e:
        return 'An error occurred while fetching IP address: ' + str(e)
    
def get_timezone():
    try:
        ip = get_ip_address()
        response = requests.get(f'https://ipinfo.io/{ip}/geo')
        if response.status_code == 200:
                data = response.json()
                city = data["city"]
                country = data["country"]
                region = data["region"]
                tz = data["timezone"]
                return tz
    except Exception as e:
        return 'Error: ' + str(e)
           
 
def promocodes(request):
    if request.method == 'POST':
        form = PromocodeForm(request.POST)
        if form.is_valid():
            expiration_date = form.cleaned_data['expiration_date']
            discount_percentage = form.cleaned_data['discount_percentage']
            max_usage_count = form.cleaned_data['max_usage_count']

            discount_coupon = DiscountCoupon.objects.create(
                expiration_date=expiration_date,
                discount_percentage=discount_percentage,
                max_usage_count=max_usage_count,
                current_usage_count=0
            )
            discount_coupon.code = get_random_string(length=10)
            discount_coupon.save()
            messages.success(request, 'Promocode added successfully.')
            return redirect('promocodes')
    else:
        form = PromocodeForm()
    promocodes = DiscountCoupon.objects.all()
    
    context = {
        'form': form,
        'promocodes': promocodes,
    }
    return render(request, 'promocodes.html', context)

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})

def news_page(request):
    latest_article = NewsArticle.objects.latest('publication_date')
    articles = NewsArticle.objects.all()
    context = {
        'latest_article': latest_article,
        'articles' : articles,       
    }
    return render(request, 'news_page.html', context)

def order_status_pie_chart(request):
    orders = Order.objects.all().values('status')
    df = pd.DataFrame(orders)
    
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']

    fig = px.pie(status_counts, names='status', values='count', title='Распределение статусов заказов')

    plot_div = plot(fig, output_type='div', include_plotlyjs=True)
    
    return render(request, 'order_status_pie_chart.html', {'plot_div': plot_div})
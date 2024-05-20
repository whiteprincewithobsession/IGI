from django import forms
from django.core.exceptions import ValidationError
from catalog.models import User, Review
from catalog.app_models.order import Order
from catalog.app_models.coupon import DiscountCoupon
import re
import datetime
import secrets

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=20, label='Phone Number')
    birth_date = forms.DateField(label='Date of Birth')
    role = forms.ChoiceField(label='Role', choices=[('client', 'Client'), ('master', 'Master')], widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'birth_date', 'role']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        pattern = re.compile(r'^\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError('Invalid phone number format. Use format +375 (29) XXX-XX-XX')
        return phone_number

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        today = datetime.datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(age)
        if age < 18:
            raise forms.ValidationError('Age must be 18+')
        return birth_date

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        role = self.cleaned_data['role']

        if role == 'client':
            user.is_client = True
            user.is_master = False
        elif role == 'master':
            user.is_client = False
            user.is_master = True

        if commit:
            user.save()
        return user
    
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'total_amount', 'description', 'category', 'price']
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        
class PromocodeForm(forms.ModelForm):
    class Meta:
        model = DiscountCoupon
        fields = ['code', 'expiration_date', 'discount_percentage', 'max_usage_count']
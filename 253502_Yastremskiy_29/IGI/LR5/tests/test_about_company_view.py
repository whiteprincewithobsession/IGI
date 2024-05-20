from django.test import TestCase
from django.urls import reverse
from catalog.app_models.company_info import CompanyInfo
from datetime import datetime
import calendar
import pytz

class AboutCompanyViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        company_data = CompanyInfo.objects.create(
            company_name='Test Company',
            history='Test history',
            logo = 'D:\studying\git_igi\253502_Yastremskiy_29\IGI\LR5\media\catalog\static\logos\workshop.jpg'
        )

    def test_about_company_view(self):
        response = self.client.get(reverse('about_company'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('company_data', response.context)
        self.assertIn('current_date_utc', response.context)
        self.assertIn('current_time_utc', response.context)
        self.assertIn('calendar', response.context)

        company_data = response.context['company_data']
        self.assertEqual(company_data.company_name, 'Test Company')
        self.assertEqual(company_data.history, 'Test history')

        current_date_utc = response.context['current_date_utc']
        current_time_utc = response.context['current_time_utc']
        utc_now = datetime.now(pytz.timezone('Europe/Moscow'))
        expected_date = utc_now.strftime('%d/%m/%y')
        expected_time = utc_now.strftime('%H:%M:%S')
        self.assertEqual(current_date_utc, expected_date)
        self.assertEqual(current_time_utc, expected_time)

        self.assertIn('calendar', response.context)
        cal = response.context['calendar']
        today = datetime.now().day
        self.assertIn(today, sum(cal, []))
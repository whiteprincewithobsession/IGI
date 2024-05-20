from django.test import TestCase
from catalog.app_models.company_info import CompanyInfo

class CompanyInfoModelTest(TestCase):
    def setUp(self):
        self.company = CompanyInfo.objects.create(
            company_name='Test Company',
            history='This is a test company with a long history.',
            logo='path/to/test/image.png'
        )

    def test_company_info_str(self):
        self.assertEqual(str(self.company), 'Test Company')

    def test_company_info_name(self):
        self.assertEqual(self.company.company_name, 'Test Company')

    def test_company_info_history(self):
        self.assertEqual(self.company.history, 'This is a test company with a long history.')

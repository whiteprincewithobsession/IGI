from django.test import TestCase
from catalog.app_models.category import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category', description='This is a test category.')

    def test_category_str(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'Test Category')

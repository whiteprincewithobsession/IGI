from django.test import TestCase
from catalog.app_models.tag import Tag

class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Test Tag')

    def test_tag_str(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(str(tag), 'Test Tag')

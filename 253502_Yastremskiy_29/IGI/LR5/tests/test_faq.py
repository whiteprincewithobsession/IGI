from django.test import TestCase
from catalog.app_models.faq import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question='What is Django?',
            answer='Django is a high-level Python web framework.'
        )

    def test_faq_str(self):
        self.assertEqual(str(self.faq), 'What is Django?')

    def test_faq_question(self):
        self.assertEqual(self.faq.question, 'What is Django?')

    def test_faq_answer(self):
        self.assertEqual(self.faq.answer, 'Django is a high-level Python web framework.')

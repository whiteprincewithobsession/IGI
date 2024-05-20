from django.test import TestCase
from django.urls import reverse
from catalog.app_models.faq import FAQ
from ..views import faq_view
from django.shortcuts import render

class FAQViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        FAQ.objects.create(question="Test Question 1", answer="Test Answer 1")
        FAQ.objects.create(question="Test Question 2", answer="Test Answer 2")

    def test_faq_view(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')

    def test_faq_view_context(self):
        response = self.client.get(reverse('faq'))
        faqs = response.context['faqs']
        self.assertEqual(len(faqs), 2)
        self.assertEqual(faqs[0].question, "Test Question 1")
        self.assertEqual(faqs[0].answer, "Test Answer 1")
        self.assertEqual(faqs[1].question, "Test Question 2")
        self.assertEqual(faqs[1].answer, "Test Answer 2")
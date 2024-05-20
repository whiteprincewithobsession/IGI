from django.test import TestCase
from django.urls import reverse
from catalog.app_models.news import NewsArticle
from django.utils import timezone
from datetime import timedelta


class NewsPageViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.article = NewsArticle.objects.create(
            title="Test Article",
            content="Test Content",
            image = 'path/to/test/image.png',
            publication_date=timezone.now() - timedelta(days=1) 
        )

    def test_news_page_view(self):
        url = reverse('news_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('latest_article', response.context)
        latest_article = response.context['latest_article']
        self.assertEqual(latest_article.title, "Test Article")

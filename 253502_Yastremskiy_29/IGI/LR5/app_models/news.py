from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

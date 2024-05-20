from django.db import models

class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='catalog/static/logos')
    history = models.TextField()

    def __str__(self):
        return self.company_name

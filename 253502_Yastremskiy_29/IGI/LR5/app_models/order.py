from django.db import models
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(default='')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.TextField(default='Pending')
    description = models.TextField(default='No description')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    category = models.TextField(default='Unknown')
    master = models.TextField(default = 'None')
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

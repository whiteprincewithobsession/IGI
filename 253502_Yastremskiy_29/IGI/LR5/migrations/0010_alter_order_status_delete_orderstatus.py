# Generated by Django 5.0.6 on 2024-05-13 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_order_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(default='Pending'),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]

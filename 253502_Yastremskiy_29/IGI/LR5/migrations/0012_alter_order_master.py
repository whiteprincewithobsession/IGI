# Generated by Django 5.0.6 on 2024-05-13 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='master',
            field=models.TextField(default='None'),
        ),
    ]

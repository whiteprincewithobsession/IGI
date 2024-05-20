# Generated by Django 5.0.6 on 2024-05-16 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_companyinfo_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcoupon',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='discountcoupon',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 15, 16, 58, 1, 292748, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-16 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_faq_alter_discountcoupon_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcoupon',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 15, 17, 40, 39, 91803, tzinfo=datetime.timezone.utc)),
        ),
    ]

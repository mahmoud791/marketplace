# Generated by Django 3.1.4 on 2020-12-18 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_customer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-22 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0023_monthly_bid_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthly_bid_details',
            name='no_of_chits',
        ),
    ]

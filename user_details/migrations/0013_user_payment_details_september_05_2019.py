# Generated by Django 3.0.3 on 2020-04-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0012_auto_20200419_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_payment_details',
            name='September_05_2019',
            field=models.BooleanField(default=False),
        ),
    ]
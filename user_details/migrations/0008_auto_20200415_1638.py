# Generated by Django 3.0.3 on 2020-04-15 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0007_auto_20200415_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_payment_details',
            old_name='April_05_2021',
            new_name='August_05_2019',
        ),
        migrations.RenameField(
            model_name='user_payment_details',
            old_name='February_05_2021',
            new_name='July_05_2019',
        ),
        migrations.RenameField(
            model_name='user_payment_details',
            old_name='January_05_2021',
            new_name='June_05_2019',
        ),
        migrations.RenameField(
            model_name='user_payment_details',
            old_name='March_05_2021',
            new_name='May_05_2019',
        ),
        migrations.RemoveField(
            model_name='user_payment_details',
            name='May_05_2021',
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('chit_draw_amount', models.IntegerField()),
                ('amount_to_pay', models.IntegerField()),
                ('commission_amount', models.IntegerField()),
            ],
        ),
    ]

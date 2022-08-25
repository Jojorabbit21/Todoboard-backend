# Generated by Django 4.1 on 2022-08-25 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Board Title')),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='Date Start')),
                ('date_exp', models.DateField(default=datetime.datetime(2022, 9, 1, 14, 15, 55, 707317), verbose_name='Date Expiration')),
            ],
        ),
    ]
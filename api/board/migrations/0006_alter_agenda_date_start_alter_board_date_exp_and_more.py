# Generated by Django 4.1 on 2022-08-26 01:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_agenda_date_start_alter_board_date_exp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2022, 8, 26, 1, 35, 10, 400497, tzinfo=datetime.timezone.utc), verbose_name='Date Start'),
        ),
        migrations.AlterField(
            model_name='board',
            name='date_exp',
            field=models.DateField(default=datetime.datetime(2022, 9, 2, 1, 35, 10, 400497, tzinfo=datetime.timezone.utc), verbose_name='Date Expiration'),
        ),
        migrations.AlterField(
            model_name='board',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2022, 8, 26, 1, 35, 10, 400497, tzinfo=datetime.timezone.utc), verbose_name='Date Start'),
        ),
    ]

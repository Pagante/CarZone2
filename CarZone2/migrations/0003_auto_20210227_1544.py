# Generated by Django 3.1.7 on 2021-02-27 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarZone2', '0002_auto_20210227_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 27, 15, 44, 52, 72599)),
        ),
    ]

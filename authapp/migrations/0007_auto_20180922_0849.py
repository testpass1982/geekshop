# Generated by Django 2.1 on 2018-09-22 05:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20180917_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 24, 5, 49, 34, 971563, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-16 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0002_alter_cotacoes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotacoes',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 16, 21, 28, 6, 375035, tzinfo=utc)),
        ),
    ]

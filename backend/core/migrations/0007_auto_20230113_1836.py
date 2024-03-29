# Generated by Django 3.2.16 on 2023-01-13 18:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230113_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 18, 36, 47, 550127, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 18, 36, 47, 554331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quote',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 18, 36, 47, 553694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2023, 1, 13, 18, 36, 47, 546880, tzinfo=utc)),
        ),
    ]

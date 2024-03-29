# Generated by Django 3.2.16 on 2023-01-13 19:30

import core.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20230113_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.address'),
        ),
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2023, 1, 13, 19, 30, 37, 681034, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.business_logo_file_path),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 19, 30, 37, 685384, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quote',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 19, 30, 37, 684720, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2023, 1, 13, 19, 30, 37, 676120, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-13 17:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230113_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 17, 15, 34, 374092, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 17, 15, 34, 378208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='quote',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 17, 15, 34, 377581, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='social_media',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Tik Tok', 'Tik Tok'), ('Instagram', 'Instagram'), ('YouTube', 'YouTube'), ('Other', 'Other')], default='Facebook', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2023, 1, 13, 17, 15, 34, 370311, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-29 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=datetime.datetime(2021, 8, 29, 8, 10, 16, 578826, tzinfo=utc), max_length=10, verbose_name='이름'),
            preserve_default=False,
        ),
    ]
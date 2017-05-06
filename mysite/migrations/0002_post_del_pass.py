# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='del_pass',
            field=models.CharField(default=datetime.datetime(2016, 7, 26, 5, 35, 19, 813000, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]

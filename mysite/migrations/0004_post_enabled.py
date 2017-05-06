# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_post_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]

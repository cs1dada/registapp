# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_post_del_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nickname',
            field=models.CharField(default=b'\xe4\xb8\x8d\xe9\xa1\x98\xe6\x84\x8f\xe9\x80\x8f\xe6\xbc\x8f\xe8\xba\xab\xe4\xbb\xbd\xe7\x9a\x84\xe4\xba\xba', max_length=10),
        ),
    ]

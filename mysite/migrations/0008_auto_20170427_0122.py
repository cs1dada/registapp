# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 01:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_diary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mood',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Mood',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
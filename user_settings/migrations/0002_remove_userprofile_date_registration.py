# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_registration',
        ),
    ]

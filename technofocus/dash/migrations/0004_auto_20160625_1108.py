# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20160625_1053'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='authors',
            new_name='author',
        ),
    ]

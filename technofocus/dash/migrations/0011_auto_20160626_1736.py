# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0010_paperlist_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperlist',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]

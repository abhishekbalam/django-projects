# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_paperlist_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperlist',
            name='file',
            field=models.FileField(default=1, upload_to='files/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]

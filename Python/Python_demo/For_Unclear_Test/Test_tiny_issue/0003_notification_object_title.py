# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2020-05-12 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20170613_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='object_title',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
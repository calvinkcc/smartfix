# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-06 19:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_auto_20180605_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=250, validators=[django.core.validators.EmailValidator()]),
        ),
    ]

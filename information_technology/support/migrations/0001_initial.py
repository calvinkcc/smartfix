# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-06 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_of_contact', models.CharField(choices=[('S', 'Services'), ('B', 'Business Inquiries'), ('O', 'Others')], max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('textarea', models.CharField(max_length=2500)),
            ],
        ),
    ]

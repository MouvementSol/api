# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_token', '0005_auto_20170206_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='companyname',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

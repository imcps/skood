# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-15 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180115_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=1000)),
            ],
        ),
    ]

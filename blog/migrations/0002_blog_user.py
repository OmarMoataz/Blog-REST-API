# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ManyToManyField(to='person.Person'),
        ),
    ]
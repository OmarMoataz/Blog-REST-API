# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, max_length=280, null=True)),
            ],
        ),
    ]
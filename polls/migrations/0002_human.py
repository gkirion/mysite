# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('height', models.IntegerField(default=0)),
                ('date_of_birth', models.DateTimeField()),
            ],
        ),
    ]

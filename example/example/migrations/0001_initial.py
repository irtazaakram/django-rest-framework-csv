# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField()),
                ('speaker', models.TextField()),
                ('scheduled_at', models.DateTimeField()),
            ],
        ),
    ]

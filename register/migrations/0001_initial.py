# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

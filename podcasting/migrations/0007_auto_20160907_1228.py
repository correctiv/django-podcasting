# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-07 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0006_auto_20160905_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='itunes_url',
            field=models.URLField(blank=True, null=True, verbose_name='Itunes url'),
        ),
        migrations.AddField(
            model_name='show',
            name='spotify_url',
            field=models.URLField(blank=True, null=True, verbose_name='Spotify url'),
        ),
    ]
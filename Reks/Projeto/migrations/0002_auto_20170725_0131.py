# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projeto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(max_length=512),
        ),
    ]
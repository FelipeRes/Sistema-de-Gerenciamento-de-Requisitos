# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisitos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisito',
            name='estado',
            field=models.CharField(choices=[('E', 'Espera'), ('A', 'Aberto'), ('F', 'Fechado'), ('C', 'Cancelado')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]

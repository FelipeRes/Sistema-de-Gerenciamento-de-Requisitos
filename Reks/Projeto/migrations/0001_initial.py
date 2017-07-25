# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complexidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=125)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prioridade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=125)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=125)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipos', to='Projeto.Projeto')),
            ],
        ),
        migrations.AddField(
            model_name='prioridade',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prioridades', to='Projeto.Projeto'),
        ),
        migrations.AddField(
            model_name='complexidade',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complexidades', to='Projeto.Projeto'),
        ),
    ]
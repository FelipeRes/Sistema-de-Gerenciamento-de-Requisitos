# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 19:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Complexidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=125)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('E', 'Espera'), ('A', 'Aberto'), ('F', 'Fechado'), ('C', 'Cancelado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Cargo')),
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
            name='Requisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=125)),
                ('especificacao', models.CharField(max_length=1024)),
                ('complexidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Complexidade')),
                ('dependencias', models.ManyToManyField(related_name='_requisito_dependencias_+', to='requisitos.Requisito')),
                ('desenvolvedor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Estado')),
                ('prioridade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Prioridade')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=125)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('A', 'Administrador'), ('D', 'Desenvolvedor')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='requisito',
            name='tipo',
            field=models.ManyToManyField(to='requisitos.Tipo'),
        ),
        migrations.AddField(
            model_name='prioridade',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Projeto'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.TipoPerfil'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complexidade',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Projeto'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitos.Projeto'),
        ),
    ]
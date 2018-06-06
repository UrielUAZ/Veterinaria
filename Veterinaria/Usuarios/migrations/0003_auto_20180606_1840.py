# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 18:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_auto_20180605_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$', 'No se permiten numeros ni espacios en blanco, solo se permiten letras,')], verbose_name='Nombre del usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(7), django.core.validators.RegexValidator('^[0-9]+$', 'No se permiten numeros ni espacios en blanco, solo se permiten letras,')], verbose_name='Telefono'),
        ),
    ]
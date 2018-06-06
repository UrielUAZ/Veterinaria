# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 19:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_auto_20180606_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[a-zA-Z]+$', 'No se permiten numeros ni espacios en blanco, solo se permiten letras,')], verbose_name='Nombre del usuario'),
        ),
    ]

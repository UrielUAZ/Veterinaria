# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 07:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(7)], verbose_name='Telefono'),
        ),
    ]

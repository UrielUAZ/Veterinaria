# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Usuario(User):
    validacion_entrada = RegexValidator(r'^[a-zA-Z]+$',
    'No se permiten numeros ni espacios en blanco, solo se permiten letras,')
    validacion_numeros = RegexValidator(r'^[0-9]+$',
    'No se permiten espacios en blanco ni letras, solo se permiten numeros,')
    nombre = models.CharField('Nombre del usuario', max_length=200, validators=[MinLengthValidator(3), validacion_entrada])
    telefono = models.CharField('Telefono', max_length=10, validators=[MinLengthValidator(7), validacion_numeros], unique=True, null=True)
	

    def __str__(self):
        return self.nombre




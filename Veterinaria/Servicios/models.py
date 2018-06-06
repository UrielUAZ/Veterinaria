# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinLengthValidator
from django.db import models

class Tipo_Servicio(models.Model):
	tipo = models.CharField('Tipo de servicio', max_length=200, validators=[MinLengthValidator(5)])
	def __str__(self):
		return self.tipo


class Servicio(models.Model):
	nombre = models.CharField('Nombre del servicio', max_length=200, validators=[MinLengthValidator(5)])
	precio = models.DecimalField('Precio', decimal_places=2, max_digits=15)
	tipo_servicio = models.ForeignKey(Tipo_Servicio)

	def __str__(self):
		return self.nombre


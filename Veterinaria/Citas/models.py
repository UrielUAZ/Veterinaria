# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Usuarios.models import Usuario
from Servicios.models import Servicio



class Cita(models.Model):

	usuario = models.ForeignKey(Usuario)
	servicio = models.ForeignKey(Servicio)
	fecha = models.DateField()
	hora = models.DateTimeField()
	

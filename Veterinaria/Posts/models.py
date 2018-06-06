# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Noticias.models import Noticia
from Usuarios.models import Usuario

class Post(models.Model):

	fecha = models.DateField()
	noticia = models.ForeignKey(Noticia)
	usuario = models.ForeignKey(Usuario)


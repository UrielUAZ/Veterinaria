# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinLengthValidator
from django.db import models

class Noticia(models.Model):

    nombre = models.TextField('Noticia', validators=[MinLengthValidator(10)])
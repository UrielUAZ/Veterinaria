# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Servicios.models import Servicio
from django.shortcuts import render

def home_page(request):
    servicios = Servicio.objects.all()
    return render(request, "home.html", {'servicios':servicios})

def inicio(request):
    return render(request, "login.html")
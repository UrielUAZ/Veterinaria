# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from Servicios.models import Servicio
from Servicios.models import Tipo_Servicio
from Servicios.forms import FormServicio
from Servicios.forms import FormTipoServicio
from Servicios.forms import ServicioEdit
from Servicios.forms import TipoServicioEdit

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "lista_servicios.html", {'servicios':servicios})

def nuevo_servicio(request):
    if request.method == 'POST':
        form = FormServicio(request.POST)
        if form.is_valid():
            servicio = form.save()
            servicio.save()
            return redirect('lista_servicios')
    else:
        form = FormServicio()
    return render(request, "nuevo_servicio.html", {'form':form})


def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == "POST":
        form = ServicioEdit(request.POST, instance=servicio)
        if form.is_valid():
            servicio = form.save()
            servicio.save()
            return redirect('lista_servicios')
    else:
        form = ServicioEdit(instance=servicio)
    return render(request, 'editar_servicio.html',{'form':form, })

def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.delete()
    return redirect('lista_servicios')


def lista_tipo_servicio(request):
    servicios = Tipo_Servicio.objects.all()
    return render(request, "lista_tipo_servicio.html", {'servicios':servicios})

def nuevo_tipo_servicio(request):
    if request.method == 'POST':
        form = FormTipoServicio(request.POST)
        if form.is_valid():
            servicio = form.save()
            servicio.save()
            return redirect('lista_tipo_servicio')
    else:
        form = FormTipoServicio()
    return render(request, "nuevo_tipo_servicio.html", {'form':form})


def editar_tipo_servicio(request, pk):
    servicio = get_object_or_404(Tipo_Servicio, pk=pk)
    if request.method == "POST":
        form = TipoServicioEdit(request.POST, instance=servicio)
        if form.is_valid():
            servicio = form.save()
            servicio.save()
            return redirect('lista_tipo_servicio')
    else:
        form = TipoServicioEdit(instance=servicio)
    return render(request, 'editar_tipo_servicio.html',{'form':form, })

def eliminar_tipo_servicio(request, pk):
    servicio = get_object_or_404(Tipo_Servicio, pk=pk)
    servicio.delete()
    return redirect('lista_tipo_servicio')
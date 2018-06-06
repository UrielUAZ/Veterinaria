# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from Citas.models import Cita
from Citas.forms import FormCita
from Citas.forms import CitaEdit


def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, "lista_citas.html", {'citas':citas})

def nueva_cita(request):
    if request.method == 'POST':
        form = FormCita(request.POST)
        if form.is_valid():
            cita = form.save()
            cita.save()
            return redirect('lista_citas')
    else:
        form = FormCita()
    return render(request, "nueva_cita.html", {'form':form})


def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == "POST":
        form = CitaEdit(request.POST, instance=cita)
        if form.is_valid():
            cita = form.save()
            cita.save()
            return redirect('lista_citas')
    else:
        form = CitaEdit(instance=cita)
    return render(request, 'editar_cita.html',{'form':form, })

def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    cita.delete()
    return redirect('lista_citas')
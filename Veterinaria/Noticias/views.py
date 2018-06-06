# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from Noticias.models import Noticia
from Noticias.forms import FormNoticia
from Noticias.forms import NoticiaEdit

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, "lista_noticias.html", {'noticias':noticias})

def nueva_noticia(request):
    if request.method == 'POST':
        form = FormNoticia(request.POST)
        if form.is_valid():
            noticia = form.save()
            noticia.save()
            return redirect('lista_noticias')
    else:
        form = FormNoticia()
    return render(request, "nueva_noticia.html", {'form':form})


def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = NoticiaEdit(request.POST, instance=noticia)
        if form.is_valid():
            noticia = form.save()
            noticia.save()
            return redirect('lista_noticias')
    else:
        form = NoticiaEdit(instance=noticia)
    return render(request, 'editar_noticia.html',{'form':form, })

def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    noticia.delete()
    return redirect('lista_noticias')
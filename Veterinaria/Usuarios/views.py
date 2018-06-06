# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from Usuarios.models import Usuario
from forms import FormUsuario
from forms import UsuarioEdit

def principal(request):
    return render(request, "administrar.html")


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "lista_usuarios.html", {'usuarios':usuarios})

def nuevo_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            return redirect('lista_usuarios')
    else:
        form = FormUsuario()
    return render(request, "nuevo_usuario.html", {'form':form})


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioEdit(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioEdit(instance=usuario)
    return render(request, 'editar_usuario.html',{'form':form, })


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('lista_usuarios')
	

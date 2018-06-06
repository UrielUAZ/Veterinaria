# -*- coding:utf-8 -*-
from django import forms
from models import Usuario

class FormUsuario(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_2 = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Usuario
		fields = (
			'username',
			'password',
			'password_2',
			'first_name',
			'last_name',
			'email',
			'nombre',
			'telefono',
		)
		
class UsuarioEdit(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'nombre',
			'telefono',
		)

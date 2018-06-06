# -*- coding:utf-8 -*-
from django import forms
from models import Noticia

class FormNoticia(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = (
			'nombre',
		)
		
class NoticiaEdit(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = (
			'nombre',
		)

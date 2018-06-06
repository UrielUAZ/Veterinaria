# -*- coding:utf-8 -*-
from django import forms
from models import Servicio
from models import Tipo_Servicio

class FormServicio(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = (
			'nombre',
			'precio',
			'tipo_servicio',
		)
		
class ServicioEdit(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = (
			'nombre',
			'precio',
			'tipo_servicio',
		)


class FormTipoServicio(forms.ModelForm):
	class Meta:
		model = Tipo_Servicio
		fields = (
			'tipo',
		)
		
class TipoServicioEdit(forms.ModelForm):
	class Meta:
		model = Tipo_Servicio
		fields = (
			'tipo',
		)
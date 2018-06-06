# -*- coding:utf-8 -*-
from django import forms
from models import Cita


class FormCita(forms.ModelForm):
	class Meta:
		model = Cita
		fields = (
			'usuario',
			'servicio',
			'fecha',
			'hora',
		)
		
class CitaEdit(forms.ModelForm):
	class Meta:
		model = Cita
		fields = (
            'usuario',
            'servicio',
            'fecha',
			'hora',
		)
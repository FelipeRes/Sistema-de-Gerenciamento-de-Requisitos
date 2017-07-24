from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User

class RegistrarProjeto(forms.Form):
	nome = forms.CharField(required = True)
	descricao = forms.CharField(required = True)

	def is_valid(self):
		valid = True
		if super(RegistrarProjeto, self).is_valid() == False:
			self.adiciona_mensagem('Verifique seus campos.')
			valid = False
		return valid

	def adiciona_mensagem(self, mensagem):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(mensagem)
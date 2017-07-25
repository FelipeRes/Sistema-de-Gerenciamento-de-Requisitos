from django import forms
from django.contrib.auth.models import User
from requisitos.models import *

class RegistrarProjeto(forms.ModelForm):
	class Meta:
		model = Projeto
		fields = ['nome', 'descricao']

	def is_valid(self):
		valid = True
		if super(RegistrarProjeto, self).is_valid() == False:
			self._errors.append('Verifique seus campos.')
			valid = False
		return valid

	def adiciona_mensagem(self, mensagem):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(mensagem)


class AdicionarTipo(forms.ModelForm):
	class Meta:
		model = Tipo
		fields = ['nome']

class AdicionarPrioridade(forms.ModelForm):
	class Meta:
		model = Prioridade
		fields = ['label', 'valor']

class AdicionarComplexidade(forms.ModelForm):
	class Meta:
		model = Complexidade
		fields = ['label', 'valor']

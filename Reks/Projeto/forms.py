from django.forms import ModelForm
from Projeto.models import *

class ProjetoFormulario(ModelForm):
	class Meta:
		model = Projeto
		fields = ['nome', 'descricao']
		exclude = ['user']
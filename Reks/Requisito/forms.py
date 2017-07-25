from django.forms import Form
from django import forms
from .models import *

class RequisitoForm(forms.Form):
	nome = forms.CharField(required=True)
	especificacao = forms.CharField(required=True)
	estado = forms.ChoiceField(choices=Requisito.ESTADOS)
	tipo = forms.ModelMultipleChoiceField(queryset=None)
	prioridade = forms.ModelMultipleChoiceField(queryset=None)
	complexidade = forms.ModelMultipleChoiceField(queryset=None)

	def __init__(self,*args,**kwargs):
		projeto_id = args[0]
		super(RequisitoForm,self).__init__((),**kwargs)
		projeto = Projeto.objects.get(id=projeto_id)
		print(Tipo.objects.filter(projeto=projeto))
		self.fields['tipo'] = forms.ModelMultipleChoiceField(queryset=Tipo.objects.filter(projeto=projeto), widget=forms.CheckboxSelectMultiple)
		self.fields['prioridade'] = forms.ModelMultipleChoiceField(queryset=Prioridade.objects.filter(projeto=projeto), widget=forms.RadioSelect)
		self.fields['complexidade'] = forms.ModelMultipleChoiceField(queryset=Complexidade.objects.filter(projeto=projeto), widget=forms.RadioSelect)
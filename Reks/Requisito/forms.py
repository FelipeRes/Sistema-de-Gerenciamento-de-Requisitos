from django.forms import Form
from django import forms
from Requisito.models import *

class RequisitoForm(forms.Form):
	class Meta():
		model = Requisito
		exclude = ['projeto', 'dependencias']
	'''nome = forms.CharField(required=True)
	especificacao = forms.CharField(required=True)
	estado = forms.ChoiceField(choices=Requisito.ESTADOS)
	tipo = forms.ModelChoiceField(queryset=Tipo.objects.all())
	prioridade = forms.ModelChoiceField(queryset=Prioridade.objects.all())
	complexidade = forms.ModelChoiceField(queryset=Complexidade.objects.all())

	def __init__(self,*args,**kwargs):
		projeto_id = args[0]
		super(RequisitoForm,self).__init__((),**kwargs)
		projeto = Projeto.objects.get(id=projeto_id)
		print(Tipo.objects.filter(projeto=projeto))
		self.fields['tipo'] = forms.ModelMultipleChoiceField(queryset=Tipo.objects.filter(projeto=projeto), widget=forms.CheckboxSelectMultiple)
		self.fields['prioridade'] = forms.ModelMultipleChoiceField(queryset=Prioridade.objects.filter(projeto=projeto), widget=forms.RadioSelect)
		self.fields['complexidade'] = forms.ModelMultipleChoiceField(queryset=Complexidade.objects.filter(projeto=projeto), widget=forms.RadioSelect)
		'''
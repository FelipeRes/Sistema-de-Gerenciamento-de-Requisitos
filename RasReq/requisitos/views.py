from django.shortcuts import render, HttpResponse, redirect
from requisitos.models import Projeto
from django.views.generic.base import View
from requisitos.forms import *

# Create your views here.
class NovoProjeto(View):
	template = 'novo_projeto.html'

	def get(self,request):
		form = RegistrarProjeto()
		return render(request, self.template,{'from':form})

	def post(self,request):
		form = RegistrarProjeto(request.POST)
		if form.is_valid():
			dados = form.cleaned_data
			projeto = Projeto.objects.create(nome = dados['nome'],descricao = dados['descricao'])
			projeto.save()
			return redirect('index')
		return render(request, self.template, {'form' : form})




def index(request):
	projetos = Projeto.objects.all()
	return render(request,'index.html', {'projetos':projetos})

def exibir(request, projeto_id):
	projeto = Projeto.objects.get(id=projeto_id)
	tipoForm = AdicionarTipo()
	data = projeto.propiedades()
	data['formTipo'] = tipoForm
	return render(request,'exibir_projeto.html', data)

def criar_requisito(request, projeto_id):
	projeto = Projeto.objects.get(id=projeto_id)
	return render(request, 'novo_requisito.html', projeto.propiedades())


from django.shortcuts import render, HttpResponse, redirect
from Projeto.forms import ProjetoFormulario
from django.views.generic.base import View
from django.http import JsonResponse
from Projeto.models import *

class ProjetoExibir(View):
	template = 'projeto.html'
	def get(self, request, projeto_id):
		projeto = Projeto.objects.get(id=projeto_id)
		return render(request, self.template, projeto.propiedades())

class ProjetoNovo(View):
	template = 'projeto_novo.html'
	def get(self, request):
		form = ProjetoFormulario()
		return render(request, self.template, {'form':form})
	def post(self, request):
		form = ProjetoFormulario(request.POST)
		if form.is_valid():
			dados = form.cleaned_data
			projeto = Projeto.objects.create(nome = dados['nome'],descricao = dados['descricao'])
			projeto.save()
			return redirect('index')
		return render(request, self.template, {'form' : form})

def AdicionarTipo(request):
	nome = request.GET.get("nome")
	projeto = Projeto.objects.get(id=request.GET.get("projeto_id"))
	tipo = Tipo(nome=nome, projeto=projeto)
	tipo.save()
	data = projeto.propiedades()
	return render(request,'projeto.html',data)

def DeletarTipo(request):
	tipo = Tipo.objects.get(id=request.GET.get("tipo_id"))
	tipo.delete()
	return render(request,'projeto.html')

def AdicionarPrioridade(request):
	label = request.GET.get("label")
	valor = request.GET.get("valor")
	projeto = Projeto.objects.get(id=request.GET.get("projeto_id"))
	prioridade = Prioridade(label=label, valor=valor,projeto=projeto)
	prioridade.save()
	data = projeto.propiedades()
	return render(request,'projeto.html',data)

def DeletarPrioridade(request):
	prioridade = Prioridade.objects.get(id=request.GET.get("prioridade_id"))
	prioridade.delete()
	return render(request,'projeto.html')

def AdicionarComplexidade(request):
	label = request.GET.get("label")
	valor = request.GET.get("valor")
	projeto = Projeto.objects.get(id=request.GET.get("projeto_id"))
	complexidade = Complexidade(label=label, valor=valor,projeto=projeto)
	complexidade.save()
	data = projeto.propiedades()
	return render(request,'projeto.html',data)

def DeletarComplexidade(request):
	complexidade = Complexidade.objects.get(id=request.GET.get("complexidade_id"))
	complexidade.delete()
	return render(request,'projeto.html')

def Editar(request, projeto_id):
	projeto = Projeto.objects.get(id=projeto_id)
	return render(request, 'projeto_editar.html', projeto.propiedades())
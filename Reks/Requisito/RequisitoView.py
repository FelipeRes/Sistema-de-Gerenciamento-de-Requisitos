from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from Requisito.models import *
from Projeto.models import *
from Requisito.forms import *
from django import forms

class RequisitoNovo(View):
	template = 'novo_requisito.html'

	def get(self, request, projeto_id):
		projeto = Projeto.objects.get(id=projeto_id)
		data = projeto.propiedades()
		return render(request, self.template, data)

	def post(self, request, projeto_id):
		projeto = Projeto.objects.get(id=projeto_id)
		dados = request.POST
		requisito = Requisito(nome= request.POST.get('nome'),
			especificacao= request.POST.get('especificacao'),
			projeto=projeto,
			estado= request.POST.get('estado'))
		requisito.prioridade = Prioridade.objects.filter(projeto=projeto,label=request.POST.get('prioridade'))[0]
		requisito.complexidade = Complexidade.objects.filter(projeto=projeto,label=request.POST.get('complexidade'))[0]
		requisito.save()
		return redirect('exibir_projeto',projeto_id)

class RequisitoExibir(View):
	template = 'requisito.html'
	def get(self, request, projeto_id, requisito_id):
		requisito = Requisito.objects.get(id=requisito_id)
		return render(request, self.template, {'requisito':requisito})

def AlterarDependencias(request, projeto_id, requisito_id):
	requisito = Requisito.objects.get(id=requisito_id)
	projeto = requisito.projeto
	requisito.dependencias.clear()
	requisito.save()
	for requisito_dependente_id in request.POST.getlist('reqs'):
		requisito.dependencias.add(Requisito.objects.get(id=requisito_dependente_id))
	return redirect('exibir_projeto', projeto.id)

def AlterarEstado(request, projeto_id, requisito_id):
	requisito = Requisito.objects.get(id=requisito_id)
	projeto = requisito.projeto
	requisito.estado = request.POST.get('estado')
	requisito.save()
	return redirect('exibir_projeto', projeto.id)

def AlterarPrioridade(request, projeto_id, requisito_id):
	requisito = Requisito.objects.get(id=requisito_id)
	projeto = requisito.projeto
	requisito.prioridade = Prioridade.objects.filter(projeto=projeto,label=request.POST.get('prioridade'))[0]
	requisito.save()
	return redirect('exibir_projeto', projeto.id)

def AlterarComplexidade(request, projeto_id, requisito_id):
	requisito = Requisito.objects.get(id=requisito_id)
	projeto = requisito.projeto
	requisito.complexidade = Complexidade.objects.filter(projeto=projeto,label=request.POST.get('complexidade'))[0]
	requisito.save()
	return redirect('exibir_projeto', projeto.id)


from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from Requisito.models import *
from Projeto.models import *
from Requisito.forms import *
from django import forms

class RequisitoNovo(View):
	template = 'requisito.html'

	def get(self, request, projeto_id):
		projeto = Projeto.objects.get(id=projeto_id)
		data = projeto.propiedades()
		return render(request, self.template, data)

	def post(self, request, projeto_id):
		template = 'requisito.html'
		projeto = Projeto.objects.get(id=projeto_id)
		dados = request.POST
		requisito = Requisito(nome= request.POST.get('nome'),
			especificacao= request.POST.get('especificacao'),
			projeto=projeto,
			estado= request.POST.get('estado'))
		requisito.save()
		list_tipo = []
		for tipo in request.POST.getlist('tipo'):
			list_tipo.append(Tipo.objects.filter(projeto=projeto, nome=tipo))
		requisito.tipo = list_tipo
		requisito.prioridade = Prioridade.objects.filter(projeto=projeto,label=request.POST.get('prioridade'))
		requisito.complexidade= complexidade.objects.filter(projeto=projeto,label=request.POST.get('complexidade'))
		requisito.save()
		return HttpResponse('deu certo')
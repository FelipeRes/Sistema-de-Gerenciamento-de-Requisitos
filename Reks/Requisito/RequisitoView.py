from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from Requisito.models import *
from Projeto.models import *
from Requisito.forms import *
from django import forms

class RequisitoNovo(View):
	template = 'requisito.html'

	def get(self, request, projeto_id):
		form = RequisitoForm(projeto_id)
		projeto = Projeto.objects.get(id=projeto_id)
		data = projeto.propiedades()
		data['form'] = form
		return render(request, self.template, data)

	def post(self, request, projeto_id):
		form = RequisitoForm(projeto_id,request.POST)
		projeto = Projeto.objects.get(id=projeto_id)
		template = 'requisito.html'
		if form.is_valid():
			requisito = form.save()
			requisito.projeto = projeto
			requisito.save()
			return HttpResponse('deu certo')
		return HttpResponse(form._errors)
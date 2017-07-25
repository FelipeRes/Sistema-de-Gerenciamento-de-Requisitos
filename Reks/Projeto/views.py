from django.shortcuts import render, HttpResponse
from Projeto.models import *
# Create your views here.

def index(request):
	projetos = Projeto.objects.all()
	return render(request, 'index.html', {'projetos':projetos})

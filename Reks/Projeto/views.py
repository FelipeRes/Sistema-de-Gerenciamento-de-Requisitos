from django.shortcuts import render, HttpResponse
from Projeto.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def index(request):
	projetos = Projeto.objects.all()
	return render(request, 'index.html', {'projetos':projetos})

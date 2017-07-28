from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Projeto(models.Model):
	nome = models.CharField(max_length=45)
	descricao = models.TextField(max_length=512)
	usuario = models.ForeignKey(User, related_name = 'administra', on_delete = models.CASCADE)
	def propiedades(self):
		return {'projeto' : self,
		'tipos': self.tipos.all(), 
		'prioridades': self.prioridades.all(), 
		'complexidades':self.complexidades.all(),
		'requisitos':self.requisitos.all().order_by('-prioridade__valor')}
	def __str__(self):
		return self.nome

	@property
	def maiorClasse(self):
		lista = []
		for d in self.requisitos.all():
			lista.append(d.classe)
		gambs = []
		if len(lista) == 0:
			return gambs
		for i in range(max(lista)):
			gambs.append(i+1)
		return gambs


class Tipo(models.Model):
	nome = models.CharField(max_length=125)
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tipos')
	def __str__(self):
		return self.nome

class Prioridade(models.Model):
	label = models.CharField(max_length=125)
	valor = models.IntegerField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='prioridades')
	def __str__(self):
		return self.label

class Complexidade(models.Model):
	label = models.CharField(max_length=125)
	valor = models.IntegerField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='complexidades')
	def __str__(self):
		return self.label

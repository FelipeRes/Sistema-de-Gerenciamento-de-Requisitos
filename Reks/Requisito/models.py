from django.db import models
from Projeto.models import *

# Create your models here.
class Requisito(models.Model):
	ESTADOS = (('E', 'Espera'), ('A', 'Aberto'), ('F', 'Fechado'), ('C','Cancelado'))
	nome = models.CharField(max_length=125)
	especificacao = models.TextField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='requisitos')
	estado = models.CharField(max_length=1, choices = ESTADOS)
	tipo = models.ManyToManyField(Tipo)
	prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
	complexidade = models.ForeignKey(Complexidade, on_delete=models.CASCADE)
	dependencias = models.ManyToManyField("self", related_name='dependentes', symmetrical=False)

	def __str__(self):
		return self.nome

	@property
	def dependenciasData(self):
		return self.dependencias.all()

	@property
	def nivel(self):
		lista = []
		return len(self.calculoNivel(lista))

	def calculoNivel(self, lista):
		for d in self.dependencias.all():
			d.calculoNivel(lista)
			if d not in lista:
				lista.append(d)
		return lista

	@property 
	def classe(self):
		dependencia = self.dependencias.all()
		valor = 0
		menores_valores = []
		for d in dependencia:
			menores_valores.append(d.classe)
		if len(menores_valores) > 0:
			valor = valor + max(menores_valores) 
		return valor + 1

	@property
	def impacto(self):
		lista = []
		return len(self.calculoImpacto(lista))

	def calculoImpacto(self, lista):
		for d in self.dependentes.all():
			d.calculoImpacto(lista)
			if d not in lista:
				lista.append(d)
		return lista



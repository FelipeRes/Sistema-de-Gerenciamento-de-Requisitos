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
	dependencias = models.ManyToManyField("self")

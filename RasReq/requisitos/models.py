from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Projeto(models.Model):
	nome = models.CharField(max_length=45)
	descricao = models.CharField(max_length=512)

class Cargo(models.Model):
	nome = models.CharField(max_length=45)
	descricao = models.CharField(max_length=512)
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

class TipoPerfil(models.Model):
	TIPOS = (('A', 'Administrador'), ('D', 'Desenvolvedor'))
	estado = models.CharField(max_length=1, choices = TIPOS)

class Perfil(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	tipo = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE)
	cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

class Estado(models.Model):
	ESTADOS = (('E', 'Espera'), ('A', 'Aberto'), ('F', 'Fechado'), ('C','Cancelado'))
	estado = models.CharField(max_length=1, choices = ESTADOS)

class Tipo(models.Model):
	nome = models.CharField(max_length=125)
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

class Prioridade(models.Model):
	label = models.CharField(max_length=125)
	valor = models.IntegerField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

class Complexidade(models.Model):
	label = models.CharField(max_length=125)
	valor = models.IntegerField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

class Requisito(models.Model):
	nome = models.CharField(max_length=125)
	especificacao = models.CharField(max_length=1024)
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	tipo = models.ManyToManyField(Tipo)
	prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
	complexidade = models.ForeignKey(Complexidade, on_delete=models.CASCADE)
	dependencias = models.ManyToManyField("self")
	desenvolvedor = models.ManyToManyField(User)



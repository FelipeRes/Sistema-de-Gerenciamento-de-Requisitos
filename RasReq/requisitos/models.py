from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Projeto(models.Model):
	nome = models.CharField(max_length=45)
	descricao = models.CharField(max_length=512)
	def propiedades(self):
		return {'projeto' : self,
		'tipos': self.tipos.all(), 
		'prioridades': self.prioridades.all(), 
		'complexidades':self.complexidades.all()}

class Cargo(models.Model):
	nome = models.CharField(max_length=45)
	descricao = models.CharField(max_length=512)
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)


class Perfil(models.Model):
	TIPOS = (('A', 'Administrador'), ('D', 'Desenvolvedor')) 
	tipo = models.CharField(max_length=1, choices = TIPOS)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)	

class Tipo(models.Model):
	nome = models.CharField(max_length=125)
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tipos')

class Prioridade(models.Model):
	label = models.CharField(max_length=125)
	valor = models.IntegerField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='prioridades')

class Complexidade(models.Model):
	label = models.CharField(max_length=125)
	valor = models.IntegerField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='complexidades')

class Requisito(models.Model):
	ESTADOS = (('E', 'Espera'), ('A', 'Aberto'), ('F', 'Fechado'), ('C','Cancelado'))
	nome = models.CharField(max_length=125)
	especificacao = models.TextField()
	projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='requisitos')
	estado = models.CharField(max_length=1, choices = ESTADOS)
	prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
	complexidade = models.ForeignKey(Complexidade, on_delete=models.CASCADE)
	dependencias = models.ManyToManyField("self")
	desenvolvedor = models.ManyToManyField(User)



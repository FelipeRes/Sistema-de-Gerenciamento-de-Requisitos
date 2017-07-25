from django.db import models

# Create your models here.
class Projeto(models.Model):
	nome = models.CharField(max_length=45)
	descricao = models.TextField(max_length=512)
	def propiedades(self):
		return {'projeto' : self,
		'tipos': self.tipos.all(), 
		'prioridades': self.prioridades.all(), 
		'complexidades':self.complexidades.all()}
	def __str__(self):
		return self.nome

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

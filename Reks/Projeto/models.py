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

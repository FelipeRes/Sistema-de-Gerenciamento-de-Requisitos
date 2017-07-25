from django.conf.urls import url, include
from Projeto import views
from Projeto import projetoView
from Projeto.projetoView import *

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^projeto/novo$', ProjetoNovo.as_view(), name='novo_projeto'),
	url(r'^projeto/(?P<projeto_id>\d+)$', ProjetoExibir.as_view(), name='exibir_projeto'),
	url(r'^projeto/(?P<projeto_id>\d+)/', include('Requisito.urls')),
	url(r'^projeto/(?P<projeto_id>\d+)/editar$', views.index, name='editar_projeto'),
	url(r'^ajax/adicionarTipo$', projetoView.AdicionarTipo, name='adicionar_tipo'),
	url(r'^ajax/deletarTipo$', projetoView.DeletarTipo, name='deletar_tipo'),
	url(r'^ajax/adicionarPrioridade$', projetoView.AdicionarPrioridade, name='adicionar_prioridade'),
	url(r'^ajax/deletarPrioridade$', projetoView.DeletarPrioridade, name='deletar_prioridade'),
	url(r'^ajax/adicionarComplexidade$', projetoView.AdicionarComplexidade, name='adicionar_complexidade'),
	url(r'^ajax/deletarComplexidade', projetoView.DeletarComplexidade, name='deletar_complexidade'),
]
from django.conf.urls import url, include
from Requisito import views
from Requisito import RequisitoView
from Requisito.RequisitoView import *

urlpatterns = [
	url(r'^requisito/novo$', RequisitoNovo.as_view(), name='novo_requisito'),
	url(r'^requisito/(?P<requisito_id>\d+)$', RequisitoExibir.as_view(), name='exibir_requisito'),
	url(r'^requisito/(?P<requisito_id>\d+)/alterar$', RequisitoView.AlterarDependencias, name='alterar_dependencia'),
	url(r'^requisito/(?P<requisito_id>\d+)/estado$', RequisitoView.AlterarEstado, name='alterar_estado'),
	url(r'^requisito/(?P<requisito_id>\d+)/prioridade$', RequisitoView.AlterarPrioridade, name='alterar_prioridade'),
	url(r'^requisito/(?P<requisito_id>\d+)/complexidade$', RequisitoView.AlterarComplexidade, name='alterar_complexidade'),
]

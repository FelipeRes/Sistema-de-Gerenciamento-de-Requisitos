from django.conf.urls import url, include
from Requisito import views
from Requisito.RequisitoView import *

urlpatterns = [
	url(r'^requisito/novo$', RequisitoNovo.as_view(), name='novo_requisito'),
	#url(r'^requisito/(?P<requisito_id>\d+)$', ProjetoExibir.as_view(), name='exibir_projeto'),
	#url(r'^requisito/(?P<requisito_id>\d+)/editar$', views.index, name='editar_projeto'),
]

from django.conf.urls import url, include
from Requisito import views
from Requisito.RequisitoView import *

urlpatterns = [
	url(r'^requisito/novo$', RequisitoNovo.as_view(), name='novo_requisito'),
	url(r'^requisito/(?P<requisito_id>\d+)$', RequisitoExibir.as_view(), name='exibir_requisito'),
]

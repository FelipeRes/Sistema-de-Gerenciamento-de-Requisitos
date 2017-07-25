from django.conf.urls import url, include
from requisitos import views
from requisitos.views import NovoProjeto

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projeto/(?P<projeto_id>\d+)$', views.exibir, name='exibir_projeto'),
    url(r'^projeto/(?P<projeto_id>\d+)/tipo/novo/$', views.adicionar_tipo, name='adicionar_tipo'),
    url(r'^requisito/novo/(?P<projeto_id>\d+)$', views.criar_requisito, name='criar_requisito'),
    url(r'^projeto/novo$', NovoProjeto.as_view(), name='novo_projeto'),

]
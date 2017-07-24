from django.conf.urls import url, include
from requisitos import views
from requisitos.views import NovoProjeto

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projeto/novo$', NovoProjeto.as_view(), name='novo_projeto'),
]
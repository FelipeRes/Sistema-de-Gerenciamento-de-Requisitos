from django.conf.urls import url, include
from requisitos import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
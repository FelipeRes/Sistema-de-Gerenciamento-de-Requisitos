from django.conf.urls import url, include
from Usuario import views
from Usuario.views import *
from django.contrib.auth import views

urlpatterns = [
	url(r'^registrar/$', RegistrarUsuario.as_view(), name='registrar'),
	url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(template_name='login.html'), name='logout'),
	url(r'^redirect/$', views.LoginView.as_view(template_name='login.html'), name='login'),
]
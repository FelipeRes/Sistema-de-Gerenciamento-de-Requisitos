from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class RegistrarUsuario(View):
	template = 'registrar.html'

	@method_decorator(login_required(login_url='/login/'))
	def get(self, request):
		return render(request, self.template, {"form": UserCreationForm() })

	@method_decorator(login_required(login_url='/login/'))
	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/login/")
		else:
			return render(request, "registrar.html", {"form": form})
		return render(request, "registrar.html", {"form": UserCreationForm() })

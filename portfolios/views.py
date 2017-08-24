from django.shortcuts import render
from .models import projeto


def portfolios_exibir(request):
	
	meuprojeto = projeto.objects.all()
	context = {'meuprojeto': meuprojeto} 
	return render(request, 'projetos/index.html', context)



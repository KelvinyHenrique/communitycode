from django.shortcuts import render

def portfolios_exibir(request):
	return render(request, 'projetos/index.html', {})


from django.shortcuts import render


def index(request):
	context = {
		'title': 'Home'
	}
	return render(request, 'main/home/index.html', context)


def company(request):
	context = {
		'title': 'Company'
	}
	return render(request, 'main/company/index.html', context)

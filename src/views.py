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


def demo(request):
	context = {
		'title': 'Demo'
	}
	return render(request, 'main/demo/index.html', context)


def tutorials(request):
	context = {
		'title': 'Tutorials'
	}
	return render(request, 'tutorials/index.html', context)


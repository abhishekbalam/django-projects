from django.shortcuts import render

# Create your views here.
def website_load(request):
	return render(request, 'website/index.html',{})

def portfolio(request):
	return render(request, 'website/portfolio.html',{})

def services(request):
	return render(request, 'website/services.html',{})

def contact(request):
	return render(request, 'website/contact.html',{})

def about(request):
	return render(request, 'website/about.html',{})

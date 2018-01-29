from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import PaperList
from .forms import UploadForm
from django.views.static import serve
import os
# Create your views here.

def admin_login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'dash/login.html', c)

def download(request):
	return HttpResponse("hello")

def admin_logout(request):
	return HttpResponse("You Are Logged out!")

def dash_load(request):
	return render(request, 'dash/dash.html',{})

def upload(request):
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			List = form.save(commit=False)
			#file = PaperList(file = request.FILES['file'])
			#file.save()
			List.save()
			return redirect(paper_list)
			
	else:
		form = UploadForm()
		return render(request, 'dash/upload.html',{'form':form})


def simple(request):
	return render(request, 'dash/simple.html',{})

def download(request):
	return serve(request, os.path.basename(MEDIA_URL), os.path.dirname(MEDIA_URL))

def paper_list(request):
	list = PaperList.objects.all()
	return render(request, 'dash/paperlist.html',{'list':list})

def auth_view(request):
	username = request.POST.get('username', '')
	password =request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponse('logged In!!')
	else:
		print("fuck")
		return HttpResponse('fuck')

def logout(request):
	auth.logout(request)
	return HttpResponse('logged out')
from django.shortcuts import render, HttpResponse 

def home(request):
	return render(request, 'accounts/login.html'),


# Create your views here.

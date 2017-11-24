from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
	return render(request,'profiles.html') 


def profile(request):
	args = {'users': request.users}
	return render(request, 'profile.html',args)
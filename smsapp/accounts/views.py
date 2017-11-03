from django.shortcuts import render, HttpResponse 

def home(request):
	items = [1,2,3,4,'A','B','C'] 
	name = 'SimiDev'
	args = {'myname': name, 'numbers':items}
	return render(request,'accounts/home.html',args)

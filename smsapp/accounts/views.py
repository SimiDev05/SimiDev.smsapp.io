from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
	items = [1,2,3,4,'A','B','C'] 
	name = 'SimiDev'
	args = {'myname': name, 'numbers':items}
	return render(request,'accounts/home.html',args)

def register(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts') 
	else:
		form = UserCreationForm()


		args = {'form': form}
		return render(request, 'accounts/reg_form.html',args)

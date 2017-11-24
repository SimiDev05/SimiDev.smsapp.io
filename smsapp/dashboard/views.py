from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm 



def gallery(request):

	return render(request, 'dashboard/gallery.html')

def view_profile(request):
	args = {'user': request.user}
	return render(request,'dashboard/profile.html', args) 

def edit_profile(request):
	if request.method == 'POST':
		form = UserChangeForm(request.POST, instance=request.user) 

		if form.is_valid():
			form.save()
			return redirect('/dashboard/profile')

	else:
		form = UserChangeForm(instance=request.user)
		args = {'form' : form}
		return render(request, 'dashboard/edit_profile.html',args)

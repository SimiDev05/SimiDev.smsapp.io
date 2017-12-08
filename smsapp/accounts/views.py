from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def home(request):
	numbers = [1,2,3,4,'A','B','C'] 
	name = 'SimiDev'
	args = {'myname': name, 'numbers': numbers}
	
	return render(request,'accounts/home.html',args)

def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts') 
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'accounts/reg_form.html',args)
	
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user) 

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/dashboard/profile')
		else:
			return redirect('/accounts/change_password')

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form' : form}
		return render(request, 'accounts/change_password.html',args)








#def change_password(request):
#	if request.method == 'POST':
#		form = PasswordChangeForm(request.POST,instance=request.user)

#		if form.is_valid():
#			form.save()
#			return redirect('/dashboard/profile')

#	else:
#		from = PasswordChangeForm

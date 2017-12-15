from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done  

urlpatterns = [

		url(r'^$', views.home, name = 'home'),
		url(r'^login/$',login, {'template_name': 'accounts/login.html'}, name = 'login'),
		url(r'^logout/$',logout, {'template_name': 'accounts/logout.html'}, name ='logout'),
		url(r'^register/$', views.register, name='register'),
		url(r'^change-password/$', views.change_password, name='change_password'),
		url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html'}, name = 'reset-password'),
		url(r'^reset-password/done/$', password_reset_done, name='password_reset_done')

			]


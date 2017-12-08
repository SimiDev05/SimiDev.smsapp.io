from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done  

urlpatterns = [

		url(r'^$', views.home),
		url(r'^login/$',login, {'template_name': 'accounts/login.html'}),
		url(r'^logout/$',logout, {'template_name': 'accounts/logout.html'}),
		url(r'^register/$', views.register, name='register'),
		url(r'^change-password/$', views.change_password, name='change_password'),
		url(r'^reset-password/$', password_reset, name='reset_password'),
		url(r'^reset-password/done/$', password_reset_done, name='password_reset_done')

			]



from django.conf.urls import url
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^$', views.gallery),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name= 'edit_profile'),
   
]

 
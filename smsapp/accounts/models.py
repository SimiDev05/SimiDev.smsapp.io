from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#description = models.CharField(max_lenght=250, default='')
	age = models.IntegerField(default=0)
	#Gender = models.CharField
	Grade = models.IntegerField(default=0)
	#Address = models.CharField(max_lenght=250)
	#Email = models.charfield(max_lenght=250)
	Phonenumber = models.IntegerField(default=0) 


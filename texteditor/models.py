from django.db import models
from django import forms

# Create your models here.

class user_details(models.Model):
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	email=models.EmailField(max_length=70,blank=True, null= True)
	def __str__(self):
		return '%s' % (self.username)

class Admin:
	pass

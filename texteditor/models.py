from django.db import models
from django import forms

# Create your models here.

class user_details(models.Model):
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	email=models.EmailField(max_length=70,blank=True, null= True, unique= True)
	def __str__(self):
		return '%s' % (self.username)

class Admin:
	pass

class ContactForm(models.Model):
	"""
	define a contact form class
	"""
	# this will be rendered like
	# <input class="form-control" id="id_subject" name="subject" size="48" type="text">
	# valid if not empty
	subject = forms.CharField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control'}))
	# A CharField that checks that the value is a valid email address.
	email = forms.EmailField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5 , 'class':'form-control'}))
	print subject

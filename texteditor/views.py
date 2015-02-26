# Create your views here.
from django.shortcuts import *
from texteditor.models import *

def home(request):
	firstname = "aravindh"
	lastname = "kumar"
	return render_to_response("index.html",locals())
def login(request):
 	message = "Kindly Login To Continue"
 	return render_to_response("login.html",locals())
def Newuser(request):
	message = "New User Signup Here"
	username = request.POST['uname'];
	password = request.POST['pass'];
	email = request.POST['email'];
	p=user_details(username = username,password = password,email = email)
	p.save()
  	return render_to_response("dashboard.html",locals())
def NavBar(request):
 	message = "NavBar"
 	return render_to_response("navbar.html",locals())
def signin(request):
	username = request.POST['uname'];
	password = request.POST['pass'];
	m =user_details.objects.get(username=username)
	if m.password == password:
		request.session['uname'] = m.username
		return HttpResponseRedirect("/dashboard")
	else:
		return HttpResponseRedirect("/login")

def dashboard(request):
	print "ececuting dashboard"
	import os
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
		print('%s' % dirName)
		for fname in fileList:
			print('\t%s' % fname)
	message = "Success Fully loged in"
	print "ececuting dashboard stoped"
	return render_to_response("dashboard.html",locals())
def sign_nav(request):
	return render_to_response("signup.html",locals())


# Create your views here.
from django.shortcuts import *
from texteditor.models import *
# from os import listdir
# from os.path import isfile, join
from os import walk
import json
import os
import urllib

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
	return HttpResponseRedirect("/login")
  	# return render_to_response("login.html",locals())
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
	f = []
	for (dirpath, dirnames, filenames) in walk('.'):
	    f.extend(dirnames)
	    break	
	return render_to_response("dashboard.html",locals())
def subDetails(request):
	data = {}		
	folder = request.POST['folderName']
	# print folder
	pat="/home/aravindh/codeanywhere/"+folder
	# print pat
	for (dirpath, dirnames, filenames) in walk(pat):		
		data ['folder'] = dirnames	
		data ['files'] = filenames
		break	       
	return HttpResponse(json.dumps(data), content_type='application/json')

def openTab(request):
	urltoSave = request.POST['urltoSave']
	# pathOrginal = os.path.dirname(os.path.abspath(__file__))
	# data = pathOrginal.replace("texteditor", "")+urltoSave
	# print data
	#print pathOrginal
	#os.system('cd ..')
	#pathOrginalafter = os.path.dirname(os.path.abspath(__file__))
	#print pathOrginalafter
	filecontent = request.POST['fd']
	print type(filecontent)
	# f=fi
	#print filecontent
	# with open(data, "wb") as write_file:
	# 	write_file.write(filecontent)	
	file = open(urltoSave, "w")
	print "encodeing"	
	filecontent=filecontent.encode("ISO-8859-1")
	print filecontent	
	# filecontent=filecontent.encode("utf-8")
	file.write(filecontent)	
	file.close()
	#print "filewritten success"
	return HttpResponse()

def openAjax(request):
	data = {}		
	folder = request.POST['fna']
	print folder		
	pat="/home/aravindh/codeanywhere/codeanywhere/templates"+folder
	print pat
	file = open(pat, 'r')
	# file=file.encode("utf-8")
	fc=file.read()
	print "before decode "+fc
	fc=unicode(fc, "ISO-8859-1")	
	#print "after decode "+fc
	data ['path'] = pat
	data ['content'] = fc
	return HttpResponse(json.dumps(data), content_type='application/json')
	
def sign_nav(request):
	return render_to_response("signup.html",locals())


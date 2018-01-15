from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import *
from home.views import *
from home.urls import *

# Create your views here.
def landing(request):
	if request.user.is_authenticated():
		#return render(request, 'landing.html')
		return redirect('/home')
	else:
		return render(request, 'landing.html')
			

def signin(request):
	return render(request, 'login.html')	

def registerView(request):
	if request.method == 'POST':
		post = request.POST

		email = post.get('email')
		password1 = post.get('pass')
		password2 = post.get('cpass')
		username = getUsername(email)

		if password1 != password2:
			messages.warning(request, "passwords do not match", fail_silently=True)
			return render(request, 'login.html')

    	user = User.objects.create_user(username=username, email=email)
    	user.set_password(password1)
    	user.save()
    	user.backend = 'django.contrib.auth.backends.ModelBackend'
    	login(request, user)
    	return redirect('/home')
		

def loginView(request):
	if request.method == 'POST':
		#user = request.user
		post = request.POST
		email = post['email']
		password = post['pass']
		username = getUsername(email)
		user = authenticate(username=username, email=email, password=password)
		try:
			if user is not None:
				login(request, user)
				print user
				return redirect('/home')
			else:
				return HttpResponse("<h1>User does not exist or Invalid Credentials!</h1>")
		except:
			return HttpResponse("<h1>User does not exist or Invalid Credentials!</h1>")


def getUsername(email):
    email = str(email)
    index = email.index('@')

    answer = email[:index]
    return answer

def home(request):
    if request.user.is_authenticated():
    	ad = Advertisment.objects.all()
    	no = Notification.objects.filter(not_user=request.user)
    	#ad = ad.reverse()
        return render(request,'home.html', {'ad' : ad, 'notify':no})
    else:
        return redirect("/login")  

# def ad(request):
# 	if request.method=='POST':
# 		post=request.POST
# 		email = post.get('email')
# 		password1 = post.get('pass')
# 		password2 = post.get('cpass')
# 		username = getUsername(email)
# 	return render(request,'formpage.html')


def logoutView(request):
	logout(request)
	return render(request, 'landing.html')	

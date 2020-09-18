from django.shortcuts import render,redirect
from usersin.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
import random,string
# Create your views here.
def home(req):
	return render(req,'usersin/home.html')


def register(req):
	error=""
	if req.method=="POST":
		fname=req.POST['first_name']
		lname=req.POST['last_name']
		uname=req.POST['username']
		em=req.POST['email']
		img=req.FILES['img']
		age=req.POST['age']
		pwd1=req.POST['pswd1']
		pwd=req.POST['pswd']
		ui=req.POST['ui']
		
		if(pwd==pwd1):
			if(len(ui)==6 and ui.isalnum()):
				x=ui
			else:
				x=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(8))
			try:
				user=User.objects.create_user(first_name=fname,last_name=lname,
					username=uname,email=em,password=pwd)
				Profile.objects.create(user=user,image=img,age=age,uniqueid=x)
				error = "no"
			except:
				error="yes"
		else:
			error="yes"
	context={'error':error}
	return render(req,'usersin/register.html',context)


def signin(req):
	error=""
	if req.method=="POST":
		uname=req.POST['uname']
		pwd=req.POST['pwd']
		user=authenticate(username=uname,password=pwd)
		try:
			if user:
				login(req,user)
				error="no"
			else:
				error="yes"
		except:
			error="yes"
	context={'error':error}
	return render(req,'usersin/signin.html',context)

@login_required()
def signout(req):
	logout(req)
	return redirect('home')

@login_required()
def changepassword(req):
	error=""
	if req.method=="POST":
		old=req.POST['oldpwd']
		new=req.POST['newpwd']
		new1=req.POST['newpwd1']
		user=User.objects.get(username__exact=req.user.username)
		if(new==new1):
			user.set_password(new1)
			user.save()
			error="no"
		else:
			error="yes"
	context={'error':error}
	return render(req,'usersin/changepassword.html',context)

@login_required()
def userprofile(req):
	user=User.objects.get(id=req.user.id)
	pro=Profile.objects.get(user=user)
	context={'user':user,'pro':pro}
	return render(req,'usersin/userprofile.html',context)

@login_required()
def editprofile(request):
	user=User.objects.get(id=request.user.id)
	pro=Profile.objects.get(user=user)
	error=""
	if request.method=="POST":
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		if 'img' in request.FILES:
			img=request.FILES['img']
		else:
			img=None
		age=request.POST['mobileno']
		user.first_name=fname
		user.last_name=lname
		pro.age=age
		if img:
			pro.image=img
		try:
			user.save()
			pro.save()
			error="no"
		except:
			error="yes"
	context={"error":error,'user':user,'pro':pro}
	return render(request,'usersin/editprofile.html',context)
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your models here.

def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")
def authenticateadmin(request):    # function for the authentication of the credentials
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    # case 1: user exists
    if user is not None and user.username == "admin":
        login(request,user)
        return redirect('adminhomepage')
    # case 2: user doesnot exists
    if user is None:
        return redirect('adminloginpage')

def adminhomepage(request):   # function for redirecting to the admin home page if the credentials are correct
    return render(request,"pizzaapp/adminhomepage.html")

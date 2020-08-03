from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your models here.

def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")
def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    # case 1: user exists
    if user is not None:
        login(request,user)

    # case 2: user doesnot exists
    if user is None:
        redirect('adminloginpage')

def adminhomepage(request):
    return render(request,"pizzaapp/adminhomepage.html")

from django.shortcuts import render
from django.shortcuts import render
# Create your models here.

def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")
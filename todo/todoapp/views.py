from django.shortcuts import render

def todoview(request):
    return render(request,"todoapp/homepage.html")

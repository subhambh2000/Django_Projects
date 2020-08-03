from django.contrib import admin
from django.urls import path
from .views import adminloginview,adminhomepage,authenticateadmin

urlpatterns = [
    path('admin/',adminloginview,name='adminloginpage'),
    path('authenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepage,name='adminhomepage'),
]

from django.contrib import admin
from django.urls import path
from .views import number,increment,decrement,reset

urlpatterns = [
    path('number/',number),
    path('increment/',increment),
    path('decrement/', decrement),
    path('reset/', reset)
]

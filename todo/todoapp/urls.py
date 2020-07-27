from django.contrib import admin
from django.urls import path
from .views import todoview,addtask,deletetask

urlpatterns = [
    path('',todoview),
    path('addtask/',addtask),
    path('delete/<int:taskid>/',deletetask),
]

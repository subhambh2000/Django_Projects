from django.contrib import admin
from django.urls import path
from .views import todoview,addtask,deletetask,editaskview,editask

urlpatterns = [
    path('',todoview,name='homepage'),
    path('addtask/',addtask),
    path('delete/<int:taskid>/',deletetask),
    path('edit/<int:taskid>/',editaskview),
    path('edit/<int:taskid>/update/',editask),
]

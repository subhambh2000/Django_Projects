from django.shortcuts import render,redirect
from .models import todomodel
def todoview(request):
    myTodo = todomodel.objects.all()
    context = {'myTodo':myTodo}
    return render(request,"todoapp/homepage.html",context)
def addtask(request):
    # function to add the input data to the database
    mytask = request.POST['task']
    todomodel(task=mytask).save()
    return redirect(request.META['HTTP_REFERER'])
def deletetask(request,taskid):
    todomodel.objects.filter(id=taskid).delete()
    return redirect(request.META['HTTP_REFERER'])

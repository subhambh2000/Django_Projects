from django.shortcuts import render,redirect
from .models import CounterModel
# Create your views here.
def number(request):
    num = (CounterModel.objects.filter(id=1)[0]).number
    context = {'number': num}
    return render(request,"pages/number.html",context)
def increment(request):
    # we will write the code to increment the number
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) + 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])
def decrement(request):
    # we will write the code to decrement the number
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) - 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])
def reset(request):
    # we will write the code to reset the number to 0
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

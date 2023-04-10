from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import gform
from .models import grocery
from django.urls import reverse

# Create your views here.
def home(request):
    lt = grocery.objects.all()
    return render(request,'home.html',{'items':lt})

# def home(request,message):
#     lt = grocery.objects.all()
#     return render(request,'home.html',{'items':lt,'message':message})

def join(request):
    if request.method=="POST":
        print("gotpost")
        name = request.POST['Name']
        type = request.POST['type']
        quantity = request.POST['quantity']
        quantity=int(quantity)
        rate = request.POST['rate']
        rate = int(rate)
        amount = rate*quantity
        new = grocery(Name = name,type=type,quantity=quantity,rate=rate,amount=amount)
        new.save()
        form = gform()
        return HttpResponseRedirect(reverse('sitegroc:home'))
        # return render(request,'join.html',{'form':form,'msg':"done"})
    else:
        print("getgot")
        form = gform()
        return render(request,'join.html',{'form':form})
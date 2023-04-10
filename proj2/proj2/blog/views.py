from django.shortcuts import render
from django.http import HttpResponse
from .models import pos

# Create your views here.

def index(request):
    all = pos.objects.all
    return render(request,'index.html', {'all':all})
def join(request):
    if(request.method=="POST"):
        pass
    else:
        return render(request,'join.html')
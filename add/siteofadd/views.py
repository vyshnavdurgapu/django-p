from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def result(request):
    print(request.POST)
    try: 
        num1 = request.POST['num1']
        print(num1)
        num2 = request.POST['num2']
        print(num2)
        res = int(num1)+int(num2)
    except:
        return HttpResponse("rey luvha add kottu")
    else:
        return HttpResponse("result is %s" %res)
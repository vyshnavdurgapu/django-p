from django.shortcuts import render
from django.http import request,HttpResponse
import csv
# Create your views here.
def home(request):
    l=[]
    with open('static/hello.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            l.append(row)
    print(l)
    return HttpResponse("hi ra pufa")


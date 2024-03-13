from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

import random

def sayhello(request):
    return HttpResponse("Hello Django by HttpResponse!")

def sayhelloplus(request):
    return render(request,"hello.html")

def sayhello2(request,username):
    now = datetime.now()
    return render(request,"hello2.html",locals())

def sayhello3(request,username):
    now = datetime.now()
    return render(request,"hello3.html",locals())

def dice(request):
    no = random.randint(1,6)
    return render(request,"dice.html",{"no":no})

def tripledice(request):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    while(no1 == no2):
        no2 = random.randint(1,6)
    while(no1 == no3 or no2 == no3):
        no3 = random.randint(1,6)
    
    return render(request,"tripledice.html",{"no1":no1,"no2":no2,"no3":no3})
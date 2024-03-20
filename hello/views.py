from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

import random

def sayhello(request):
    return HttpResponse("Hello Django by HttpResponse!")

def sayhelloplus(request):
    return render(request,"hello/hello.html")

def sayhello2(request,username):
    now = datetime.now()
    return render(request,"hello/hello2.html",locals())

def sayhello3(request,username):
    now = datetime.now()
    return render(request,"hello/hello3.html",locals())

def dice(request):
    no = random.randint(1,6)
    return render(request,"dice/dice.html",{"no":no})

def tripledice(request):
    
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    no4 = random.randint(1,6)
    no5 = random.randint(1,6)
    no = {"no1":no1,"no2":no2,"no3":no3,"no4":no4,"no5":no5}
        
    return render(request,"dice/tripledice.html",locals())
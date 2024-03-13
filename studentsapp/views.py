from django.shortcuts import render

from studentsapp.models import student

# Create your views here.

def showone(request):
    try:
        std = student.objects.get(cName = "a")
    except:
        errormessage = "讀取錯誤，找不到學生"
        
    return render(request,"showone.html",locals())

def showall(request):
    try:
        stds = student.objects.all().order_by("id")
    except:
        errormessage = "讀取錯誤"
        
    return render(request,"showall.html",locals())
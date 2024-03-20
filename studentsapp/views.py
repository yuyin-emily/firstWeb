from django.shortcuts import render, redirect
from studentsapp.models import student

# Create your views here.

def showone(request):
    try:
        std = student.objects.get(cName = "a")
    except:
        errormessage = "讀取錯誤，找不到學生"
        
    return render(request,"show/showone.html",locals())

def showall(request):
    try:
        stds = student.objects.all().order_by("id")
    except:
        errormessage = "讀取錯誤"
        
    return render(request,"show/showall.html",locals())

def students(request):
    try:
        stds = student.objects.all().order_by("id")
    except:
        errormessage = "讀取錯誤"
        
    return render(request,"show/students.html",locals())

def post(request):
    if request.method == "POST":
        message = request.POST["username"]
    else:
        message = "資料未傳送"
    return render(request,"show/post.html",locals())

def post1(request):
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        unit = student.objects.create(cName=cName,
                                      cSex=cSex,
                                      cBirthday=cBirthday,
                                      cEmail=cEmail,
                                      cPhone=cPhone,
                                      cAddr=cAddr)
        unit.save()
        return redirect("/students")
    else:
        message = "請輸入資料(資料未作驗證)"
    return render(request, "show/post1.html", locals())
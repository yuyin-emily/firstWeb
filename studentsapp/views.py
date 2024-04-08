from django.shortcuts import render, redirect
from studentsapp.models import student
from studentsapp.forms import PostForm

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

def postforms(request):
    postform = PostForm()
    return render(request, "show/postforms.html", locals())

def post2(request):
    if request.method == "POST":
        postform = PostForm()
        if postform.is_valid():
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
            message = "寫入成功"
            return redirect("/students")
        else:
            message = "驗證失敗"
    else:
        message ="姓名、性別、生日必須輸入"
        postform = PostForm()
    return render(request,"show/post2.html",locals())

def delete(request, id=None):
    if request.method == "POST":
        id = request.POST["id"]
    try:
        unit = student.objects.get(id=id)
        unit.delete()
        message = "刪除該筆數據"
        return redirect("/students")
    except:
        if id == None:
            message = ""
        else:
            message = "查無此編號"
    return render(request,"edit/delete.html",locals())

def edit(request, id=None, mode=None):
    if mode == "load":
        unit = student.objects.get(id=id)
        strdate = str(unit.cBirthday)
        strdate2 = strdate.replace("年", "-")
        strdate2 = strdate.replace("月", "-")
        strdate2 = strdate.replace("日", "-")
        unit.cBirthday = strdate2
        return render(request, "edit/edit.html", locals())
    elif mode == "save":
        unit = student.objects.get(id=id)
        unit.cName = request.POST["cName"]
        unit.cSex = request.POST["cSex"]
        unit.cBirthday = request.POST["cBirthday"]
        unit.cEmail = request.POST["cEmail"]
        unit.cPhone = request.POST["cPhone"]
        unit.cAddr = request.POST["cAddr"]
        unit.save()
        message = "已修改..."
        return redirect("/students")
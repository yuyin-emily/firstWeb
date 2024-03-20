"""firstWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#將hello的view import
import hello.views as hviews
import studentsapp.views as sviews

urlpatterns = [
    path("admin/", admin.site.urls),
    #網址路徑,對應執行函式
    
    #hview
    path("", hviews.sayhello),
    path("dice/", hviews.dice),
    path("tripledice/", hviews.tripledice),
    path("helloplus/", hviews.sayhelloplus),
    path("hello2/<str:username>", hviews.sayhello2),
    path("hello3/<str:username>", hviews.sayhello3),
    
    #sview
    path("showone", sviews.showone),
    path("showall", sviews.showall),
    path("students", sviews.students),
    path("post", sviews.post),
]

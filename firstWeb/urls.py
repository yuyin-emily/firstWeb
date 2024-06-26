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
from django.conf.urls.static import static
from django.conf import settings

#將hello的view import
import hello.views as hviews
import studentsapp.views as sviews
import flower.views as fviews

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
    path("post1", sviews.post1),
    path("postforms", sviews.postforms),
    path("post2", sviews.post2),
    
    path("delete", sviews.delete),
    path("delete/<int:id>/", sviews.delete),
    path("edit/", sviews.edit),
    path("edit/<int:id>/<str:mode>", sviews.edit),
    
    
    path('flower/', fviews.flowers),
    path('flower/create/', fviews.create, name='create'),
    path('flower/<slug:slug>/', fviews.detail, name='detail'),
    path('tags/<slug:slug>/', fviews.tags, name='tags'),
    path('flower/edit/<int:pk>', fviews.edit, name='edit'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

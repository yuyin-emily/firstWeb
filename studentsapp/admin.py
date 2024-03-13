from django.contrib import admin

from studentsapp.models import student

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ("id","cName","cSex","cBirthday","cEmail","cPhone","cAddr")
    list_filter = ("cName","cSex")
    search_fields = ("cName",)
    ordering = ("id",)
    
admin.site.register(student,studentAdmin)
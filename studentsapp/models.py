from django.db import models

# Create your models here.

class student(models.Model):
    cName = models.CharField(max_length=20,null=False)
    cSex = models.CharField(max_length=2,null=False,default="M")
    cPhone = models.CharField(max_length=50,blank=True,default="")
    cAddr = models.CharField(max_length=255,blank=True,default="")
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100,blank=True,,default="")
    
    def __str__(self):
        return self.cName
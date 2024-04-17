from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Flower
from django.forms import ModelForm

class FlowerForm(ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'description':forms.Textarea(attrs={"class":"form-control"}),
            'slug':forms.TextInput(attrs={"class":"form-control"}),
            'category':forms.Select(attrs={"class":"form-control"}),
            'tags':forms.SelectMultiple(attrs={"class":"form-control"}),
            'images':forms.FileInput(attrs={"class":"form-control",'id':'image_filed'}),
        }
        labels = {
            'title':'名稱',
            'description':'敘述',
            'slug':'代號',
            'category':'類別',
            'tags':'標籤',
            'images':'圖片',
        }
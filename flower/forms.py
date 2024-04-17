from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Flower
from django.forms import ModelForm

class FlowerForm(ModelForm):
    title = forms.CharField(label="title",widget=forms.TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = Flower
        fields = ["title"]
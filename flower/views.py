from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from flower.models import Flower
from .forms import FlowerForm

# Create your views here.

def flowers(request):
    q = request.GET.get('q', None)
    flowers = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    return render(request, 'flower/flower.html', {'flowers': flowers})

# def flowers(request):
#     q = request.GET.get('q', None)
#     flowers = ''
#     if q is None or q is "":
#         flowers = Flower.objects.all()
#     elif q is not None:
#         flowers = Flower.objects.filter(title_contains=q)
#     return render(request, 'flower.html', {'flowers': flowers })


def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', locals())

def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'flower/flower.html', locals())

def create(request):
    if request.method == "POST":
        if form.valid():
            form.save()
            return HttpResponseRedirect("/flower/")
        else:
            form = FlowerForm()
        return render(request, "flower/edit.html", locals())

def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = FlowerForm(request.POST, instance=flower)
        if form.valid():
            form.save()
            return HttpResponseRedirect("flower/")
        else:
            form = FlowerForm(instance=flower)
        return render(request, "flower/edit.html", locals())


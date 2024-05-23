from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import *
from .models import *

def frontpage(request):
    return render(request, 'frontpage.html')

def receipies(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        n = data.get('name')
        d = data.get('descp')
        i = files.get('image')
        receipe.objects.create(name=n, descp=d, image=i)
        return redirect('/recipe')
    queryset = receipe.objects.all()
    context = {'receipies': queryset}
    return render(request, 'veges.html', context)

def upload(request):
    queryset = receipe.objects.all()
    context = {'recipes': queryset}
    return render(request, 'uploaded.html', context)

def manage(request):
    queryset = receipe.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        queryset = queryset.filter(name__icontains=search_query)
    context = {'recipes': queryset}
    return render(request, 'manage.html', context)

def delete(request, id):
    recipe = get_object_or_404(receipe, id=id)
    recipe.delete()
    return redirect('/manage/')

def update(request, id):
    recipe = get_object_or_404(receipe, id=id)
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        recipe.name = data.get('name')
        recipe.descp = data.get('descp')
        if files.get('image'):
            recipe.image = files.get('image')
        recipe.save()
        return redirect('/manage')
    context = {'receipies': recipe}
    return render(request, 'update.html', context)

def frontpage1(request):
    return render(request, 'frontpage1.html')

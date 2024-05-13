from django.shortcuts import render , redirect
from vege.models import *
from django.shortcuts import get_object_or_404

def frontpage(request):
    return render(request , 'frontpage.html')
def receipies(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        n = data.get('name')
        d = data.get('descp')
        i = files.get('image')
        receipe.objects.create(
            name=n,
            descp=d,
            image=i
        )
        return redirect('/recipe')
    queryset=receipe.objects.all()
    context={'receipies':queryset}
    return render(request,'veges.html',context)

def upload(request):
    queryset = receipe.objects.all()
    context = {'recipes': queryset} 
    return render(request, 'uploaded.html', context)

def manage(request):
    queryset = receipe.objects.all()
    context = {'recipes': queryset} 
    return render(request, 'manage.html', context)
def delete(request, id):
    recipe = get_object_or_404(receipe, id=id)
    recipe.delete()
    return redirect('/manage/')

from django.shortcuts import render , redirect
from vege.models import *

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
        return redirect('/receipies/')
    queryset=receipe.objects.all()
    context={'receipies':queryset}
    
    return render(request, 'veges.html',context)

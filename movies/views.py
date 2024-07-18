from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def home(request):
    movie = Movie.objects.all()
    return render(request,'home.html',{'movie':movie})

def add_movies(request):
    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        desc = request.POST['desc']
        image = request.FILES['image']
        movie= Movie(name=name,year=year,desc=desc,image=image)
        movie.save()
        return redirect('view_movies')
    messages.info(request,"THe Data doesn't Get From Form")
    return render(request,'add_movies.html')

def view_movies(request):
    movie = Movie.objects.all()
    return render(request,'view_movies.html',{'movie':movie})

def update_movies(request,id):
    movie = Movie.objects.get(id=id)
    form = UpdateForm(request.POST,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('view_movies')
    form = UpdateForm(instance=movie)
    return render(request,'edit_movies.html',{'form':form})

def delete_movies(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('view_movies')
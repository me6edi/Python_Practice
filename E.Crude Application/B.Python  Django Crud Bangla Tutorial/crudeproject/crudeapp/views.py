from django.shortcuts import render, redirect
from .models import inserting

# Create your views here.
def index(request):
    data = inserting.objects.all()
    return render(request, 'index.html', {'data':data})



def create(request):
    print(request.POST)
    name = request.GET['name']
    fname = request.GET['fname']
    mname = request.GET['mname']
    age = request.GET['age']

    mehedi = inserting(name=name, fname=fname, mname=mname, age=age)
    mehedi.save()
    return redirect('/')

def delete(request, id):
    data = inserting.objects.get(pk=id)
    data.delete()
    return redirect('/')
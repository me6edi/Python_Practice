from django.shortcuts import render , redirect
from.models import Computer
 
# Create your views here.
def index(request):
    students = Computer.objects.all()
    return render(request, 'index.html', {'students':students})

def delete(request, id):
    students = Computer.objects.get(pk=id)
    students.delete()
    return redirect('/')
 
def edit(request, id):
     students = Computer.objects.get(pk=id)
     context = {
          'students': students
     }
     return render(request, 'edit.html', context)


def add_students(request):
     return render(request, 'add_students.html')

def create(request):
     print(request.POST)
     name = request.GET['name']
     roll = request.GET['roll']
     dpartment = request.GET['dpartment']
     phone = request.GET['phone']
     blood_group = request.GET['blood_group']
     student_list = Computer(name=name, roll=roll, dpartment=dpartment, phone=phone, blood_group=blood_group)
     student_list.save()
     return redirect('/')

def update(request, id):
     students = Computer.objects.get(pk=id)
     students.name = request.GET['name']
     students.roll = request.GET['roll']
     students.dpartment = request.GET['dpartment']
     students.phone = request.GET['phone']
     students.blood_group = request.GET['blood_group']
     students.save()
     return redirect('/')



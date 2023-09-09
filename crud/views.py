from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.

def HomePage(request):
    # form = StudentFp
    if request.method == 'POST':
        submitted_form = StudentForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save();
        
    return render(request,'crud/index.html', {
            'form': StudentForm(),
            'students': Student.objects.all()
    })

def DeleteStudent(request, id):
    student = Student.objects.get(id = id)
    student.delete()
    
    return redirect('homepage')


def EditStudent(request, id):
    if request.method == 'GET':
        student = Student.objects.get(id = id)
        return render(request, 'crud/edit.html', {
            'student': student
        })
    if request.method == 'POST':
        student = Student.objects.get(id = id)
        student.name = request.POST.get('student_name')
        student.email = request.POST.get('student_email')
        student.password = request.POST.get('student_password')
        student.save()
        return redirect('homepage')
# class EditStudent(View):
#     def get(self, request, id):
#         print(id)
        

        
    
    

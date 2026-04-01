from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Teacher
from departement.models import Departement 

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teachers.html", {'teacher_list': teachers})

def add_teacher(request):
    depts = Departement.objects.all()
    if request.method == 'POST':
        dept_id = request.POST.get('department')
        dept_instance = get_object_or_404(Departement, id=dept_id)

        Teacher.objects.create(
    first_name=request.POST.get('first_name'),
    last_name=request.POST.get('last_name'),
    teacher_id=request.POST.get('teacher_id'),
    gender=request.POST.get('gender'),
    departement=dept_instance, 
    date_of_birth=request.POST.get('date_of_birth'), 
    joining_date=request.POST.get('joining_date'),   
    mobile_number=request.POST.get('mobile_number'),
    teacher_image=request.FILES.get('teacher_image')
)
        messages.success(request, 'Teacher added Successfully')
        return redirect('teacher_list')
    
    return render(request, 'teachers/add-teacher.html', {'depts': depts})

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    depts = Departement.objects.all() 

    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.teacher_id = request.POST.get('teacher_id')
        teacher.gender = request.POST.get('gender')
        
        dept_id = request.POST.get('departement')
        teacher.departement = get_object_or_404(Departement, id=dept_id)
        
        if request.FILES.get('teacher_image'):
            teacher.teacher_image = request.FILES.get('teacher_image')

        teacher.save()
        messages.success(request, 'Teacher updated successfully')
        return redirect('teacher_list')
    
    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher, 'depts': depts})


def view_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teacher.delete()
    messages.success(request, 'Teacher deleted successfully')
    return redirect('teacher_list')

from subjects.models import Subject

def teacher_dashboard(request):
    subjects = Subject.objects.all() 
    return render(request, 'teacher/teacher_dashboard.html', {'subjects': subjects})
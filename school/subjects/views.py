from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from teacher.models import Teacher
from departement.models import Departement
from django.contrib import messages


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})


def add_subject(request):
    teachers = Teacher.objects.all()
    depts = Departement.objects.all()

    if request.method == 'POST':
        s_id = request.POST.get('subject_id')
        s_name = request.POST.get('subject_name')
        d_id = request.POST.get('department')
        t_id = request.POST.get('teacher')

      
        dept_instance = get_object_or_404(Departement, id=d_id)
        teacher_instance = get_object_or_404(Teacher, id=t_id)

       
        Subject.objects.create(
            subject_id=s_id,
            subject_name=s_name,
            departement=dept_instance, 
            teacher=teacher_instance
        )
        
        messages.success(request, "Subject added successfully!")
        return redirect('subject_list')

    return render(request, 'subjects/add-subject.html', {'teachers': teachers, 'depts': depts})


def edit_subject(request, pk):
 
    subject = get_object_or_404(Subject, pk=pk)
    teachers = Teacher.objects.all()
    depts = Departement.objects.all()

    if request.method == 'POST':
     
        subject.subject_id = request.POST.get('subject_id')
        subject.subject_name = request.POST.get('subject_name')
        
        d_id = request.POST.get('department')
        t_id = request.POST.get('teacher')
        
       
        subject.departement = get_object_or_404(Departement, id=d_id)
        subject.teacher = get_object_or_404(Teacher, id=t_id)
        
        subject.save() 
        messages.success(request, "Subject updated successfully!")
        return redirect('subject_list')

    return render(request, 'subjects/edit-subject.html', {
        'subject': subject,
        'teachers': teachers,
        'depts': depts
    })
    
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    messages.success(request, "Subject deleted successfully!")
    return redirect('subject_list')
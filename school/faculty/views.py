
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Import ديال الموديلات من الـ apps لخرين
from student.models import Student
from teacher.models import Teacher
from departement.models import Departement
from subjects.models import Subject

# الصفحة الرئيسية (Redirect Logic)
def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')  
        elif request.user.groups.filter(name='Teachers').exists():
            return redirect('teacher_dashboard')
        elif request.user.groups.filter(name='Students').exists():
            return redirect('student_dashboard')
    
    return render(request, 'authentication/login.html')

# Dashboard ديال الـ Admin (فيه الحساب ديال كولشي)
@login_required
def admin_dashboard(request):
    from student.models import Student
    from teacher.models import Teacher
    from departement.models import Departement
    from subjects.models import Subject

    context = {
        'count_students': Student.objects.count(),
        'count_teachers': Teacher.objects.count(), # غادي نديروها فبلاصت Awards مثلا
        'count_departments': Departement.objects.count(),
        'count_subjects': Subject.objects.count(), # غادي نديروها فبلاصت Revenue
    }
    return render(request, 'home/index.html', context)

@login_required
def teacher_dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'students/student-dashboard.html')
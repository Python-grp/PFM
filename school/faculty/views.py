from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Public view
def index(request):
    # If user is already logged in, redirect to appropriate dashboard
    if request.user.is_authenticated:
        
        if request.user.is_staff:
            return redirect('admin_dashboard')  
      
        elif request.user.groups.filter(name='Teachers').exists():
            return redirect('teacher_dashboard')
        elif request.user.groups.filter(name='Students').exists():
            return redirect('student_dashboard')

    # Otherwise, show login page
    return render(request, 'authentication/login.html')



@login_required
def admin_dashboard(request):
    return render(request, 'Home/index.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'students/student-dashboard.html')

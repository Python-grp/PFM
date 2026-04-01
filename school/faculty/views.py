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

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Department, Subject
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from home_auth.decorators import admin_required

from .forms import DepartmentForm, SubjectForm

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_admin', False)

class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'faculty/department_list.html'
    context_object_name = 'department_list'

class DepartmentCreateView(AdminRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'faculty/department_form.html'
    success_url = reverse_lazy('department-list')

class DepartmentUpdateView(AdminRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'faculty/department_form.html'
    success_url = reverse_lazy('department-list')

class DepartmentDeleteView(AdminRequiredMixin, DeleteView):
    model = Department
    template_name = 'faculty/department_confirm_delete.html'
    success_url = reverse_lazy('department-list')

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'faculty/subject_list.html'
    context_object_name = 'subject_list'

class SubjectCreateView(AdminRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'faculty/subject_form.html'
    success_url = reverse_lazy('subject-list')

class SubjectUpdateView(AdminRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'faculty/subject_form.html'
    success_url = reverse_lazy('subject-list')

class SubjectDeleteView(AdminRequiredMixin, DeleteView):
    model = Subject
    template_name = 'faculty/subject_confirm_delete.html'
    success_url = reverse_lazy('subject-list')

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Exam, Result
from django.contrib.auth.mixins import LoginRequiredMixin
from home_auth.mixins import AdminOrTeacherRequiredMixin
from .forms import ExamForm, ResultForm


class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'exam/exam_list.html'
    context_object_name = 'exam_list'

class ExamCreateView(AdminOrTeacherRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam/exam_form.html'
    success_url = reverse_lazy('exam-list')

class ExamUpdateView(AdminOrTeacherRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exam/exam_form.html'
    success_url = reverse_lazy('exam-list')

class ExamDeleteView(AdminOrTeacherRequiredMixin, DeleteView):
    model = Exam
    template_name = 'exam/exam_confirm_delete.html'
    success_url = reverse_lazy('exam-list')

class ResultListView(LoginRequiredMixin, ListView):
    model = Result
    template_name = 'exam/result_list.html'
    context_object_name = 'result_list'
    
    def get_queryset(self):
        user = self.request.user
        val_is_student = getattr(user, 'is_student', False)
        val_is_teacher = getattr(user, 'is_teacher', False)
        val_is_admin = getattr(user, 'is_admin', False)
        
        if val_is_student:
            return Result.objects.filter(student__student_id=user.username)
        elif val_is_teacher and not val_is_admin:
            return Result.objects.filter(exam__subject__teacher__teacher_id=user.username)
        
        return Result.objects.all()

class ResultCreateView(AdminOrTeacherRequiredMixin, CreateView):
    model = Result
    form_class = ResultForm
    template_name = 'exam/result_form.html'
    success_url = reverse_lazy('result-list')

class ResultUpdateView(AdminOrTeacherRequiredMixin, UpdateView):
    model = Result
    form_class = ResultForm
    template_name = 'exam/result_form.html'
    success_url = reverse_lazy('result-list')

class ResultDeleteView(AdminOrTeacherRequiredMixin, DeleteView):
    model = Result
    template_name = 'exam/result_confirm_delete.html'
    success_url = reverse_lazy('result-list')

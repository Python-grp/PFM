from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Holiday, TimeTable
from django.contrib.auth.mixins import LoginRequiredMixin
from home_auth.mixins import AdminRequiredMixin
from .forms import HolidayForm, TimeTableForm

class HolidayListView(LoginRequiredMixin, ListView):
    model = Holiday
    template_name = 'planning/holiday_list.html'
    context_object_name = 'holiday_list'

class HolidayCreateView(AdminRequiredMixin, CreateView):
    model = Holiday
    form_class = HolidayForm
    template_name = 'planning/holiday_form.html'
    success_url = reverse_lazy('holiday-list')

class HolidayUpdateView(AdminRequiredMixin, UpdateView):
    model = Holiday
    form_class = HolidayForm
    template_name = 'planning/holiday_form.html'
    success_url = reverse_lazy('holiday-list')

class HolidayDeleteView(AdminRequiredMixin, DeleteView):
    model = Holiday
    template_name = 'planning/holiday_confirm_delete.html'
    success_url = reverse_lazy('holiday-list')

class TimeTableListView(LoginRequiredMixin, ListView):
    model = TimeTable
    template_name = 'planning/timetable_list.html'
    context_object_name = 'timetable_list'

class TimeTableCreateView(AdminRequiredMixin, CreateView):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'planning/timetable_form.html'
    success_url = reverse_lazy('timetable-list')

class TimeTableUpdateView(AdminRequiredMixin, UpdateView):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'planning/timetable_form.html'
    success_url = reverse_lazy('timetable-list')

class TimeTableDeleteView(AdminRequiredMixin, DeleteView):
    model = TimeTable
    template_name = 'planning/timetable_confirm_delete.html'
    success_url = reverse_lazy('timetable-list')
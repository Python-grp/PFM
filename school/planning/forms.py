from django import forms
from .models import Holiday, TimeTable

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['title', 'start_date', 'end_date', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['day', 'start_time', 'end_time', 'subject', 'teacher', 'student_class']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control'}),  # assuming it's text or you can make it select if Class model exists
        }

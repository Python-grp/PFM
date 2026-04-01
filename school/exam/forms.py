from django import forms
from .models import Exam, Result

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'date', 'subject', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['exam', 'student', 'marks_obtained', 'total_marks', 'remarks']
        widgets = {
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Department, Subject

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'head_of_department', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'head_of_department': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'department', 'teacher']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
        }

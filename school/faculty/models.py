from django.db import models
from teacher.models import Teacher

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=150)
    head_of_department = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='headed_departments')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='subjects')

    def __str__(self):
        return f"{self.name} ({self.code})"

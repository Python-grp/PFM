from django.db import models
from faculty.models import Subject
from teacher.models import Teacher

# Create your models here.
class Holiday(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title

class TimeTable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=15, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    student_class = models.CharField(max_length=50) # To easily match with Student.student_class

    def __str__(self):
        return f"{self.student_class} - {self.subject.name} ({self.day})"
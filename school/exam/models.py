from django.db import models
from faculty.models import Subject
from student.models import Student

# Create your models here.

class Exam(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.subject.name}"

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    remarks = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('exam', 'student')

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.exam.title}"

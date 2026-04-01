from django.db import models
from teacher.models import Teacher
from departement.models import Departement

class Subject(models.Model):
    subject_id = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=100)
    
    # تأكدي أن هاد السطور مافيهمش فراغ زايد فالبداية
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name
    
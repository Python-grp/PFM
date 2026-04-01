from django.db import models
class Departement(models.Model):
    name = models.CharField(max_length=100)
    department_id = models.CharField(max_length=50, null=True, blank=True)
    head_of_department = models.CharField(max_length=100, null=True, blank=True)

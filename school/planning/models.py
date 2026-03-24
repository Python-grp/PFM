from django.db import models

# Create your models here.
class Holiday(models.Model):
    title=models.CharField(max_length=100)
    start_date=models.DateField
    end_date=models.DateField
    description=models.CharField(max_length=300)
    def __str__(self):
        return self.title
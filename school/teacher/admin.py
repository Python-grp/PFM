from django.contrib import admin
from .models import Teacher

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'teacher_id', 'gender', 'date_of_birth',  'joining_date', 'mobile_number')
  search_fields = ('first_name', 'last_name', 'teacher_id')
  list_filter = ('gender',)
  readonly_fields = ('teacher_image',)
list_display = ('first_name', 'last_name', 'teacher_id', 'departement')